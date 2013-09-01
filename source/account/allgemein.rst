========= 
Allgemein
=========

:Authors: - Uwe Müller
:Date: 2013-31-08    

       
Übersicht
=========

Für unterschiedliche Aufgaben können unterschiedliche Rollen vergeben werden, die durch die Vergabe von Rechten auf Betriebssystemebene definiert werden. 

* :doc:`Mitglieds-Account <mitglied>` zur Verwaltung der Mitgliedschaft und *aller* gebuchten Webpakete
* :doc:`Paket-Admin <paket-admin>` zur Verwaltung eines Webpaketes
* :doc:`Domain-Admin <domain-admin>` zur Verwaltung einer oder mehrerer Domains *in* einem Webpaket
* :doc:`E-Mail-Account <userohneshell>` ohne die Zuweisung einer Shell  

Die Verwaltung von Domains (Registrierung, Transfer, DNS-Server etc.) erfolgt durch den

* :doc:`Domain-Account <domainaccount>`

im externen Verwaltungstool und ist unabhängig von den oben genannten Rollen. 

Die folgende Hierarchie gliedert sich in absteigender Reihenfolge.
[Bild]

Datenbank-User
==============

Die Datenbank-Systeme haben jeweils ihre eigene User-Verwaltung und sind unabhängig von der Vergabe von Rechten auf Betriebssystemebene.
(http:// Datenbankuser) 
Verwaltung der User (http:// userverwaltung http:// hsadmin shell http:// hsadmin webfrontend)

