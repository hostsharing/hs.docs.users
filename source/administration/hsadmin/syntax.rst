======
Syntax
======

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          - Michael Hierweck

:Date: |date|, |time|

Die Funktionen von HSAdmin können über das Kommandozeilenprogramm
hsscript aufgerufen werden.

Aufrufparameter
---------------

+---------------+---------------------------------------+
| Parameter     | Erläuterung                           |
+===============+=======================================+
| -u <Benutzer> | Benutzer                              |
+---------------+---------------------------------------+
| -r <Benutzer> | unter anderer Nutzerkennung ausführen |
+---------------+---------------------------------------+
| -e <Befehl>   | Ausführen                             |
+---------------+---------------------------------------+
| -i            | interaktiver Modus                    |
+---------------+---------------------------------------+
| -v            | Version                               |
+---------------+---------------------------------------+

Befehlssyntax
-------------

module.function({where:{field:'value',...}, set:{field:'value',...}}) 

+-----------+-------------------------------------------------------------+
| Parameter | Erläuterung                                                 |
+===========+=============================================================+
| module    | Modul, dessen Funktion aufgerufen werden soll               |
+-----------+-------------------------------------------------------------+
| function  | Funktion, welche aufgerufen werden soll                     |
+-----------+-------------------------------------------------------------+
| where     | selektiert nach Wert eines oder mehrerer Felder             |
+-----------+-------------------------------------------------------------+
| set       | setzt oder aktualisiert den Wert eines oder mehrerer Felder |
+-----------+-------------------------------------------------------------+
