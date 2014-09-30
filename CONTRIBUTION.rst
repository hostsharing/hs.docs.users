Beitragen
=========

Gerne können Sie unser Repository clonen und anschließend Änderungen vornehmen.
Pull-Requests übernehmen wir dann gerne wieder in das Hostsharing-Repository
sofern sie sich in die allgemeine technische Dokumentation von Hostsharing
einfügen und die unten folgenden Hinweise beachtet werden.

Installationsanleitungen, Tipps und Tricks etc. gehören *nicht* in diese Dokumentation. Hierfür bieten wir zur Zeit das Wiki der Mitglieder `<https://wiki.hostshaing.net>`_ an.

Allgemeine Hinweise
-------------------

* Möglichst kurze und eindeutige Sätze schreiben
* Aussagen müssen klar und verständlich sein, Umschreibungen verwirren
* Auf umgangssprachliche Ausdrücke wird verzichtet
* Sind deutsche Fachbegriffe gebräuchlich, werden diese verwendet
* Die Dokumentation soll für jeden verständlich sein
 

Anrede
------

Die direkte Anrede ist zu vermeiden, auch ``man`` soll nicht verwendet werden. 

Bilder
------
Die Dateigröße von Bildern sollte klein gehalten und die Bilder selbst nicht überdimensioniert sein. 

Syntax-Regeln
-------------

Die einheitliche Verwendung der Syntax-Regeln ist sehr wichtig für die Lesbarkeit der Dokumentation.

Hervorhebungen
--------------

Hervorhebungen zeigen auf, was wichtig ist. Hervorgehobene Elemente sind im Textfluss eingebettet. 
Unterstreichungen sollten nicht verwendet werden.  
Auf eine inflationäre Verwendung von Aufrufezeichen wird verzichtet.


Benennungsregeln
----------------

Seitentitel müssen kurz und sprechend sein.

Glossar
-------

Zur Erläuterung von Begriffen oder Abkürzungen soll das Glossar verwendet werden.


Dokumentenformat
================

Hier einige Regeln, die bei der Dokumentation beachtet werden sollten:

Seitenstruktur
--------------

Die Hauptüberschrift, die auch im Inhaltsverzeichnis erscheint, sollte so
geschrieben werden::

        ========================
        Installation von hsusers
        ========================

danach folgen Angaben zu den Autoren, Datums- und Zeitangaben::

   .. |date| date:: %d.%m.%Y
   .. |time| date:: %H:%M

   :Authors: - Max Mustermann 
             - Michaela Mustermann

   :Date: |date|, |time|



Kapitelstruktur
===============

Jedes Kapitel oder jeder Ordner muss eine ``index.rst``-Datei mit folgenden
Abschnitten enthalten:

* Überschrift des Abschnitts: Dieser wird im Inhaltsverzeichnis angezeigt.
* Sphinx ``toctree``-Anweisung wobei jede Datei in diesem Ordner verlinkt sein sollte.

Hervorhebungen
--------------

Mit `Pygments <http://pygments.org/>`_ lassen sich Hervorhebungen in Sphinx angeben.

Auch verschiedenartige Hervorhebungen lassen sich realisieren:

- für Python-Skripte::

.. code-block:: python
        
        if "foo" == "bar":
            pass

- Für XML::

    .. code-block:: xml
    
        <?xml version="1.0" encoding="UTF-8"?>
        <rules
            xmlns="http://namespaces.plone.org/xdv"
            xmlns:css="http://namespaces.plone.org/xdv+css">
        ...
        </rules>


- Für Angaben in der Konsole::
        
    .. code-block:: console
    
        $ sh myscript.sh
        

- Soll ein gesamtes Dokument hervorgehoben werden, kann dies z.B. so
  geschehen::

    ..highlight\:\: console
        
        $ ./bin/instance start
                         



RestructuredText-Markierungen
-----------------------------

- Kursiv::

    *Italic*

- Halbfett::

    **Halbfett**

- Hervorhebung von Code innerhalb einer Zeile::

    ``code_hervorhebung``

- Externe Links::

    `Externer Link <http://www.hostsharing.net>`_

- Interner Link::

    :doc:`Interner Link <impressum>`

- Aufzählungsliste::

    * Erster Punkt
    * Zweiter Punkt


Bilder
------

Einbindung von Bilder::

        ..image:: bild.png

Diagramme
---------

Diagramme werden mit `graphviz http://www.graphviz.org`_ erstellt::

        .. graphviz:: filemap-mit-ssl.dot

Glossar
-------

Begriffe oder Abkürzungen im Text, die eine Erläuterung erhalten, werden so angegeben::

        :term:`Quota`
    
Informationsboxen
-----------------

Informationsboxen lassen sich in Sphinx mit den Anweisungen ``warning`` und
``note`` angeben.

Warnungen
`````````

.. warning:: 
 
    Diese Box enthält eine Warnung!

Warnungen wie diese können so angegeben werden::

    .. warning:: 
 
        Diese Box enthält eine Warnung!

Hinweise
````````

.. note::

    TODO: Diese Box enthält einen Hinweis!

::

    .. note::

        TODO: Diese Box enthält einen Hinweis! 

Tipps
`````

.. tip::
    Diese Box enthält einen Tipp!

::

    .. tip::
        Diese Box enthält einen Tipp!



