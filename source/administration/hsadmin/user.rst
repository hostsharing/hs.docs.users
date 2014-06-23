=================
HSAdminmodul user
=================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          - Dominic Schlegel

:Date: |date|, |time|


Das HSAdminmodul ``user`` verfügt über folgende Optionen:

+-----------------+----------------------------------------+
| Option          | Erläuterung                            |
+=================+========================================+
| name            | Benutzerkennung (z.B. xyz00-abc)       |
+-----------------+----------------------------------------+
| comment         | Kommentar                              |
+-----------------+----------------------------------------+
| password        | Passwort                               |
+-----------------+----------------------------------------+
| shell           | shell (z.B. ``/bin/bash)``             |
+-----------------+----------------------------------------+
| quota           | zugewiesener Speicherplatz in Megabyte |
+-----------------+----------------------------------------+
| quota_softlimit | tolerierte Speichergrenze in Megabyte  |
+-----------------+----------------------------------------+
| quota_hardlimit | harte Speichergrenze in Megabyte       |
+-----------------+----------------------------------------+

Beispiel:

.. code-block:: console

    xyz00@hsadmin> user.add ({set:{name:'xyz00-mustermann',comment:'Max Mustermann',password:'!1?2-3aBc',shell:'/bin/bash',quota:'100',quota_softlimit:'50',quota_hardlimit:'75'}})
