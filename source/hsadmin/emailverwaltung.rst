=================
E-Mail-Verwaltung
=================

:Authors: - Uwe Müeller
:Date: 2013-03-01

domain 		bezeichnet die Domain
localpart	bezeichnet den Part vor '@'
target		bezeichnet das Ziel, mehrere Ziele werden durch Komma separiert 

E-Mailadresse anlegen
---------------------
hsadmin --call:emailaddress.add --set:localpart='test' --set:domain='example.com' --set:target='xyz00-test'

Ziel einer E-Mailadresse ändern
-------------------------------
hsadmin --call:emailaddress.update --set:target='xyz00-test' test@example.com

E-Mailadresse löschen
---------------------
hsadmin --call:emailaddress.delete test@example.com

Alle E-Mailadressen einer Domain löschen
------------------------------------------
hsadmin --call:emailaddress.delete --where:domain=example.com

Alle E-Mail-Adressen einer Domain weiterleiten ( Catch-All)
------------------------------------------------------------
Eine Catch-All-Weiterleitung wird konfiguriert, in dem für Ziel und Quelle ein leerer
Local-Part angegeben wird.

hsadmin --call:emailaddress.add --set:localpart='' --set:domain='example.com' --set:target='@example.org'

E-Mailadressen suchen
---------------------
hsadmin --call:emailaddress.search

Der Aufruf sucht nach vorhandenen E-Mail Adressen und gibt folgende Informationen aus:

id		ID des HSadmin Auftrages
domain		Domain
target		Ziel der E-Mail Adresse
hivename        Name des Hives
localpart	Lokaler Teil der E-Mail Adresse
subdomain	Subdomain der E-Mail Adresse
emailaddress	E-Mail Adresse
fulldomain 	Vollständiger Domainname

Anlegen von Ordnern unterhalb von Maildir
-----------------------------------------

makemaildir -f Trash Maildir


