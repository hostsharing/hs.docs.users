=========
Allgemein
=========

:Author: - Uwe Müller

:Date:   2014-08-02         


Jeder :term:`Hive` hat einen eigenen MySQL- und PostgresSQL-Datenbankserver.

Zugriff
-------

Der Zugriff erfolgt über:

+--------------------+-----------+------+
| Datenbank          | Hostnamen | Port |
+====================+===========+======+
|     MySQL          | localhost | 3306 |
+--------------------+-----------+------+
|        PostgresSQL | localhost | 5432 |
+--------------------+-----------+------+


Verwaltung der Datenbanken und Datenbanknutzer
----------------------------------------------

Die Verwaltung von Datenbanken und Nutzern erfolgt entweder über ein Webfrontend


Webfrontend
-----------

Für die Verwaltung der angelegten Datenbanken stehen folgende Webfrontends für MySQL und PostgresSQL zur Verfügung: 

MySQL      `PHPmyAdmin <https://phpmyadmin.hostsharing.net/current>`_ .

PostgesSQL `PHPgAdmin <https://phppgadmin.hostsharing.net/current>`_ .



Rechte vergeben
---------------

Datenbankbenutzern müssen initial Rechte vergeben werden:


MySQL:.. code-block:: console   

     mysql>GRANT SELECT, INSERT, DELETE, UPDATE ON xyz00_meinedatenbank.* TO xyz00_abc;Alternativ können mit ``GRANT ALL`` einem Datenbankbenutzer alle Rechte zuweisen.
     

Rechte -> postgresql




