==========================
HSAdmin-Modul emailaddress
==========================


Das HSAdmin-Modul ``emailaddress`` verfügt über folgende Optionen:

+---------------+------------------------------------------------------------------------+
| Option        | Erläuterung                                                            |
+===============+========================================================================+
| domain        | Name einer  Domain                                                     |
+---------------+------------------------------------------------------------------------+
| localpart     | bezeichnet den lokalen  Part einer Domain (Part vor '@')               |
+---------------+------------------------------------------------------------------------+
| target        | Ziel einer E-Mail-Adresse, mehrere Ziele werden durch Kommata getrennt |
+---------------+------------------------------------------------------------------------+

Beispiel:

.. code-block:: console

    xyz00@hsadmin> emailaddress.add ({set:{domain:'hs-example.de',localpart:'info',target:'ihre@emailadresse.de'}})

.. code-block:: console

    xyz00@hsadmin> emailaddress.search({where:{domain:"YOUR_DOMAIN"}})
