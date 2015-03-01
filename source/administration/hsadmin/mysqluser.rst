=======================
HSAdmin-Modul mysqluser
=======================

Das HSAdmin-Modul ``mysqluser`` verfügt über folgende Optionen:



+---------------+------------------------------------------------+
| Option        | Erläuterung                                    |
+===============+================================================+
| name          | Name des Datenbanknutzers (z.B. xyz00_abc)     |
+---------------+------------------------------------------------+
| password      | Passwort                                       |
+---------------+------------------------------------------------+

Beispiel:

.. code-block:: console

    xyz00@hsadmin> mysqluser.add  ({set:{name:'xyz00_owner',password:'!1?2-3aBc'}})
 
