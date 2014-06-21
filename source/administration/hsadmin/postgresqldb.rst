=========================
HSAdminmodul postgresqldb 
=========================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          - Dominic Schlegel

:Date: |date|, |time|



Das HSAdminmodul postgresqldb verfügt über folgende Optionen:

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

    $ postgresqldb.add ({set:{name:'xyz00_abc',owner:'xyz00_abc',encoding:'latin1'}})

