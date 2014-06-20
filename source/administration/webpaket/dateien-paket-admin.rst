=========================
Initial angelegte Dateien
=========================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:date: |date|, |time|

Weblog
------

Im Verzeichnis ``var`` werden folgende Dateien initial angelegt:


+-----------------+--------+--------+-----------+-------------------------------------------------------+
| Rechte Schleuse | Nutzer | Gruppe | Datei     | Erläuterung                                           |
+=================+========+========+===========+=======================================================+
| -rw-------     | xyz00  | xyz00  |   web.log |  Apache Weblog aller im Paket aufgeschaltenen Domains |
+-----------------+--------+--------+-----------+-------------------------------------------------------+
| -rw-------      | xyz00  | xyz00  | web.err   | Fehlermeldungen bei Zugriffen auf Webseiten           |
+-----------------+--------+--------+-----------+-------------------------------------------------------+
 
Weitere Informationen zum Logging unter http: logging

HSAdmin
-------

Im Homeverzeichnis werden folgende Dateien initial angelegt:

+-----------------+--------+--------+----------------+----------------------------------------------------------------------------------------------------+
| Rechte Schleuse | Nutzer | Gruppe | Datei          | Erläuterung                                                                                        |
+=================+========+========+================+====================================================================================================+
| -rw-------     | xyz00  | xyz00  |  .hsadmin.conf |  Konfigurationsdatei für HSAdmin, initial leer. Beinhaltet den Namen des Paket-Admin und Passwort. |
+-----------------+--------+--------+----------------+----------------------------------------------------------------------------------------------------+
| -rw-------     | xyz00  | xyz00  | .hsadmin.tgt   | HSAdmin, speichert den Zugriff auf HSAdmin.                                                        |
+-----------------+--------+--------+----------------+----------------------------------------------------------------------------------------------------+


