===========
Logging
===========

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|  

          

Traffic
-------

Im :doc:`Web-Paket<../webpaket/index>` wird jeden Monat eine :doc:`Traffic-Log-Datei<traffic-log>` für den erzeugten Traffic erzeugt, die den Verbrauch eines jeden Tages pro Zeile enthält.
Der Traffic setzt sich aus HTTP-, FTP- und Mail-Traffic (POP3, IMAP) zusammen. Bei Überschreitung des gebuchten Traffics wird der :doc:`Paket-Admin<../benutzer/paket-admin>` automatisch per E-Mail informiert. 

Der Traffic für einzelne :doc:`Nutzer<../benutzer/index>` innerhalb eines Pakets kann nicht beschränkt werden.

        

HTTP-Log
--------
Das in kurzen Abständen aktualisierte Logfile ``web.log`` des Webservers steht im Paketverzeichnis ``/home/pacs/xyz00/var/`` dem :doc:`Paket-Admin<../benutzer/paket-admin>` zur Verfügung. 
Aus dem Logfile werden nach Ablauf des Tages einzelne Logfiles für alle abgerufenen :doc:`Domain- und Subdomains<../domain/index>` generiert und unter  ``/home/pacs/xyz00/var/web-www.example.org-YYYYMMDD-HHMI.log.gz`` gespeichert. 
Diese Dateien werden 48 Tage archiviert und nach Ablauf dieser Frist automatisch gelöscht.  Das Error-Logfile ``web.err`` des Webservers steht unter ``/home/pacs/xyz00/var`` dem :doc:`Paket-Admin<../benutzer/paket-admin>` zur Verfügung. 

Inhalt: 

.. toctree::       
        :maxdepth: 1                
         
        traffic-log        
        
