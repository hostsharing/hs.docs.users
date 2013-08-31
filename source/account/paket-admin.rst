===========
Paket-Admin
===========

:Authors: - Uwe Müller
:Date:  2013-31-08

Allgemein
=========

   * ist Initial vorhanden.
   * der Name ist xyz00 (http:// pakete).
   * hat eine reguläre Shell (z.B. "/bin/bash")
   * weitere User beginnen mit dem Paket-Präfix ``xyz00-``, gefolgt von einer individuell zu vergebenen Zeichenfolge.
   * hat einen E-Mail-Account

Rolle
-----

   * verwaltet ein Web-Paket, seine Benutzer, Dienste und Domains. 

Rechte
------

alle Rechte eines :term:`Domain-Admin` und folgende zusätzliche Rechte:

   * Domains einem Benutzer (:term:`Domain-Admin`) des Pakets zuordnen,
   * Domains des Paketes administrieren,
   * User und Datenbanken einrichten, löschen und ändern,
   * kann die Rechte eines Users seines Paketes annehmen.

   .. warning:: 
        Eine Domain kann auf den Account eines Paketadmins aufgeschaltet werden. Aus Sicherheitsgründen empfiehlt es sich Domains auf separate User aufzuschalten.
::

Domainbestellungen siehe Domainbestellungen


