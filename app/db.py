from os							import getenv
from sqlite3					import connect
from contextlib					import closing
from pygwarts.magical.spells	import patronus
from dotenv						import load_dotenv








load_dotenv()








def db_delete(word :str, loggy) -> str | None :

	"""
		Will try to delete word from db
		returns None in case of success, str as problem description otherwise
	"""

	if	not isinstance(word,str):

		reason = f"Invalid word type {type(word)} to delete from db"
		loggy.warning(reason)
		return reason

	try:

		connection = connect(getenv("DB_PATH"))

		with closing(connection):

			current = connection.execute("SELECT word,state FROM navbow WHERE word=%s"%word).fetchall()

			if	not current:

				reason = f"\"{word}\" cannot be deleted cause it is not in db"
				loggy.warning(reason)
				return reason


			if	1 <len(current):

				reason = f"\"{word}\" will not be deleted cause it has multiple states in db"
				loggy.warning(reason)
				return reason


			op = connection.execute("DELETE FROM navbow WHERE word=%s"%word).fetchall()
			still = connection.execute("SELECT word,state FROM navbow WHERE word=%s"%word).fetchall()


			if	still:

				reason = "%s\"%s\" not deleted"%("delete output is abnormal, " if op else "",word)
				loggy.warning(reason)
				return reason


			loggy.info("\"%s\" deleted from db%s"%(word," but output is abnormal" if op else ""))


	except	Exception as E : self.loggy.warning(f"\"{word}\" delete failed due to {patronus(E)}")








def db_accept(word :str, loggy) -> str | None :

	"""
		Will try to accept word (convert from unknown or 0 to known or 1)
		returns None in case of success, str as problem description otherwise
	"""

	if	not isinstance(word,str):

		reason = f"Invalid word type {type(word)} to update"
		loggy.warning(reason)
		return reason

	try:

		connection = connect(getenv("DB_PATH"))

		with closing(connection):

			current = connection.execute("SELECT word,state FROM navbow WHERE word=%s"%word).fetchall()

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


			op = connection.execute("UPDATE navbow SET state=1 WHERE word=%s"%word).fetchall()
			still = connection.execute("SELECT word,state FROM navbow WHERE word=%s AND state=0"%word).fetchall()


			if	still:

				reason = "%s\"%s\" not updated"%("update output is abnormal, " if op else "",word)
				loggy.warning(reason)
				return reason


			loggy.info("\"%s\" updated to known%s"%(word," but output is abnormal" if op else ""))


	except	Exception as E : self.loggy.warning(f"\"{word}\" update failed due to {patronus(E)}")







