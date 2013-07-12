=======
Domains
=======

:Authors: - Uwe Müeller
:Date: 2013-03-01

Domainregistrierung/ -transfer zu Hostsharing
---------------------------------------------

1. Verzeichnisse für die Domain im Paket anlegen und die Domain in die DNS-Server von
   Hostsharing eintragen:
  
   hsadmin -c domain.add --set:user="xyz00-dom" --set:name="example.com"

2. Im Domainbestellsystem (http://externer link) gewünschte Aktion einleiten.

Domainkündigung, -löschung, -transfer (Abgehend)
------------------------------------------------

1. Im Domainbestellsystem (http://externer link) gewünschte Aktion einleiten.

2. Verzeichnisse für die Domain im Paket löschen und die Domain aus dem DNS-Server von
   Hostsharing austragen:

   hsadmin -c domain.delete "example.com"

warning::
    Hierbei werden sämtliche Daten im Domainverzeichnis gelöscht.

Domain einem Domain-User neu zuordnen 
--------------------------------------

Eine Domain kann einem anderen User zugeordnet werden, auch Paket übergreifend, sofern die
Pakete den gleichen Eigentümer haben. Aus Sicherheitsgründen ist diese Maßnahme nur dem Mitglied erlaubt.
Es wird das entsprechende Passwort abgefragt.

1. Löschen 

hsadmin -c domain.delete "example.com"

2. Anlegen 

hsadmin -u hsh00-xyz -c domain.add --set:name="example.com" --set:user="abc00-abc"


lokale Subdomain anlegen/löschen
---------------------------------

Lokale Subdomains können auf zwei Wegen angelegt werden:

Gleicher Domain-Admin/Paket
---------------------------
Ausführbar vom Domain-Admin und vom Paket-Admin.

Anlegen: 
Verzeichnis unterhalb ~/doms/example.com/subs/  anlegen.

Löschen: 
Verzeichnis unterhalb ~/doms/example.com/subs/ löschen.

Anderer Domain-Admin/Paket
--------------------------
Nur Ausführbar vom Paket-Admin.

Anlegen: Nur wenn beide Pakete den gleichen Eigentümer haben.
hsadmin -u hsh00-xyz -c domain.add --set:name="sub.example.com" --set:user="abc00-abc"

Löschen:
hsadmin -c domain.delete "sub.example.com"


extern registierte Domain/Subdomain aufschalten
--------------------------------------------------
Ausführbar vom Domain-Admin und vom Paket-Admin.

Domain anlegen:
hsadmin -c domain.add --set:user="xyz00-dom" --set:name="example.com"

Subdomain anlegen:
Verzeichnis unterhalb ~/doms/example.com/subs/ anlegen. 

Im Zonenfile (http:// Verwaltung Zonefiles) der extern registrierten Domain/Subdomain die DNS-Server der Hostsharing eG ein tragen:

dns1.hostsharing.net
dns2.hostsharing.net
dns3.hostsharing.net


Domains suchen, Statusinformationen
--------------------------------------

hsadmin -c domain.search

Der Aufruf sucht im Paket aufgeschaltete Domains und gibt zu der jeweiligen Domain Informationen
aus:

- name: Name der Domain
- id: Nummer des HSadmin Auftrages
- status: self 
- hivename: Der Hive, auf dem die Domain aufgeschaltet ist
- user: Der User zudem die Domain aufgeschaltet ist
- statuschanged: Datum der letzten Änderung
- filed: Datum der erfolgreichen Auftragsausführung
- since: Datum der Aufschaltung
- until: Datum der Kündigung/Löschung
- dnsmaster: Angabe der für die jeweilige Domain eingetragene DNS-Server


Verzeichnisse
-------------
Beim Aufschalten von Domains werden folgende Verzeichnisse angelegt:

example.com			Domain
	     -cgi		Ablage der Konfigurationsdateien für cgi
	     -cgi-ssl   	Ablage der Konfigurationsdateien für cgi-ssl    
	     -etc		Ablage Allgemeiner Konfigurationsdateien (z.B. .htpasswd)
	     -fastcgi		Ablage der Konfigurationsdateien für fastcgi
	     -fastcgi-ssl 	Ablage der Konfigurationsdateien für fastscgi-ssl
	     -htdocs		http: Ablage für die Daten der Domain
	     -htdocs-ssl	https: Ablage für die Daten der Domain 
	     -subs		http: Ablage für Subdomains
	     -subs-ssl   	https: Ablage für Subdomains
	     -var		Ablage für Logfiles

htaccess in htdocs/htdocs-ssl
-----------------------------
Beim Anlegen der Verzeichnisse für Domains wird in dem jeweiligen
htdocs/htdocs-ssl Verzeichnis eine .htaccess mit folgendem Inhalt angelegt:

Redirect permanent / http://www.example.com

bzw.:

Redirect permanent / https://www.example.com

Aufrufe der Domain example.com werden somit auf die Subdomain www.example.com weitergeleitet.            │~                                                                                                            
Die .htaccess kann bei Bedarf gelöscht werden.   
