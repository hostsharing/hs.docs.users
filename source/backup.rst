======
Backup
======

:Authors: - Uwe Müeller
:Date: 2013-03-01

Hostsharing stellt ein Backup sämtlicher Daten der Webpakete incl. Datenbanken und User-Accounts zur Verfügung.
Die Sicherungen werden 14 Tage rückwirkend zur Verfügung gestellt und in einem externen Rechenzentrum gesichert.

Datenbanken
===========

Die Sicherungen der Datenbanken vom Vortag werden im Webpaket im Verzeichnis  /home/pacs/xyz00/.bak/ gesichert. 
Die Wiederherstellung erfolgt durch den Paketadmin durch die entsprechenden Datenbanktools.
Beispiele hierzu finden sich unter (http://Restore von Mysql Datenbanken) für Mysql und (http://Restore von Postgresql Datenbanken) für Potsgresql.

Sollen ältere Sicherungen wiederhergestellt werden, muss ein Rücksicherungsauftrag  unter Angabe der jeweiligen Datenbank an  service@hostsharing.net gesendet werden. 
Die Sicherung wird unter /home/restore/ bereitgestellt und kann vom Paketadmin in das Webpaket  zur weiteren Verarbeitung kopiert werden. 

Datendateien
============

Zur Rücksicherung der Dateidaten muss ein Rücksicherungsauftrag an service@hostsharing.net gesandt werden. 
Anzugeben sind:

- Betreffendes Webpaket
- Pfad des rückzusichernden Verzeichnisses, oder alternativ 
- Pfad und Dateiname der rückzusichernden Datei


 
