=====================
HSAdmin-Modul mysqldb
=====================


Das HSAdmin-Modul mysqldb verfügt über folgende Optionen:

+---------------+------------------------------------------------+
| Option        | Erläuterung                                    |
+===============+================================================+
| name          | Datenbankname (z.B. xyz00_abc)                 |
+---------------+------------------------------------------------+
| owner         | Datenbanknutzer (z.B. xyz00_owner)             |
+---------------+------------------------------------------------+
| encoding      | Zeichensatz der Datenbank (Standard ist UTF-8) |
+---------------+------------------------------------------------+

Beispiel:

.. code-block:: console

    xyz00@hsadmin> mysqldb.add ({set:{name:'xyz00_abc',owner:'xyz00_owner',encoding:'latin1'}})
