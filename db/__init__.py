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
def db_match_set(pendings :Sequence[str], connection :Connection, loggy :LibraryContrib) -> Set[str] :

	"""
		Fetches words filtered by "pendings" set. Always returns a set, either with
		strings that correspond to words matched in db or empty.
	"""

	query = "SELECT word FROM %s WHERE word IN ('%s')"%(getenv("WORDS_TABLE"),"','".join(pendings))
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")
	loggy.info(f"Matched {len(current)} row{flagrate(len(current))} from database")

	return set(map(itemgetter(0),current))








@connection_manager
def db_fetch_words(connection :Connection, loggy :LibraryContrib) -> List[Tuple[str]] | str :

	"""
		Fetches all rows from db and returns it as list of tuples.
		Any Exception caught will be returned as "reason" string instead of rows.
	"""

	query = "SELECT word,added,source FROM %s"%getenv("WORDS_TABLE")
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")

	if	not current:

		reason = f"No rows found in database"
		loggy.warning(reason)
		return reason

	loggy.info(f"Fetched {len(current)} row{flagrate(len(current))} from database")
	return sorted(current,key=itemgetter(1,0))








@connection_manager
def db_remove(word :str, connection :Connection, loggy :LibraryContrib) -> None | str :

	"""
		Will try to remove word from db
		returns None in case of success, str as problem description otherwise
	"""

	if	not isinstance(word,str):

		reason = f"Invalid word type {type(word)} to remove from db"
		loggy.warning(reason)
		return reason


	query = "SELECT word FROM %s WHERE word='%s'"%(getenv("WORDS_TABLE"),word)
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug(f"Query result: {current}")


	if	not current:

		reason = f"\"{word}\" cannot be removed cause it is not in db"
		loggy.warning(reason)
		return reason


	query = "DELETE FROM %s WHERE word='%s'"%(getenv("WORDS_TABLE"),word)
	loggy.debug(f"Constructed query: {query}")

	connection.execute(query)
	loggy.debug("Query result no exception")


	query = "SELECT word FROM %s WHERE word='%s'"%(getenv("WORDS_TABLE"),word)
	loggy.debug(f"Constructed query: {query}")

	still = connection.execute(query).fetchall()
	loggy.debug("Query result no exception")


	if	still:

		reason = f"\"{word}\" was not removed from db"
		loggy.warning(reason)
		return reason

	loggy.info(f"\"{word}\" removed from db")








@connection_manager
def db_add(word :str, src :str, connection :Connection, loggy :LibraryContrib) -> None | str :

	"""
		Will try to accept word (convert from unknown or 0 to known or 1)
		returns None in case of success, str as problem description otherwise
	"""

	if	not isinstance(word,str):

		reason = f"Invalid word type {type(word)} to add to db"
		loggy.warning(reason)
		return reason


	query = "SELECT word,added FROM %s WHERE word='%s'"%(getenv("WORDS_TABLE"),word)
	loggy.debug(f"Constructed query: {query}")

	current = connection.execute(query).fetchall()
	loggy.debug(f"Query result: {current}")


	if	current:

		try:	reason = f"\"{word}\" in db since {TimeTurner(current[0][1]).Ymd_dashed}"
		except	Exception as E: reason = f"\"{word}\" in db since when not determined"
		finally:

			loggy.warning(reason)
			return reason


	ts = TimeTurner().epoch
	query = "INSERT INTO %s (word,added,source) VALUES ('%s',%s,'%s')"%(getenv("WORDS_TABLE"),word,ts,src)
	loggy.debug(f"Constructed query: {query}")

	connection.execute(query)
	loggy.debug("Query result no exception")


	query = "SELECT word,added,source FROM %s WHERE word='%s'"%(getenv("WORDS_TABLE"),word)
	loggy.debug(f"Constructed query: {query}")

	added = connection.execute(query).fetchall()
	loggy.debug(f"Query result: {added}")


	if	not added or added[0][1] != ts or added[0][2] != src:

		reason = f"\"{word}\" adding not completed"
		loggy.warning(reason)
		return reason

	loggy.info(f"\"{word}\" successfully added to db")







