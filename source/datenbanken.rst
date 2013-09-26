===========
Datenbanken
===========

:Authors: - Uwe Müller
:Date: 2013-26-09


Allgemein
=========
Jeder Host hat seinen eigenen MySQL und PostgresSQL Datenbankserver. 

Zugriff MySQL
-------------
* über den Hostnamen localhost
* Port 3306

Zugriff PostgresSQL
--------------------
* über den Hostnamen localhost
* Port 5432

Webfrontend
-----------
Für die Verwaltung der angelegten Datenbanken stehen folgende Webfrontends für MySQL und PostgresSQL zur Verfügung: 

MySQL      `PHPmyAdmin <https://phpmyadmin.hostsharing.net/current>`_ .
PostgesSQL `PHPgAdmin <https://phppgadmin.hostsharing.net/current>`_ .

Datenbankbenutzer
-----------------

Datenbankbenutzer haben eine eigene Benutzerverwaltung und sind unabhängig von den Nutzern des Web-Paketes.

* Präfix für Datenbankbenutzer ist ``xyz00_`` .

Datenbanken
-----------

* Präfix für Datenbanknamen ist ``xyz00_`` .

Rechte vergeben
---------------

Datenbankbenutzern müssen initial Rechte vergeben werden:

MySQL:

.. code-block:: console
        mysql>GRANT SELECT, INSERT, DELETE, UPDATE ON xyz00_meinedatenbank.* TO xyz00_abc;

Alternativ können mit ``GRANT ALL`` einem Datenbankbenutzer alle Rechte zuweisen.


Rechte -> postgresql
