======
Domain
======

:Authors: - Uwe Müller
:Date: 2013-26-08

Allgemein
---------

Folgende Aufgaben sind in der Verwaltung einer Domain sind möglich:
 
- Domainregistrierung
- Domaintransfer zu Hostsharing
- Extern registrierte Domains aufschalten
- Extern registrierte Subdomains aufschalten
- Domain neu zuordnen (Domain-Admin neu zuordnen oder Zuordnung zu einem Webpaket ändern)
- Subdomain neu zuordnen (Domain-Admin neu zuordnen oder Zuordnung zu einem Webpaket ändern)
- lokale Subdomains separat aufschalten
- Verwaltung der Zonefiles
- Transfer zu einem anderen Provider
- Domain löschen
 
Domainverwaltung
----------------

Die Domainverwaltung  ist in zwei Aufgabenbereiche geteilt:

- Domaineinrichtung und -konfiguration.
  Die Einrichtung und Konfiguration kann mit HSadmin auf der shell (http:// hsadmin-shell)
  oder Alternativ im Webfrontend (http:// hsadmin webfrontend) durchgeführt werden.

- Domain-Bestellsystem (http:// doku-domainbestellsystem)
  Zur Vergabe von Aufträgen (Registrierung, Kündigung, Transfer) an Domainregistrierungsstellen.

  Die Vergabe von Aufträgen an Domainregistrierungsstellen ist nur über das Webfrontend möglich.
  Der Nutzer ist für die Aktionen im Domainbestellsystem juristisch eigenverantwortlich.  Über das Webfrontend
  sind, abhängig von der jeweiligen Domainregistrierungsstelle, sämtliche  Aktionen möglich
  wie z.B. Registrierung, Update von Benutzerdaten, Änderungen von DNS-Servern, CHPROV (change provider, KK), Kündigung und Transit einer Domain.
  Die Anzahl der pro Tag möglichen Registrierungen ist auf 25 Domains beschränkt, um den Nuzter vor Mißbrauch zu schützen.

  
Paket-Subdomain xyz00.hostsharing.net
-------------------------------------

Bei der Paketeinrichtung wird die Subdomain xyz00.hostsharing.net im Ordner "doms" des Paketadmins
angelegt. Hierbei handelt es sich um eine nutzbare Subdomain, die alle Funktionen von Domains unterstützt
mit folgenden Einschränkungen:

- Die Paket-Subdomain kann nicht gelöscht oder einem anderen Benutzer zugeordnet werden.
- Subsubdomains zu der Paketdomain können nicht aufgeschaltet werden.

   .. note::
        Das Zonefile der Paket-Subdomain sollte auf keinen Fall geändert werden, da dies zur Funktionsunfähigkeit des gesamten Pakets führen kann.
   ::  

Die Paket-Subdomain ist dafür geeignet, Webpakete oder Web-Anwendungen zu testen ohne das hierfür eine Domain registriert werden muss. 
