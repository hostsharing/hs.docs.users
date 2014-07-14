======
Backup
======

.. |date| date:: %d.%m.%Y 
.. |time| date:: %H:%M  
   
:Authors: - Michael Hierweck
          - Uwe Müller  
   
:Date: |date|, |time|


Hostsharing führt nächtliche Sicherungen der Daten durch. Die Sicherungen werden auf separaten Servern in einem separaten Rechenzentrum aufbewahrt. In der Regel können jeweils
mindestens die letzten 14 nächtlichen Datensicherungen wiederhergestellt werden. 


In der Datensicherung enthalten sind: 

* die Paket-Konfiguration.
* die Dateien im Paket selbst, insofern diese nicht vom Paket-Admin explizit ausgeschlossen wurden
* die zum Paket gehörigen Datenbanken 
* die zum Paket gehörigen eingegangenen E-Mails
* die Logfiles



In der Datensicherung sind nicht enthalten:

* ausgehende, aber noch ``nicht`` versandte E-Mails.
* eingehende, aber noch ``nicht`` im Postfach abgelegte E-Mails
* Dateien im Paket, die vom Paketinhaber per Konfiguration von der Datensicherung ausgeschlossen wurden
* Dateien in Verzeichnissen für temporäre Daten
          

Rücksicherung
-------------

Für die Rücksicherung der Datenbestände ist ein Rücksicherungsauftrag für die betroffene Sicherungsdatei in Auftrag zu geben.
Der Rücksicherungsauftrag erfolgt per E-Mail an service@hostsharing.net und beinhaltet folgende Angaben:

* das betreffende Webpaket,
* der Pfad des rückzusichernden Verzeichnisses, oder alternativ
* der Pfad und der Dateiname der rückzusichernden Datei,
* sowie das Datum des angeforderten Sicherungslaufs.

Datenbanken
-----------

Unmittelbar vor Beginn der Sicherung der Daten des Dateisystems werden MySQL- und PostgreSQL-Datenbanken in das Verzeichnis ``/home/pacs/xyz00/.bak/``  gesichert. Diese Sicherungen fließen in die nachfolgende Dateisystemsicherung ein.
Die Rücksicherung von Datenbanken erfolgt durch den Paket-Admin auf Basis der im Verzeichnis ``/home/pacs/xyz00/.bak/`` abgelegten Datenbanksicherungen.


.. note::

        Bemerkung
        Für ältere Datenbankbestände ist ein Rücksicherungsauftrag für die betroffene Sicherungsdatei in Auftrag zu geben.

