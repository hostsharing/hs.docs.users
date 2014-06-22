=======================
HSAdminmodul emailalias 
=======================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          - Dominic Schlegel

:Date: |date|, |time|


Das HSAdmin-Modul ``emailalias`` verfügt über folgende Optionen:

+---------------+------------------------------------------------------------------------+
| Option        | Erläuterung                                                            |
+===============+========================================================================+
| name          | Name des E-Mailalias                                                   |
+---------------+------------------------------------------------------------------------+
| target        | Ziel einer E-Mail-Adresse, mehrere Ziele werden durch Kommata getrennt |
+---------------+------------------------------------------------------------------------+

Beispiel:

.. code-block:: console

    xyz00@hsadmin> emailalias.add ({set:{name:'xyz00',target:'webmaster@hs-example.de'}})

