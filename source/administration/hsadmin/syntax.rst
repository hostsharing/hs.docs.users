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

+--------------------+---------------------------------------------------------------------------------+
| Parameter          | Erläuterung                                                                     |
+====================+=================================================================================+
| --user <Benutzer>  | Benutzer, welcher zur Authentifizierung und Autorisierung verwendet werden soll |
| -u <Benutzer>      |                                                                                 |
+--------------------+---------------------------------------------------------------------------------+
| --runas <Benutzer> | Benutzer, mit dessen Rechten der Befehl ausgeführt werden soll                  |
| -r <Benutzer>      |                                                                                 |
+--------------------+---------------------------------------------------------------------------------+
| --expr <Befehl>    | Befehl, welcher ausgeführt werden soll                                          |
| -e <Befehl>        |                                                                                 |
+--------------------+---------------------------------------------------------------------------------+
| --file <Datei>     | Datei, aus welcher Befehler gelesen und ausgeführt werden sollen                |
| -f <Datei>         |                                                                                 |
+--------------------+---------------------------------------------------------------------------------+
| --interactive      | interaktiver Modus                                                              |
| -i                 |                                                                                 |
+--------------------+---------------------------------------------------------------------------------+

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
