Datenbanken
============

:Authors: - Uwe Müeller
:Date: 2013-03-01

MySQL und PostgesSQL
--------------------

Datenbanken können mit hsadmin auf der Kommandozeile oder im Browser angelegt werden.
HSadmin -> shell Webfrontend

Datenbankuser anlegen
---------------------

MySQL
-----

hsadmin -c mysqluser.add --set:name=xyz00_dbuser --set:password=geheim

PostgesSQL
----------

hsadmin -c postgresqluser.add --set:name=xyz00_dbuser --set:password=geheim

Datenbankuser löschen
--------------------

MySQL
-----

hsadmin -c mysqluser.delete --set:name=xyz00_dbuser 

PostgesSQL
----------

hsadmin -c postgresqluser.delete --set:name=xyz00_dbuser 

Datenbank anlegen
=================

MySQL
-----

hsadmin -c mysqldb.add --set:name=xyz00_mydatabase --set:owner=xyz00_dbuser [ --set:encoding=latin1 ]

PostgesSQL
----------

hsadmin -c postgresqldb.add --set:name=xyz00_mydatabase --set:owner=xyz00_dbuser [ --set:encoding=LATIN1 ]

Wird das Encoding weggelassen, ist der Default  "UTF-8".

Datenbank löschen
=================

MySQL
-----

hsadmin -c mysqldb.delete xyz00_mydatabase 
			  
PostgesSQL
----------

hsadmin -c postgresqldb.delete yz00_mydatabase 

Datenbanken suchen
==================

MySQL
-----

hsadmin -c mysqldb.search

PostgesSQL
----------

hsadmin -c postgresqldb.search


Die Aufrufe "search" liefern folgende Informationen über die angelegten Datenbanken:

systemencoding	Zeichencodierung des Systems 

sqluserclass 	Klasse des hsadmin Datenbankusers

name		Name der Datenbank

instance	Instanz ( z.B. mysql oder pgsql)

id		Interne ID der Datenbank

encoding	Zeichencodierung der Datenbank

owner		Datenbankbenutzer

hivename	Der Hive auf dem die Datenbank eingerichtet ist

pac 		Webpaket zu dem die Datenbank gehört
