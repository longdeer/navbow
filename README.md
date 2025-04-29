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
Navtex messages must be constructed according to "NAVTEX MANUAL" by IMO. This is a handy tool,
that allows filtering out determined information and attract attention to probably controversial moments
in messages.
It was tested on messages of 10 years archive from ``https://www.navtex.net/navtex-archive.html``.
Besides words classification, Navanalyzer provides additional things discovery:
<li>invalid headers - easy detection;</li>
<li>incorrect dates, outdated messages - might be derived from scan;</li>
<li>not utf-8 symbols - handled by built-in scanner;</li>
<li>unmatched punctuation - will be shown in "analysis";</li>
<li>message structure - difference between original message and built chunks;</li>

From the archive tests the set of valid symbols for Navtex message was obtained:
``'()+,-./0123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ``

Requirements
------------
``python`` >=3.10

Installation
-------------
``
git clone https://github.com/longdeer/NavtexBoWAnalyzer.git
``

Usage
-----
```
from NavtexBoWAnalyzer import Navanalyzer
bow = dict()
navana = Navanalyzer("A")						# Passing station literal
analysis = navana.with_mapping("/path/to/file", bow)
if not analysis["state"]: print(analysis["message"])			# 0 state means broken or empty file
else:
	print("\n".join( " ".join(line) for line in analysis["air"] ))	# Building sanitized message
	print(analysis["analysis"]["coords"])				# Detected coordinates
	print(analysis["analysis"]["alnums"])				# Detected alphabetic numbers
	print(analysis["analysis"]["nums"])				# Detected numbers
	print(analysis["analysis"]["known"])				# Detected known words (was in BoW)
	print(analysis["analysis"]["unknown"])				# Detected unknown words (was not in BoW)
	print(analysis["analysis"]["pending"])				# Detected pending words (was 0 in BoW)
	print(analysis["analysis"]["punct"])				# Detected unmatched punctuation
	print(analysis["analysis"].get("header"))			# Detected Station Subject Number (optional)
	print(analysis["analysis"].get("DTG"))				# Detected Date Time Group (optional)
	print("\n".join(analysis["raw"]))				# Original file content
```
