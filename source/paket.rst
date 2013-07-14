==========
Web-Pakete 
==========

:Authors: - Uwe Müeller
:Date: 2013-03-01

Allgemein
=========

Ein Web-Paket stellt eine eigene UNIX-User-Gruppe dar, beinhaltet eine definierte Leistung
(http:// Leistungsbeschreibungen)  und kann durch Optionen jederzeit aufgewertet werden. 
Jedes Web-Paket hat eine Bezeichnung aus einem frei wählbaren Präfix und einem zweistelligen Zähler (z.B xyz00). 
Ableitend ergibt sich aus der Vergabe des Paket-Präfix:

- der Name des Paketadmins xyz00 (http://userverwaltung)
- das Paketverzeichnis /home/pacs/xyz00/
- die Paketdomain xyz00.hostsharing.net


Paketdomain xyz00.hostsharing.net
---------------------------------

Die Paketdomain kann für Zugriffe (z.B. HTTP, HTTPS, FTP, SCP oder ssh) genutzt werden, ohne das eine
generische Domain (z.B. example.com) bestellt werden muss. Die Paketdomain ist dem
Paket-Admin fest zugeordnet.

Speicherbelegung
----------------

Zum belegten Paket-Speicher zählen neben den Verzeichnissen und die darin abgelegten
Daten ebenfalls die angelegten Datenbanken, Dateien unter /home/restore und temporäre
Daten im Verzeichnis /tmp.

Traffic
-------

Der Traffic setzt sich aus HTTP-, FTP- und Mail-Traffic (POP3, IMAP) zusammen.
Bei Überschreitung des gebuchten Traffics wird der Paketadmin automatisch per E-Mail
informiert (http:// leistungsbeschreibugen traffic/fair use).

Der Traffic für einzelne Nutzer innerhalb eines Paketes kann nicht beschrängt werden.

Logfiles werden unter ~/var/traffic-iptables-yyyy-mm.log des Paketadmins abgelegt.
Eine technische Beschreibung der Logfiles findet sich hier (http://hs-kerndoku logging)


Weblog?
-------

Verzeichnisse
-------------

[Bild-skizze] 

drwx--x--x 16 xyz00 xyz00 4096 Oct 25 09:24 .
drwx------  2 xyz00 xyz00   61 Oct 26 01:37 .bak
drwx--x--x  2 xyz00 xyz00   21 Oct  7 14:01 cgi
drwx--x--x  2 xyz00 xyz00   21 Oct  7 14:01 cgi-ssl
dr-xr-x--T  2 xyz00 xyz00    6 Oct  7 13:42 doms
drwx--S---  2 xyz00 xyz00    6 Oct  7 13:42 etc
drwx--x--x  2 xyz00 xyz00   20 Oct  7 14:01 fastcgi
drwx--x--x  2 xyz00 xyz00   20 Oct  7 14:01 fastcgi-ssl
drwxr-sr-x  4 xyz00 xyz00   27 Oct  7 15:10 users
drwxr-s---  2 xyz00 xyz00 8192 Nov 26 01:33 var
drwx------ 9  xyz00 xyz00 4096 12. Sep 13:07 Maildir


.bak
----

Verzeichnis zur Ablage komprimierter Backups der Datenbanken und Cronjobs. 

cgi/ cgi-ssl
------------

Verzeichnis zur Ablage externer Software zur Generierung dynamischer Webseiten in einem Webserver.
Im Verzechnis SSL sind die Dateien zu hinterlegen, wenn die Generierung der Daten
verschlüsselt erfolgen soll.


fastcgi/ fastcgi-ssl
--------------------
Verzeichnis zur Ablage externer Software zur Generierung dynamischer Webseiten in einem Webserver.
Im Verzechnis SSL sind die Dateien zu hinterlegen, wenn die Generierung der Daten
verschlüsselt erfolgen soll.

doms
------

Verzeichnis zur Ablage der Domain und Unterverzeichnisse für die Domains des Paketadmins.

etc
----

Verzeichnis für Paketeigene Konfigurationsdateien (z.B. Event-Handler, config.ini).

users
------

Verzeichnis der angelegten Nutzer im Paket.

var
----

Verzeichnis zur Ablage von Logfiles (Web-Logs, Traffic-Logs, Logfiles aller Domains des Paketadmins)

Maildir
-------

Mailordner des Paketadmins


(http:// Domains)
(http:// Pakettraffic)
und weitere


Paket-Rechte Schleuse
xyz00-abc@h03:~$ ls -ld . doms/ doms/example.com/ doms/example.com/*
drwxr-xr-x  5 xyz00-abc xyz00  76 Oct 13  2010 .
dr-xr-x--T  5 httpd     xyz00  47 Feb 22  2011 doms/
drwxr-x--- 12 xyz00-abc httpd 138 Feb 22  2011 doms/example.com/
drwxr-xr-x  2 xyz00-abc xyz00  21 Feb 22  2011 doms/example.com/cgi
drwxr-xr-x  2 xyz00-abc xyz00  21 Feb 22  2011 doms/example.com/cgi-ssl
drwxr-xr-x  2 xyz00-abc xyz00   6 Feb 22  2011 doms/example.com/etc
drwxr-xr-x  2 xyz00-abc xyz00  20 Feb 22  2011 doms/example.com/fastcgi
drwxr-xr-x  2 xyz00-abc xyz00  20 Feb 22  2011 doms/example.com/fastcgi-ssl
drwxr-xr-x  2 xyz00-abc xyz00  22 Feb 22  2011 doms/example.com/htdocs
drwxr-xr-x  2 xyz00-abc xyz00  22 Feb 22  2011 doms/example.com/htdocs-ssl
drwxr-xr-x  3 xyz00-abc xyz00  16 Feb 22  2011 doms/example.com/subs
drwxr-xr-x  3 xyz00-abc xyz00  16 Feb 22  2011 doms/example.com/subs/www
drwxr-xr-x  3 xyz00-abc xyz00  16 Feb 22  2011 doms/example.com/subs-ssl
drwxr-xr-x  3 xyz00-abc xyz00  16 Feb 22  2011 doms/example.com/subs-ssl/www
drwxr-xr-x  2 xyz00-abc xyz00   6 Feb 22  2011 doms/example.com/var
