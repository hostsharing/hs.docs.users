===================
HSAdminmodul domain 
===================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          - Dominic Schlegel

:Date: |date|, |time|

Das HSAdminmodul ``domain`` verfügt über folgende Optionen:

+--------+------------------------+
| Option | Erläuterung            |
+========+========================+
| name   | Name einer Domain      |
+--------+------------------------+
| user   | Name des Domain-Admins |
+--------+------------------------+


+----------------+----------------------------------------+
| Option         | Erläuterung                            |
+================+========================================+
| greylisting    | Greylisting aktvieren/deaktivieren     |
+----------------+----------------------------------------+
| multiviews     | Multiviews aktivieren/deaktiveren      |
+----------------+----------------------------------------+
| indexes        | Indexes aktiveren/deaktivieren         |
+----------------+----------------------------------------+
| htdocsfallback | htdocsfallback  aktivieren/deaktiveren |
+----------------+----------------------------------------+
| includes       | Includes aktivieren/deaktivieren       |
+----------------+----------------------------------------+

Beispiel:


.. code-block:: console

    xyz00@hsadmin> domain.add ({set:{name:'hs-example.de',user:'xyz00'}})
