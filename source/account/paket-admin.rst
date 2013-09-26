===========
Paket-Admin
===========

:Authors: - Uwe Müller
:Date:  2013-26-09

Übersicht
=========

Die Rolle des Paket-Admin wird initial beim Anlegen eines Webpaketes eingerichtet.  

* der Name ist xyz00 (http:// pakete),
* hat eine reguläre Shell z.B. ``/bin/bash``,
* hat einen E-Mail-Account,
* hat ein eigenes Passwort.

Rolle
-----

* verwaltet ein Web-Paket, seine Benutzer, Dienste und Domains. 

Rechte
------

alle Rechte eines :doc:`Domain-Admin <domain-admin>` und folgende zusätzliche Rechte:

* Domains einem Benutzer Domain-Admin des Pakets zuordnen,
* Domains des Paketes administrieren,
* User und Datenbanken einrichten, löschen und ändern,
* kann die Rechte eines Users seines Paketes annehmen.

   .. warning:: 
        Eine Domain kann auf den Account eines Paketadmins aufgeschaltet werden. Aus Sicherheitsgründen empfiehlt es sich Domains auf separate User aufzuschalten.
::

Domainbestellungen siehe :doc:`Domainbestellungen <domain>`
