====================
Datenbank einrichten
====================
Beim Anlegen einer Datenbank ist die Reihenfolge entscheidend:

* Zunächst den Datenbanknutzer anlegen, den Verwalter der jeweiligen Datenbank
* Anlegen der Datenbank angelegt.

Anmeldung mit dem Paket-Admin xyz00 unter https://admin.hostsharing.net.

Wechsel auf dem Tab *MySQL User*:

.. image:: db-user.jpg

Nach Button *User anlegen* erscheint folgende Eingabemaske:

.. image:: db-user-anlegen.jpg

Die Felder werden wie folgt belegt:

MySQL User: xyz00

Benutzer-Postfix: dbuser (Zulässige Zeichen: 0 bis 9 und a bis z Buchstaben)

Passwort: PASSWORT

Mit dem Tab *MySQL DB* und dort dem Button *Datenbank anlegen* wird diese Eingabemaske sichtbar:

.. image:: db-anlegen.jpg

Die Felder hier:

MySQL Datenbank 

Paket: xyz00

Datenbank-Postfix: dbmysql (Zulässige Zeichen: 0 bis 9 und a bis z Buchstaben)

Zeichensatz: utf8

Verwalter: xyz00_dbuser


