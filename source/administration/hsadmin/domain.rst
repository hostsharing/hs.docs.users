===================
HSAdminmodul domain 
===================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          - Dominic Schlegel

:Date: |date|, |time|

Das HSAdminmodul ``domain`` verfügt über folgende Optionen:

+--------+------------------------+
| Option | Erläuterung            |
+========+========================+
| name   | Name einer Domain      |
+--------+------------------------+
| user   | Name des Domain-Admins |
+--------+------------------------+

Beispiel:


.. code-block:: console

    xyz00@hsadmin> domain.add ({set:{name:'hs-example.de',user:'xyz00'}})


+----------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option         | default | Erläuterung                                                                                                                                                                                                                                                                             |
+================+=========+=========================================================================================================================================================================================================================================================================================+
| greylisting    | aktiv   | E-Mails werden verzögert durch den Mailserver angenommen, siehe :term:`Greylisting`. Ist die Option deaktivert, werden E-Mails ohne Verzögerung angenommen.                                                                                                                             |
+----------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| multiviews     | aktiv   | Der Webserver berücksichtigt Einstellungen im Browser beim Abruf einer Domain (z.B. eine bevorzugte Sprache).  Die Option kann mittels .htaccess-Datei für jedes Verzeichnis konfiguriert werden.                                                                                       |
+----------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| indexes        | aktiv   | Der Webserver erzeugt für Verzeichnisse, die keine eigene Index-Datei enthalten, eine Liste mit den im Verzeichnis enthaltenen Dateien. Ist die Option deaktiviert, wird ein Fehler 303 ausgegeben Die Einstellung kann mittels .htaccess-Datei für jedes Verzeichnis angepasst werden. |
+----------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| htdocsfallback | aktiv   | Der Webserver leitet auf die Hauptdomain, wenn keine Sub-Domain angelegt ist. Ist die Option deaktivert, wird ein Fehler 404 ausgegeben: Seite nicht gefunden.                                                                                                                          |
+----------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| includes       | aktiv   | Der Webserver erkennt  :term:`SSI`-Komandos und -Dateien. Die Option kann mittels .htaccess-Datei für jedes Verzeichnis konfiguriert werden.                                                                                                                                            |
+----------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


