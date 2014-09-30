===========
Paket-Admin
===========

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|


Allgemein
---------

Die Rolle des Paket-Admins wird initial beim Anlegen eines :doc:`Web-Pakets</administration/webpaket/index>` eingerichtet und verwaltet das Web-Paket, seine :doc:`Benutzer<index>`, Dienste und :doc:`Domains</administration/domain/index>`. 

* der Name ist :term:`xyz00`,
* hat eine reguläre :term:`shell` z.B. ``/bin/bash``,
* ist ein E-Mail-Account,
* hat ein eigenes Passwort.

Rechte
------

Alle Rechte eines :doc:`Domain-Admins <domain-admin>` und folgende zusätzliche Rechte:

* Nutzer, :doc:`Datenbanknutzer<../datenbanken/datenbanken-nutzer>` und :doc:`Datenbanken<../datenbanken/index>` einrichten, löschen und ändern,
* Domains einem :doc:`Domain-Admin <domain-admin>` des :doc:`Web-Pakets<./../webpaket/index>` zuordnen,
* Domains des :doc:`Web-Pakets<./../webpaket/index>` administrieren,
* kann die Rechte eines Nutzers seines :doc:`Web-Pakets<./../webpaket/index>` annehmen.

   .. warning:: 
        Eine Domain kann auf den Account des :term:`Paket-Admins` aufgeschaltet werden. Aus Sicherheitsgründen empfiehlt es sich Domains auf separate :doc:`Domain-Admins <domain-admin>` aufzuschalten.


Administration
--------------

Nutzer einrichten, löschen und ändern; Domain(s) einem Domain-Admin zuordnen, Domain(s) administrieren: 

* per Webfrontend, :doc:`siehe</administration/HSAdmin/webfrontend>`
* mit ``hsscript``, :doc:`siehe</administration/HSAdmin/index>`

Rechte eines Web-Paket-Nutzers annehmen:

.. code-block:: console
    
    $ sudo -u xyz00-abc -i

Bei Web-Paket-Nutzer ohne :term:`shell`:

.. code-block:: console

    $ sudo -u xyz00-abc -s


