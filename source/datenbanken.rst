===========
Datenbanken
===========

:Authors: - Uwe Müller
:Date: 2013-27-08


Allgemein
=========
Jeder Host hat seinen eigenen MySQL und PostgresSQL Datenbankserver. 


Zugriff MySQL
-------------
- über den Hostnamen localhost
- Port 3306

Zugriff PostgresSQL
--------------------
- über den Hostnamen localhost
- Port 5432



Webfrontend
-----------

MySQL https://phpmyadmin.hostsharing.net/current .
PostgesSQL https://phppgadmin.hostsharing.net/current .


Datenbankuser
-------------

Datenbankuser haben eine eigene Userverwaltung und  sind unabhängig von den Usern des Paketes
(http:// user, datenbankverwaltung).
Präfix für Datenbankuser ist xyz00_ .

Datenbanken
-----------
Präfix für Datenbanknamen ist xyz00_ .

Rechte vergeben
Allen Benutzern, außer dem Paketadmin, müssen wir noch Rechte geben, sonst können sie gar
nichts machen. Das erledigt man mit dem Befehl GRANT.
mysql>GRANT SELECT, INSERT, DELETE, UPDATE ON xyz00_meinedatenbank.* TO xyz00_otto;
Hinter der Datenbank verwenden wir .*, um alle Tabellen der Datenbank zu inkludieren.
Mit GRANT ALL kann man einem User auch alle Kommandorechte zuweisen.
Alle Aufgaben können wir jetzt in Zukunft vom User xyz00_otto erledigen lassen.

Rechte -> postgresql
