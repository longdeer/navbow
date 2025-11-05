from typing						import List
from typing						import Tuple
from os							import getenv
from sqlite3					import connect
from contextlib					import closing
from pygwarts.magical.spells	import patronus








def db_fetch(loggy) -> List[Tuple[str,int]] | str :

	"""
		Fetches all rows from db and returns it as list of tuples.
		Any Exception caught will be returned as "reason" string instead of rows.
	"""

	try:

		db = getenv("DB_PATH")
		connection = connect(db)
		loggy.debug(f"Established connection to db: \"{db}\"")


		with closing(connection):


			query = "SELECT word,state FROM navbow"
			loggy.debug(f"Constructed query: {query}")
			current = connection.execute(query).fetchall()
			loggy.debug("Query result no exception")


			if	not current:

				reason = f"No rows found in database"
				loggy.warning(reason)
				return reason


			loggy.info(f"Fetched {len(current)} rows from database")
			return current


	except	Exception as E:

		reason = f"\"{word}\" delete failed due to {patronus(E)}"
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
		loggy.debug(f"Established connection to db: \"{db}\"")


		with closing(connection):


			query = "SELECT word,state FROM navbow WHERE word='%s'"%word
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


			query = "DELETE FROM navbow WHERE word='%s'"%word
			loggy.debug(f"Constructed query: {query}")
			op = connection.execute(query).fetchall()
			loggy.debug(f"Query result: {op}")


			query = "SELECT word,state FROM navbow WHERE word='%s'"%word
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
		loggy.debug(f"Established connection to db: \"{db}\"")


		with closing(connection):


			query = "SELECT word,state FROM navbow WHERE word='%s'"%word
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


			query = "UPDATE navbow SET state=1 WHERE word='%s'"%word
			loggy.debug(f"Constructed query: {query}")
			op = connection.execute(query).fetchall()
			loggy.debug(f"Query result: {op}")


			query = "SELECT word,state FROM navbow WHERE word='%s' AND state=0"%word
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







