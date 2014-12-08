===========
Logging
===========
          

Traffic
-------

Im :doc:`Web-Paket<../webpaket/index>` wird jeden Monat eine :doc:`Traffic-Log-Datei<traffic-log>` für den erzeugten Traffic erzeugt, die den Verbrauch eines jeden Tages pro Zeile enthält.
Der Traffic setzt sich aus HTTP-, FTP- und Mail-Traffic (POP3, IMAP) zusammen. Bei Überschreitung des gebuchten Traffics wird der :doc:`Paket-Admin<../benutzer/paket-admin>` automatisch per E-Mail informiert. 

Der Traffic für einzelne :doc:`Benutzer<../benutzer/index>` innerhalb eines Pakets kann nicht beschränkt werden.

HTTP-Log
--------
Das in kurzen Abständen aktualisierte Logfile ``web.log`` des Webservers steht im Paketverzeichnis ``/home/pacs/xyz00/var/`` dem Paket-Admin zur Verfügung. 
Aus dem Logfile werden nach Ablauf des Tages einzelne Logfiles für alle abgerufenen :doc:`Domain- und Sub-Domains<../domain/index>` generiert und unter  ``/home/pacs/xyz00/var/web-www.example.org-YYYYMMDD-HHMI.log.gz`` gespeichert. 
Diese Dateien werden 48 Tage archiviert und nach Ablauf dieser Frist automatisch gelöscht.  Das Error-Logfile ``web.err`` des Webservers steht unter ``/home/pacs/xyz00/var`` dem Paket-Admin zur Verfügung. 

Inhalt: 

.. toctree::       
        :maxdepth: 1                
         
        traffic-log        
        
