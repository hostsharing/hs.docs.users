============
Domain-Admin
============

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M


:Authors: - Uwe Müller

:Date: |date|, |time|

Allgemein
---------

* wird durch den :doc:`Paket-Admin <paket-admin>` angelegt,
* hat eine reguläre :term:`Shell` (z.B. ``/bin/bash``),
* hat eine Verzeichnisstruktur unterhalb ``~/doms/``,
* ist ein E-Mail-Account.

Rolle
----- 

* Verwalter seiner Domain(s) in einem :doc:`Web-Paket</administration/webpaket/index>`.

Rechte
------

* E-Mail-Adressen für eine Domain anlegen,
* Sub-Domains anlegen,
* Zonen-Daten einer Domain bearbeiten,
* Dateien und Verzeichnisse anlegen oder ändern.


Konfiguration
-------------

E-Mail-Adressen anlegen:

* per Webfrontend, :doc:`siehe</administration/hsadmin/webfrontend>`
* mit ``hsscript``, :doc:`siehe</administration/hsadmin/index>`

Zonen-Daten einer Domain bearbeiten:

* mit einem beliebigen Texteditor

Sub-Domain(s) anlegen, Dateien und Verzeichnisse anlegen, ändern, löschen:

* Mit dem :term:`shell`-Kommando ``mkdir`` oder einem Dateimanager.
