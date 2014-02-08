===========
Paket-Admin
===========

:Authors: - Uwe Müller
:Date:  2014-08-02

Allgemein
---------

Die Rolle des Paket-Admin wird initial beim Anlegen eines Webpaketes eingerichtet.  

* der Name ist :term:`xyz00` (http:// pakete),
* hat eine reguläre :term:`Shell` z.B. ``/bin/bash``,
* hat einen E-Mail-Account,
* hat ein eigenes Passwort.

Rolle
-----

* verwaltet ein Web-Paket, seine Benutzer, Dienste und Domains. 

Rechte
------

alle Rechte eines :doc:`Domain-Admin <domain-admin>` und folgende zusätzliche Rechte:

* Domains einem Domain-Admin des Pakets zuordnen,
* Domains des Paketes administrieren,
* Nutzer, Datenbanknutzer und Datenbanken einrichten, löschen und ändern,
* kann die Rechte eines Nutzers seines Paketes annehmen.

   .. warning:: 
        Eine Domain kann auf den Account des :term:`Paket-Admin` aufgeschaltet werden. Aus Sicherheitsgründen empfiehlt es sich Domains auf separate :doc:`Domain-Admins <domain-admin>` aufzuschalten.


Domainbestellungen siehe :doc:`Domainbestellungen <domain>`
