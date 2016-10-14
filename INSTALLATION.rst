Installation
============

Dieses Projekt nutzt den `Sphinx Documentation Generator <http://sphinx.pocoo.org/>`_.


Vorbereitung
------------

Anlegen eines Basisordners für Hostsharing-Dokumentation::

        $ mkdir hs-docs

Wechseln in den Basisordner::

        $ cd hs-docs

Anlegen einer Python-Umgebung mit virtualenv::

        $ virtualenv virtualenv

Installation von Buildout::

        $ virtualenv/bin/pip install zc.buildout


Einrichten des Projekts
-----------------------

Ausschecken des Projekts::

        $ git clone https://dev.hostsharing.net/r/docs/hs.docs.users.git

Wechseln in den Projektordner::

        $ cd hs.docs.users.git

Installation des Sphinx Documentation Generator::

        $ ../virtualenv/bin/buildout


Generieren der Dokumentation
----------------------------

Erstellen der Ausgabe-Dateien::

        $ bin/sphinxbuilder
