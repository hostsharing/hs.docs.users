================
Paket-Sub-Domain
================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time| 


Paket-Sub-Domain xyz00.hostsharing.net
--------------------------------------

Bei der Paketeinrichtung wird die Sub-Domain xyz00.hostsharing.net im Verzeichnis ``doms`` des :doc:`Paket-Admins <../benutzer/paket-admin>`
angelegt. Hierbei handelt es sich um eine nutzbare Sub-Domain, die alle Funktionen von Domains mit folgenden Einschränkungen unterstützt:

* Die Paket-Sub-Domain kann nicht gelöscht oder einem anderen Benutzer zugeordnet werden,
* Sub-Subdomains zu der Paket-Sub-Domain können nicht aufgeschaltet werden.

   .. warning::

        Das Zonefile der Paket-Subdomain sollte auf keinen Fall geändert werden, da dies zur Funktionsunfähigkeit des gesamten Pakets führen kann.

Verwendung
----------

Die Paket-Sub-Domain ist dafür geeignet, Web-Pakete oder Web-Anwendungen zu testen, ohne dass hierfür eine Domain registriert werden muss. 


