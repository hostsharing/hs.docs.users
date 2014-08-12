=======================
Installation von hsdocs
=======================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M


:Authors: - Michael Hierweck
          - Veit Schiele
          - Uwe Müller

:Date: |date|, |time|

. Anlegen einer Pythozon-Umgebung mit virtualenv
   ::
    $ virtualenv virtual

. Auschecken des Projekts
   ::
    $ git clone  hsh04-repository@hsh04.hostsharing.net:hsdocs buildout

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

.. _
   `Sphinx Documentation Generator`: http://sphinx.pocoo.org/

Falls Sie die Sourcen für Ihre Zwecke anpassen möchten, beachten Sie bitte,
dass Sphinx ein `erweitertes Markup`_ für `ReStructuredText`_ bereitstellt.

.. _`erweitertes Markup
   `: http://sphinx.pocoo.org/markup/ 
.. _`ReStructuredText`: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

