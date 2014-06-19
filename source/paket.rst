==========
Web-Pakete 
==========

:Authors: - Uwe Müller
:Date: 2013-08-02



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









