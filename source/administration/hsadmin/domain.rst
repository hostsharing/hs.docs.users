====================
HSAdmin-Modul domain
====================
Das HSAdmin-Modul ``domain`` verfügt über folgende Optionen:

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


+-----------------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                | default | Erläuterung                                                                                                                                                                                                                                                                                     |
+=======================+=========+=================================================================================================================================================================================================================================================================================================+
| greylisting           | on      | E-Mails werden verzögert durch den Mailserver angenommen, siehe :term:`Greylisting`. Ist die Option deaktivert, werden E-Mails ohne Verzögerung angenommen.                                                                                                                                     |
+-----------------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| multiviews            | on      | Der Webserver berücksichtigt Einstellungen im Browser beim Abruf einer Domain (z.B. eine bevorzugte Sprache).  Die Option kann mit einer :term:`.htaccess`-Datei für jedes Verzeichnis konfiguriert werden.                                                                                     |
+-----------------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| indexes               | on      | Der Webserver erzeugt für Verzeichnisse, die keine eigene Index-Datei enthalten, eine Liste mit den im Verzeichnis enthaltenen Dateien. Ist die Option deaktiviert, wird ein Fehler 303 ausgegeben. Die Option kann mit einer .htaccess-Datei für jedes Verzeichnis konfiguriert werden.        |
+-----------------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| htdocsfallback        | on      | Der Webserver leitet auf die Hauptdomain, wenn keine Sub-Domain angelegt ist. Ist die Option deaktivert, wird ein Fehler 404 ausgegeben: Seite nicht gefunden.                                                                                                                                  |
+-----------------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| includes              | on      | Der Webserver erkennt  :term:`SSI`-Komandos und -Dateien. Die Option kann mit einer .htaccess-Datei für jedes Verzeichnis konfiguriert werden.                                                                                                                                                  |
+-----------------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| backupmxforexternalmx | off     | Der Paket-Hive wird als Weiterleitung (transport) beim Mail-In-Server eingetragen. Ist die Option aktiv, ist der Hostsharing-Mail-In-Server Backup-MX. Der eigentliche Mailserver befindet sich außerhalb der Infrastruktur von Hostsharing (z.B. anderer Provider, DSL-Anschluß mit fester IP) |
+-----------------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

        Die Option ``backupmxforexternalmx`` erfordert Änderungen am :doc:`Zonefile<../zonefile/index>` einer Domain.
