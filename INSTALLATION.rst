Installation
============

Dieses Projekt nutzt den `Sphinx Documentation Generator <http://sphinx.pocoo.org/>`_.

. Anlegen einer Python-Umgebung mit virtualenv
    ::
        $ virtualenv virtual

. Auschecken des Projekts
   ::
        $ git clone hsh04-repository@hsh04.hostsharing.net:hsdocs buildout

. Wechseln in das Verzeichnis
   ::
        $ cd buildout

. Installation des Sphinx Documentation Generator
   ::
        $ ../virtualenv/bin/python bootstrap.py
        $ ./bin/buildout

. Falls setuptools verlangt werden, sind diese zu installieren
  und der vorangegangene Schritt im Anschluss zu wiederholen
   ::
        $ ../virtualenv/bin/pip install 'distribute>=0.7'

. Erstellen der Ausgabe-Dateien
    ::
        $ bin/sphinxbuilder
