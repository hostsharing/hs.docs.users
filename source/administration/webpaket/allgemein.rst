=========
Allgemein
=========

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|

Ein Web-Paket ist technisch eine eigene UNIX-Nutzer-Gruppe. 
Ein Web-Paket beinhaltet eine definierte Leistung und kann durch Optionen jederzeit erweitert werden.

Die Bezeichnung besteht aus einem frei wählbaren, dreistelligen Präfix und einem zweistelligen Zähler (z.B xyz00). 
Ableitend ergibt sich aus der Vergabe des Paket-Präfix:

* der Name des :doc:`Paketadmins<../../account/paket-admin>` xyz00 
* das Paketverzeichnis \ ``/home/pacs/xyz00/``\
* die :doc:`Paket-Sub-Domain<../../domain/paket-subdomain>` xyz00.hostsharing.net

Ein Web-Paket kann enthalten:

* Nutzer mit unterschiedlichen Rollen (z.B. :doc:`E-Mail-<../../account/userohneshell>`, :doc:`Domain-<../../account/domain-admin>` oder :doc:`Datenbank-Nutzer<../../datenbanken/datenbanken-nutzer>`)
* :doc:`Datenbanken<../../datenbanken/index>`
* :doc:`Domains</domain/index>`

