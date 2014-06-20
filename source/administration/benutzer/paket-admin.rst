===========
Paket-Admin
===========

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|


Allgemein
---------

Die Rolle des Paket-Admin wird initial beim Anlegen eines :doc:`Web-Paketes</administration/webpaket/index>` eingerichtet.  

* der Name ist :term:`xyz00`,
* hat eine reguläre :term:`Shell` z.B. ``/bin/bash``,
* ist ein E-Mail-Account,
* hat ein eigenes Passwort.

Rolle
-----

* verwaltet ein :doc:`Web-Paket<../../webpaket/index>`, seine :doc:`Benutzer<index>`, Dienste und :doc:`Domains</administration/domain/index>`. 

Rechte
------

alle Rechte eines :doc:`Domain-Admin <domain-admin>` und folgende zusätzliche Rechte:

* Domains einem :doc:`Domain-Admin <domain-admin>` des :doc:`Web-Paketes<./../webpaket/index>` zuordnen,
* Domains des :doc:`Web-Paketes<./../webpaket/index>` administrieren,
* Nutzer, :doc:`Datenbanknutzer<../../datenbanken/datenbanken-nutzer>` und :doc:`Datenbanken<../../datenbanken/index>` einrichten, löschen und ändern,
* kann die Rechte eines Nutzers seines :doc:`Web-Paketes<./../webpaket/index>` annehmen.

   .. warning:: 
        Eine Domain kann auf den Account des :term:`Paket-Admin` aufgeschaltet werden. Aus Sicherheitsgründen empfiehlt es sich Domains auf separate :doc:`Domain-Admins <domain-admin>` aufzuschalten.



