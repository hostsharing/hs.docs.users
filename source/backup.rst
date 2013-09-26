======
Backup
======

:Authors: - Michael Hierweck
          - Uwe Müller
:Date: 2013-26-09

Hostsharing sichert gespeicherte Daten nächtlich vollständig in einem externen Rechenzentrum und bewahrt diese für 14 Tage auf.

E-Mails
=======

In die Postfächer zugestellte E-Mails werden von der Sicherung des Dateisystems erfasst.

Datenbanken
===========

Unmittelbar vor Beginn der Sicherung der Daten des Dateisystems werden MySQL- und PostgreSQL-Datenbanken in das Verzeichnis ``/home/pacs/xyz00/.bak/`` gesichert. Diese Sicherungen fließen
in die nachfolgende Dateisystemsicherung ein.

Rücksicherung
=============

Zur Rücksicherung der Dateidaten muss ein Rücksicherungsauftrag an service@hostsharing.net gesandt werden. 
Anzugeben sind:

* das betreffende Webpaket,
* der Pfad des rückzusichernden Verzeichnisses, oder alternativ 
* der Pfad und der Dateiname der rückzusichernden Datei,
* sowie das Datum des angeforderten Sicherungslaufs. 

Die Rücksicherung von Datenbanken erfolgt durch den Paket-Admin auf Basis der im Verzeichnis
``/home/pacs/xyz00/.bak/`` abgelegten Datenbanksicherungen.
Für ältere Datenbankbestände ist zuvor ein Rücksicherungsauftrag für die betroffene Sicherungsdatei in Auftrag zu geben.
