===========================
HSAdminmodul postgresqluser 
===========================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          - Dominic Schlegel

:Date: |date|, |time|


Das HSAdmin-Modul ``postgresqluser`` verfügt über folgende Optionen:



+---------------+------------------------------------------------+
| Option        | Erläuterung                                    |
+===============+================================================+
| name          | Name des Datenbank-Nutzers (z.B. xyz00_abc)    |
+---------------+------------------------------------------------+
| password      | Passwort                                       |
+---------------+------------------------------------------------+


Beispiel:

.. code-block:: console

    xyz00@hsadmin> postgresqluser.add ({set:{name:'xyz00_abc',password:'!1?2-3aBc'}})
 
