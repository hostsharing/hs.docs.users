===================
HSAdminmodul domain 
===================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|

Das HSAdminmodul ``domain`` verfügt über folgende Optionen:

+---------------+------------------------------------------------+
| Option        | Erläuterung                                    |
+===============+================================================+
| name          | Name einer Domain                              |
+---------------+------------------------------------------------+
| user          | Name des Domain-Admins                         |
+---------------+------------------------------------------------+
 
Beispiel:

.. code-block:: console

    $ domain.add ({set:{name:'hs-example.de',user:'edv43'}})
