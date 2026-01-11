Navtex messages analyzing tool
==============================

General information
-------------------
<ul>
  <li>Navtex is an international automated direct-printing service for promulgation of
maritime safety information (MSI), navigational and meteorological warnings, meteorological
forecasts and other urgent safety-related messages to ships. It was developed to provide a
low-cost, simple and automated means of receiving MSI on board ships at sea in coastal
waters. The information transmitted may be relevant to all sizes and types of vessels and the
selective message-rejection feature ensures that mariners can receive MSI broadcasts which
are tailored to their particular needs.
  </li>
  <li>NAVTEX fulfills an integral role in the Global Maritime Distress and Safety System
(GMDSS) developed by the International Maritime Organization (IMO) and incorporated into
the 1988 amendments to the International Convention for the Safety of Life at Sea
(SOLAS), 1974, as a requirement for ships to which the Convention applies.
  </li>
</ul>

Delimitation of METAREAs
------------------------
![image](https://github.com/user-attachments/assets/29c92b08-fc42-487c-b81b-1bb34b30621f)

Delimitation of NAVAREAs
------------------------
![image](https://github.com/user-attachments/assets/54894784-130f-4007-8a40-2b618624859f)

Features
--------
Navtex messages must be constructed according to "NAVTEX MANUAL" by IMO. The information provided by Navtex coordinators to broadcast stations might sometimes content typos. This software can help with messages analysis. It suggests some tools to for filtering out determined information (numbers, coordinates, e.t.c.) and attract attention to probably controversial moments in messages. For example if message will content a word "NORH" the user will be informed about it to decide if it is typo and "NORTH" was meant. It works as a stand-alone server with api for messages input and web interface for controlling and management. Once the message is sent to the server, it will be broken to the words to analyze against the inner words database, which must be populated by user, accepting the "right" words and discarding "mistakes". All this information will be accessible on the web interface. It was tested on messages of 10+ years archive from `https://www.navtex.net/navtex-archive.html`. Besides words classification, it provides additional things discovery:
<ul>
	<li>invalid headers - easy detection;</li>
	<li>incorrect dates, outdated messages - might be derived from scan;</li>
	<li>not utf-8 symbols - handled by built-in scanner;</li>
	<li>unmatched punctuation - will be shown in message "analysis";</li>
	<li>message structure - auto uppercase and difference between original message and built chunks;</li>
</ul>

Requirements
------------
`python` >=3.10

Installation
-------------
Clone project repository:
```
git clone https://github.com/longdeer/navbow.git
```
Go into project folder and create virtual environment:
```
cd navbow
python3 -m venv .venv
```
Install dependencies:
```
.venv/bin/pip install -r requirements.txt
```
Create `.env` file with corresponding configuration:
```
# Server variables
APP_NAME=string
APP_STATIC_FOLDER='path to navbow project folder'/client
APP_TEMPLATES_FOLDER='path to navbow project folder'/client
LISTEN_ADDRESS=ip address string for server
LISTEN_PORT=port value for server
SERVER_LOGGY='path to server log file'
SERVER_LOGGY_HANDOVER=True or False (more verbose logger output)
SERVER_LOGGY_LEVEL=20 (INFO) level recommended
STATION_LITERAL=your NAVTEX station B1 literal
ACCESS_LIST='{"view":["ip address for accessing"],"control":["ip address for management"],"receive":["ip address from which server is allowed to receive messages"]}'
DB_PATH='path to sqlite3 db file' ('path to navbow project folder'/db/navbow.sqlite3 - recommended)
DB_LOGGY='path to db log file'
DB_LOGGY_LEVEL=20 (INFO) level recommended
DB_LOGGY_HANDOVER=True or False (more verbose logger output)
WORDS_TABLE=words_table_name_for_db
HISTORY_VIEW_TABLE=messages_table_name_for_db
HISTORY_CONTROL_TABLE=words_management_table_name_for_db
HISTORY_VIEW_LIMIT=number of messages to view on web page (1000 - recommended)
```
Run tests for configuration check:
```
.venv/bin/python3 navbow.py --test
```

Usage
-----
Along with web server, `navbow` might be use as just analyzer, when provided with paths to files as standard input to obtain an "analysis" dictionary as standard output:
```
.venv/bin/python navbow.py --analyzer tests/msg/IA76 tests/msg/SE94
```
The above tool doesn't suggest management. For full power use run `navbow` server with `address:port` from `.env` file:
```
.venv/bin/python3 navbow.py --server
```
Or bypass `.env` and provide new `address:port`:
```
.venv/bin/python3 navbow.py --server 192.168.0.42:12345
```
Now you have your `navbow` server running and ready for work. You can visit provided `address:port` page from the clients, which `ip` is in `.env` file's `ACCESS_LIST["view"]` list. Next you can send messages to the server for analysis, from clients with `ip` in `.env` file's `ACCESS_LIST["receive"]` list. You can use `navbow` analyzer to redirect it's output to the running server process on the `address:port` from `.env` file:
```
.venv/bin/python navbow.py --analyzer tests/msg/IA76 tests/msg/SE94 --upload
```
Or on the bypassed `address:port`:
```
.venv/bin/python navbow.py --analyzer tests/msg/IA76 tests/msg/SE94 --upload 127.0.0.1:12345
```
Also you can use another software to upload messages strings to the server:
```
import requests
import json

IA76 = """ZCZC IA76
210800 UTC JAN
BALTIC ICE INFORMATION
VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL 'ICEINFO'
ON VHF OR
PHONE +46 (0)10 492 76 00 AS FOLLOWS:
WHEN PASSING LAT N60 ON VHF CH78.
ARRIVAL REPORT ON VHF CH16 WHEN THE SHIP IS WELL MOORED.
DEPARTURE REPORT ON VHF CH16 LATEST 6 HOURS BEFORE DEPARTURE.
FOR INFORMATION ON RESTRICTIONS GO TO 'BALTICE.ORG'"""

SE94 = """ZCZC SE94
171900 NAVTEX-HAMBURG (NCC)
WEATHERFORECAST FOR GERMAN BIGHT UNTIL 18.11.2019 12 UTC:
NORTHEAST TO NORTH 4 INCREASING ABOUT 6 EASTERN PART LATER
DECREASING A LITTLE AND SHIFTING EAST EASTERN PART AT TIMES MISTY
SEA INCREASING 25 METRE.
OUTLOOK UNTIL 19.11.2019 00 UTC:
WESTERN PART NORTH 6 TO 7 OTHERWISE EAST TO SOUTHEAST 5.
NNNN"""

load = {

	"messages": {

		"IA76": IA76,
		"SE94": SE94
	}
}

requests.post("http://127.0.0.1:12345/ws-cast-receiver", data=json.dumps(load))
```
Or to upload the files itself:
```
import requests
import json

with(

	open("tests/msg/IA76", "rb") as F1,
	open("tests/msg/SE94", "rb") as F2
):
	requests.post("http://127.0.0.1:12345/ws-cast-receiver",files={ "IA76": F1, "SE94": F2 })
```
Now on the `address:port` page you must see two columns. Left column is the "view" of messages "analysis". Right column is the "control" of found words. In the right column you can use "-" and "+" buttons to "forget" and add words to the database, correspondingly.