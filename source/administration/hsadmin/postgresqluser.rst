===========================
HSAdminmodul postgresqluser 
===========================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          - Dominic Schlegel

:Date: |date|, |time|


Das HSAdminmodul ``postgresqluser`` verfügt über folgende Optionen:



+---------------+------------------------------------------------+
| Option        | Erläuterung                                    |
+===============+================================================+
| name          | Name des Datenbanknutzers (z.B. xyz00_abc)     |
+---------------+------------------------------------------------+
| password      | Password                                       |
+---------------+------------------------------------------------+


Beispiel:

.. code-block:: console

    $ postgresqluser.add ({set:{name:'xyz00_abc',password:'!1?2-3aBc'}})
 
