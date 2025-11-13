from os							import getenv
from typing						import Set
from typing						import List
from typing						import Tuple
from collections.abc			import Sequence
from sqlite3					import connect
from operator					import itemgetter
from contextlib					import closing
from pygwarts.magical.spells	import patronus








def db_analysis_check(pendings :Sequence[str], loggy=None) -> Set[str] | str :

	"""
		Fetches words filtered by "pendings" set. Always returns a set, either with
		strings that correspond to words matched in db or empty.
	"""

	try:

		db = getenv("DB_PATH")
		table = getenv("TABLE_NAME")
		connection = connect(db)
		if loggy : loggy.debug(f"Established connection to db: \"{db}\"")


		with closing(connection):


			query = "SELECT word FROM %s WHERE word IN ('%s')"%(table,"','".join(pendings))
			if loggy : loggy.debug(f"Constructed query: {query}")
			current = connection.execute(query).fetchall()
			if loggy : loggy.debug("Query result no exception")


			if loggy : loggy.info(f"Fetched {len(current)} matches from database")
			return set(map(itemgetter(0),current))


	except	Exception as E:

		if loggy : loggy.warning(f"Fetching db failed due to {patronus(E)}")
		return set()








def db_fetch(loggy) -> List[str] | str :

	"""
		Fetches all rows from db and returns it as list of tuples.
		Any Exception caught will be returned as "reason" string instead of rows.
	"""

	try:

		db = getenv("DB_PATH")
		table = getenv("TABLE_NAME")
		connection = connect(db)
		loggy.debug(f"Established connection to db: \"{db}\"")


		with closing(connection):


			query = "SELECT word,added,source FROM %s"%table
			loggy.debug(f"Constructed query: {query}")
			current = connection.execute(query).fetchall()
			loggy.debug("Query result no exception")


			if	not current:

				reason = f"No rows found in database"
				loggy.warning(reason)
				return reason


			loggy.info(f"Fetched {len(current)} rows from database")
			return sorted(current,key=itemgetter(1,0))


	except	Exception as E:

		reason = f"Fetching db failed due to {patronus(E)}"
		loggy.warning(reason)
		return reason








def db_remove(word :str, loggy) -> None | str :

	"""
		Will try to remove word from db
		returns None in case of success, str as problem description otherwise
	"""

	if	not isinstance(word,str):

		reason = f"Invalid word type {type(word)} to remove from db"
		loggy.warning(reason)
		return reason

	try:

		db = getenv("DB_PATH")
		connection = connect(db)
		table = getenv("TABLE_NAME")
		loggy.debug(f"Established connection to db: \"{db}\"")


		with closing(connection):


			query = "SELECT word FROM %s WHERE word='%s'"%(table,word)
			loggy.debug(f"Constructed query: {query}")
			current = connection.execute(query).fetchall()
			loggy.debug(f"Query result: {current}")


			if	not current:

				reason = f"\"{word}\" cannot be removed cause it is not in db"
				loggy.warning(reason)
				return reason


			if	1 <len(current):

				reason = f"\"{word}\" will not be removed cause it has multiple states in db"
				loggy.warning(reason)
				return reason


			query = "DELETE FROM %s WHERE word='%s'"%(table,word)
			loggy.debug(f"Constructed query: {query}")
			op = connection.execute(query).fetchall()
			loggy.debug(f"Query result: {op}")


			query = "SELECT word FROM %s WHERE word='%s'"%(table,word)
			loggy.debug(f"Constructed query: {query}")
			still = connection.execute(query).fetchall()
			loggy.debug(f"Query result: {still}")


			if	still:

				reason = "%s\"%s\" not removed"%("remove output is abnormal, " if op else "",word)
				loggy.warning(reason)
				return reason


			connection.commit()
			loggy.info("\"%s\" removed from db%s"%(word," but output is abnormal" if op else ""))


		loggy.debug(f"Closed connection to db: \"{db}\"")


	except	Exception as E:

		reason = f"\"{word}\" remove failed due to {patronus(E)}"
		loggy.warning(reason)
		return reason








def db_accept(word :str, loggy) -> None | str :

	"""
		Will try to accept word (convert from unknown or 0 to known or 1)
		returns None in case of success, str as problem description otherwise
	"""

	if	not isinstance(word,str):

		reason = f"Invalid word type {type(word)} to update"
		loggy.warning(reason)
		return reason

	try:

		db = getenv("DB_PATH")
		connection = connect(db)
		table = getenv("TABLE_NAME")
		loggy.debug(f"Established connection to db: \"{db}\"")


		with closing(connection):


			query = "SELECT word,state FROM %s WHERE word='%s'"%(table,word)
			loggy.debug(f"Constructed query: {query}")
			current = connection.execute(query).fetchall()
			loggy.debug(f"Query result: {current}")


			if	not current:

				reason = f"\"{word}\" cannot be updated cause it is not in db"
				loggy.warning(reason)
				return reason


			if	1 <len(current):

				reason = f"\"{word}\" will not be updated cause it has multiple states in db"
				loggy.warning(reason)
				return reason


			if	current[0]:

				reason = f"\"{word}\" cannot be updated cause it is not in unknown state"
				loggy.warning(reason)
				return reason


			query = "UPDATE %s SET state=1 WHERE word='%s'"%(table,word)
			loggy.debug(f"Constructed query: {query}")
			op = connection.execute(query).fetchall()
			loggy.debug(f"Query result: {op}")


			query = "SELECT word,state FROM %s WHERE word='%s' AND state=0"%(table,word)
			loggy.debug(f"Constructed query: {query}")
			still = connection.execute(query).fetchall()
			loggy.debug(f"Query result: {still}")


			if	still:

				reason = "%s\"%s\" not updated"%("update output is abnormal, " if op else "",word)
				loggy.warning(reason)
				return reason


			connection.commit()
			loggy.info("\"%s\" updated to known%s"%(word," but output is abnormal" if op else ""))


		loggy.debug(f"Closed connection to db: \"{db}\"")


	except	Exception as E:

		reason = f"\"{word}\" update failed due to {patronus(E)}"
		loggy.warning(reason)
		return reason







