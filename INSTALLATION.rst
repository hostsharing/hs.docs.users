Installation
============

Dieses Projekt nutzt den `Sphinx Documentation Generator <http://sphinx.pocoo.org/>`_.

Anlegen einer Python-Umgebung mit virtualenv::

        $ virtualenv virtualenv

Anlegen von Verzeichnissen zur Dateiablage::

        $ mkdir -p resources/develop-eggs resources/downloads resources/eggs resources/extends

Auschecken des Projekts::

        $ git clone https://github.com/hostsharing/hsusers.git

Wechseln in das Verzeichnis::

        $ cd hsusers

Installation des Sphinx Documentation Generator::

        $ ../virtualenv/bin/python bootstrap.py
        $ ./bin/buildout

Erstellen der Ausgabe-Dateien::

        $ bin/sphinxbuilder
