from os								import getenv
from typing							import Set
from typing							import List
from typing							import Tuple
from typing							import Callable
from collections.abc				import Sequence
from sqlite3						import connect
from sqlite3						import Connection
from operator						import itemgetter
from pygwarts.magical.spells		import patronus
from pygwarts.magical.spells		import flagrate
from pygwarts.magical.time_turner	import TimeTurner
from pygwarts.irma.contrib			import LibraryContrib








irma = LibraryContrib(

	handler=getenv("DB_LOGGY"),
	init_name=f"{getenv('APP_NAME')}-db",
	init_level=getenv("DB_LOGGY_LEVEL"),
	force_handover=getenv("DB_LOGGY_HANDOVER")
)








def connection_manager(qurier :Callable[[str | Sequence[str]],Set[str] | List[str] | str | None]):
	def wrapper(*args, loggy=irma):

		try:

			db = getenv("DB_PATH")
			connection = connect(db)
			loggy.debug(f"Established connection to db: \"{db}\"")

			with connection:

				response = qurier(*args, connection, loggy)
				return response

		except	Exception as E:

			reason = f"Query failed due to {patronus(E)}"
			loggy.warning(reason)

			return reason

		finally:
				loggy.debug(f"Closing connection to db: \"{db}\"")
				connection.close()

	return	wrapper








@connection_manager
def wordsdb_match_set(targets :Sequence[str], connection :Connection, loggy :LibraryContrib) -> Set[str] :

	"""
		Fetches words filtered by "targets" set. Always returns a set, either with
		strings that correspond to words matched in db or empty.
	"""

	table = getenv("WORDS_TABLE")
	query = "SELECT word FROM %s WHERE word IN ('%s')"%(table,"','".join(targets))
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")
	loggy.info(f"Matched {len(current)} row{flagrate(len(current))} from {table}")

	return set(map(itemgetter(0),current))








@connection_manager
def wordsdb_fetch(connection :Connection, loggy :LibraryContrib) -> List[Tuple[str]] | str :

	"""
		Fetches all rows from db and returns it as list of tuples.
		Any Exception caught will be returned as "reason" string instead of rows.
	"""

	table = getenv("WORDS_TABLE")
	query = "SELECT word,added,source FROM %s ORDER BY 2,1"%table
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")

	if	not current:

		reason = f"No rows found in {table}"
		loggy.info(reason)
		return reason

	loggy.info(f"Fetched {len(current)} row{flagrate(len(current))} from {table}")
	return current








@connection_manager
def wordsdb_remove(target :str, connection :Connection, loggy :LibraryContrib) -> None | str :

	"""
		Will try to remove word from db
		returns None in case of success, str as problem description otherwise
	"""

	if	not isinstance(target,str):

		reason = f"Invalid word type {type(target)} to remove from db"
		loggy.warning(reason)
		return reason


	table = getenv("WORDS_TABLE")
	query = "SELECT word FROM %s WHERE word='%s'"%(table,target)
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug(f"Query result: {current}")


	if	not current:

		reason = f"\"{target}\" cannot be removed cause it is not in db"
		loggy.warning(reason)
		return reason


	query = "DELETE FROM %s WHERE word='%s'"%(table,target)
	loggy.debug(f"Constructed query: {query}")

	connection.execute(query)
	loggy.debug("Query result no exception")


	query = "SELECT word FROM %s WHERE word='%s'"%(table,target)
	loggy.debug(f"Constructed query: {query}")

	still = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")


	if	still:

		reason = f"\"{target}\" was not removed from db"
		loggy.warning(reason)
		return reason

	loggy.info(f"\"{target}\" removed from db")








@connection_manager
def wordsdb_add(
				target		:str,
				src			:str,
				connection	:Connection,
				loggy		:LibraryContrib
			)->	Tuple[str,float,str] | str :

	"""
		Will try to accept word (convert from unknown or 0 to known or 1)
		returns None in case of success, str as problem description otherwise
	"""

	if	not isinstance(target,str):

		reason = f"Invalid word type {type(target)} to add to db"
		loggy.warning(reason)
		return reason

	target = target.upper()
	table = getenv("WORDS_TABLE")
	query = "SELECT word,added FROM %s WHERE word='%s'"%(table,target)
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug(f"Query result: {current}")


	if	current:

		try:	reason = f"\"{target}\" in db since {TimeTurner(current[0][1]).Ymd_dashed}"
		except	Exception as E: reason = f"\"{target}\" in db since when not determined"
		finally:

			loggy.warning(reason)
			return reason


	ts = TimeTurner().epoch
	query = "INSERT INTO %s (word,added,source) VALUES ('%s',%s,'%s')"%(table,target,ts,src)
	loggy.debug(f"Constructed query: {query}")

	connection.execute(query)
	loggy.debug("Query result no exception")


	query = "SELECT word,added,source FROM %s WHERE word='%s'"%(table,target)
	loggy.debug(f"Constructed query: {query}")

	added = connection.execute(query).fetchall()
	loggy.debug(f"Query result: {added}")


	if	not added or added[0][1] != ts or added[0][2] != src:

		reason = f"\"{target}\" adding not completed"
		loggy.warning(reason)
		return reason

	loggy.info(f"\"{target}\" successfully added to db")
	return added[0]








@connection_manager
def historydb_fetch_view(connection :Connection, loggy :LibraryContrib) -> List[str] | str :

	table = getenv("HISTORY_VIEW_TABLE")
	query = "SELECT view,added FROM %s ORDER BY 2 DESC"%table
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")


	if	not current:

		reason = f"No rows found in {table}"
		loggy.info(reason)
		return reason


	loggy.info(f"Fetched {len(current)} row{flagrate(len(current))} from {table}")
	return list(map(itemgetter(0),current))








@connection_manager
def historydb_add_view(target :str, src :str, connection :Connection, loggy :LibraryContrib) -> None | str :

	if	not isinstance(target,str):

		reason = f"Invalid view type {type(target)} to add to db"
		loggy.warning(reason)
		return reason


	ts = TimeTurner().epoch
	table = getenv("HISTORY_VIEW_TABLE")
	query = "INSERT INTO %s (view,added,source) VALUES ('%s',%s,'%s')"%(table,target,ts,src)
	loggy.debug(f"Constructed query: {query}")

	connection.execute(query)
	loggy.debug("Query result no exception")

	l = len(target)
	loggy.info(f"{l} symbol{flagrate(l)} view successfully added to db")


	query = "SELECT COUNT(*) FROM %s"%table
	loggy.debug(f"Constructed query: {query}")

	count = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")


	if	0 <(rem := count[0][0] -100):

		query = "DELETE FROM %s WHERE (view,added) IN (SELECT view,added FROM %s ORDER BY 2 LIMIT %s)"%(
			table,table,rem
		)
		loggy.debug(f"Constructed query: {query}")

		connection.execute(query)
		loggy.debug("Query result no exception")








@connection_manager
def historydb_fetch_control(connection :Connection, loggy :LibraryContrib) -> List[str] | str :

	table = getenv("HISTORY_CONTROL_TABLE")
	query = "SELECT word FROM %s ORDER BY 1"%table
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")


	if	not current:

		reason = f"No rows found in {table}"
		loggy.info(reason)
		return reason


	loggy.info(f"Fetched {len(current)} row{flagrate(len(current))} from {table}")
	return list(map(itemgetter(0),current))








@connection_manager
def historydb_add_control(
							targets		:str | Sequence[str],
							src			:str,
							connection	:Connection,
							loggy		:LibraryContrib
						)-> None | str	:

	table = getenv("HISTORY_CONTROL_TABLE")

	if	isinstance(targets,str):

		l = 1
		query = "INSERT INTO %s (word,added,source) VALUES ('%s',%s,'%s')"%(
			table, targets, TimeTurner().epoch, src
		)
	else:
		l = len(targets)
		query = "INSERT INTO %s (word,added,source) VALUES %s"%(

			table,
			",".join( "('" + target + f"',{TimeTurner().epoch},'{src}')" for target in targets )
		)

	loggy.debug(f"Constructed query: {query}")

	connection.execute(query)
	loggy.debug("Query result no exception")

	loggy.info(f"{l} control word{flagrate(l)} successfully added to db")








@connection_manager
def historydb_remove_control(
								targets		:str | Sequence[str],
								connection	:Connection,
								loggy		:LibraryContrib
							)-> None | str	:

	table = getenv("HISTORY_CONTROL_TABLE")

	if	isinstance(targets,str):

		l = 1
		query = "DELETE FROM %s WHERE word='%s'"%(table, targets)
	else:
		l = len(targets)
		query = "DELETE FROM %s WHERE word IN (%s)"%(
			table, ",".join( "'" + target + "'" for target in targets )
		)

	loggy.debug(f"Constructed query: {query}")

	connection.execute(query)
	loggy.debug("Query result no exception")

	loggy.info(f"{l} control word{flagrate(l)} probably removed from db")







