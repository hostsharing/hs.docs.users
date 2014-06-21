=================
HSAdminmodul user
=================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|


Das HSAdminmodul user verfügt über folgende Optionen:

+--------------------+----------------------------------+
| Option             | Erläuterung                      |
+====================+==================================+
| name               | Benutzerkennung (z.B. xyz00-abc) |
+--------------------+----------------------------------+
| comment            | Kommentar                        |
+--------------------+----------------------------------+
| password           | Passwort                         |
+--------------------+----------------------------------+
| shell              | shell (z.B. /bin/bash)           | 
+--------------------+----------------------------------+
| quota              | zugewiesener Speicherplatz       |
+--------------------+----------------------------------+
| quota_softlimit    | tolerierte Speichergrenze        |
+--------------------+----------------------------------+
| quota_hardlimit    | harte Speichergrenze             |
+--------------------+----------------------------------+

Beispiel:

.. code-block:: console

    $ user.add ({set:{name:'xyz00',comment:'your name',password:'!1?2-3abc',shell:'/bin/bash',quota:'100',quota_softlimit:'50',quota_hardlimit:'75'}})
