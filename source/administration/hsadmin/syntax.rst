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

+-----------+---------------------------------------+
| Parameter | Erläuterung                           |
+===========+=======================================+
| where     | selektiert nach einem Feld            |
+-----------+---------------------------------------+
| set       | setzt einen Wert                      |
+-----------+---------------------------------------+

