========
Benutzer
========

:Authors: - Uwe Müller
:Date: 2013-08-26




Benutzer
========

Für unterschiedliche Aufgaben in einem Paket können unterschiedliche Rollen vergeben werden, die durch die Vergabe von Rechten auf Betriebssystemebene definiert werden.
Datenbank-Systeme haben eine eigene User-Verwaltung und sind unabhängig von der Betriebssystemebene.  

Die folgende Hierarchie gliedert sich in absteigender Reihenfolge.

Mitglied 
========

- Initial vorhanden
- der Name ist xyz 
- hat keine Shell
- erlischt mit dem Ende der Mitgliedschaft
- eigenes Passwort
- technisch unabhängig von anderen Benutzern

Rolle
=====

- mit HSAdmin alle Pakete verwalten die dem Mitglied zugeordnet sind
- kann die Rechte eines Paket-Admins annehmen
- Rechnungen herunterladen
- technisch unabhängig von anderen Accounts

Domainbestellsystem
===================

- Initial vorhanden
- der Name ist hs-xyz
- eigenes Passwort

Rolle
-----

- Verwaltung von Domains im externen Verwaltungstool.

Paket-Admin
===========

- ist Initial vorhanden.
- der Name ist xyz00 (http:// pakete).
- hat eine reguläre Shell (z.B. "/bin/bash")
- weitere User beginnen mit dem Paket-Präfix xyz00-, gefolgt von einer individuell zu vergebenen
  Zeichenfolge.
- hat einen E-Mail Account

Rolle
-----

- verwaltet ein Web-Paket, seine User, Dienste und Domains. 

Rechte
------

alle Rechte eines Domain-Admin und folgende zusätzliche Rechte:

- Domains einem User (Domainadmin) des Pakets zuordnen,
- Domains des Paketes administrieren,
- User und Datenbanken einrichten, löschen und ändern,
- kann die Rechte eines Users seines Paketes annehmen.

   .. warning:: 
        Eine Domain kann auf den Account eines Paketadmins aufgeschaltet werden. Aus Sicherheitsgründen empfiehlt es sich Domains auf separate User aufzuschalten.
::

Domainbestellungen siehe Domainbestellungen

Domain-Admin
============

- wird durch den Paket-Admin angelegt
- hat eine reguläre Shell (z.B. "/bin/bash")
- hat eine Verzeichnisstruktur unterhalb ~/doms/
- hat einen E-Mail Account

Rolle
----- 

Verwalter seiner Domain(s):

- Sub-Domains aufschalten
- Dateien und Verzeichnisse
  anlegen oder ändern

Rechte
------

- E-Mail-Adressen für eine Domain einrichten
- Sub-Domains anlegen
- Zonen-Daten einer Domain bearbeiten.

User ohne Shell
===============

- wird durch den Paket-Admin angelegt,
- hat keine Shell (das Programm "passwd" wird an Stelle einer Shell gestartet).

Rolle
-----

- als E-Mail-Account.

Rechte
------

- nur Passwortänderung möglich.

Datenbank-User
==============

Die Datenbank-Systeme haben jeweils ihre eigene User-Verwaltung. (http:// Datenbankuser)

Verwaltung der User (http:// userverwaltung http:// hsadmin shell http:// hsadmin webfrontend)
