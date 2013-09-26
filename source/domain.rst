======
Domain
======

:Authors: - Uwe Müller
:Date: 2013-26-09

Allgemein
---------

Folgende Aufgaben sind in der Verwaltung einer Domain sind möglich:
 
* Domainregistrierung,
* Domaintransfer zu Hostsharing,
* Extern registrierte Domains aufschalten,
* Extern registrierte Subdomains aufschalten,
* Domain neu zuordnen (:doc:`Domain-Admin <account/domain-admin>` neu zuordnen oder Zuordnung zu einem Web-Paket ändern),
* Subdomain neu zuordnen (Domain-Admin neu zuordnen oder Zuordnung zu einem Webpaket ändern),
* lokale Subdomains separat aufschalten,
* Verwaltung der Zonefiles,
* Verwaltung der Domaindaten (z.B. Handel, Owner, Kontaktdaten),
* Transfer zu einem anderen Provider,
* Domain löschen/kündigen.
 
Domainverwaltung
----------------

Die Domainverwaltung ist in zwei Aufgabenbereiche geteilt:

* **Domaineinrichtung und -konfiguration.**

  Die Einrichtung und Konfiguration ist mit unserem Verwaltungstool HSadmin auf der Konsole (http:// hsadmin-shell)
  oder alternativ im Webfrontend (http:// hsadmin webfrontend) möglich.

* **Vergabe von Aufträgen an Domainregistrierungsstellen**

  Zur Vergabe von Aufträgen an Domainregistrierungsstellen.

  Die Vergabe ist nur über das Webfrontend des Domainbestellsystems möglich. Abhängig von der jeweiligen Domainregistrierungsstelle sind eine vielzahl von Aktionen möglich (z.B. Registrierung, Update von Benutzerdaten, Änderungen von DNS-Servern, CHPROV (change provider, KK), Kündigung und Transit einer Domain). Die Anzahl der pro Tag möglichen Registrierungen ist beschränkt um Mißbrauch vorzubeugen. Nach Rücksprache kann kann das Limit erhöht werden.

   .. warning::

        Der Nutzer ist für sämtliche Aktivitäten im Domainbestellsystem juristisch eigenverantwortlich. 
        
Paket-Subdomain xyz00.hostsharing.net
-------------------------------------

Bei der Paketeinrichtung wird die Subdomain xyz00.hostsharing.net im Ordner "doms" des Paketadmins
angelegt. Hierbei handelt es sich um eine nutzbare Subdomain, die alle Funktionen von Domains unterstützt
mit folgenden Einschränkungen:

* Die Paket-Subdomain kann nicht gelöscht oder einem anderen Benutzer zugeordnet werden,
* Subsubdomains zu der Paketdomain können nicht aufgeschaltet werden.

   .. warning::

        Das Zonefile der Paket-Subdomain sollte auf keinen Fall geändert werden, da dies zur Funktionsunfähigkeit des gesamten Pakets führen kann.

Die Paket-Subdomain ist dafür geeignet, Webpakete oder Web-Anwendungen zu testen ohne das hierfür eine Domain registriert werden muss. 
