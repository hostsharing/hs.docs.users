======
Backup
======

:Authors: - Michael Hierweck
          - Uwe Müller
:Date: 2014-07-02

Hostsharing sichert gespeicherte Daten nächtlich vollständig in einem externen Rechenzentrum und bewahrt diese für 14 Tage auf.

E-Mails
=======

In die Postfächer zugestellte E-Mails werden von der Sicherung des Dateisystems erfasst.

Rücksicherung
=============

Für die Rücksicherung der Datenbestände ist ein Rücksicherungsauftrag für die betroffene Sicherungsdatei in Auftrag zu geben.
Der Rücksicherungsauftrag erfolgt per E-Mail an service@hostsharing.net und beinhaltet folgende Angaben: 

* das betreffende Webpaket,
* der Pfad des rückzusichernden Verzeichnisses, oder alternativ 
* der Pfad und der Dateiname der rückzusichernden Datei,
* sowie das Datum des angeforderten Sicherungslaufs.


Datenbanken
===========

Unmittelbar vor Beginn der Sicherung der Daten des Dateisystems werden MySQL- und PostgreSQL-Datenbanken in das Verzeichnis ``/home/pacs/xyz00/.bak/`` gesichert. Diese Sicherungen fließen
in die nachfolgende Dateisystemsicherung ein.

Die Rücksicherung von Datenbanken erfolgt durch den  :doc:`Paket-Admin<account/paket-admin>` auf Basis der im Verzeichnis ``/home/pacs/xyz00/.bak/`` abgelegten Datenbanksicherungen.

Für ältere Datenbankbestände ist ein Rücksicherungsauftrag für die betroffene Sicherungsdatei in Auftrag zu geben.

