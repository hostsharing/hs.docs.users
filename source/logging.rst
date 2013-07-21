===========
Traffic-Log
===========

:Authors: - Uwe Müeller
:Date: 2013-03-01

Der im Webpaket erzeugte Traffic wird dem Paketadmin unter /home/pacs/xyz00/var/traffic-iptables-YYYY-MM.log zugänglich gemacht.
Für jeden Monat wird eine Logdatei erzeugt die den Verbrauch eines jeden Tages des Webpaketes pro Zeile enthält.

Das Logfile hat folgenden Aufbau:

# Datum   ;Paket ; Monatslimit; Tageslimit; Trafficsumme ; IP-Adresse 1 ; Traffic 1 ; IP-Adresse 2 ; Traffic 2
2012-08-01;xyz00 ;  10240     ; 341.333   ; 89.367       ; 83.223.79.125; 89.367    ;              ; 0.000

Bedeutung der einzelnen Spalten: 
  
- Datum:        Datum der Messung 
- Paket:        Name des Webpaketes
- Monatslimit:  Gebuchter Gesamttraffic pro Monat in Megabyte
- Tageslimit:   Tägliches Traffic-Kontingent bei gleichmäßigem Verbrauch in Megabyte 
- Trafficsumme: Gesamtsumme des angefallenen Traffic am angegebenen Tag in Megabyte
- IP-Adresse 1: Primäre IP-Adresse des Webpaketes 
- Traffic 1:    Über die primäre IP-Adresse angefallener Traffic in Megabyte
- IP-Adresse 2: Sekundäre IP-Adresse des Pakets 
- Traffic 2:    Über die sekundäre IP-Adresse angefallener Traffic in Megabyte


HTTP-Log 
========

Das in kurzen Abständen aktualisierte Logfile web.log des Webservers steht im Paketverzeichnis /home/pacs/xyz00/var/ dem Paketadmin zur Verfügung.

Aus dem Logfile web.log werden nach Ablauf des Tages einzelne Logfiles für alle abgerufenen Domain- und Subdomains generiert und unter  /home/pacs/xyz00/var/web-www.example.org-YYYYMMDD-HHMI.log.gz
gespeichert. Diese Dateien werden 48 Tage archiviert und nach Ablauf der Frist automatisch gelöscht.  

Das Error-Logfile web.err des Webservers steht unter /home/pacs/xyz00/var/ dem Paketadmin zur Verfügung. 

