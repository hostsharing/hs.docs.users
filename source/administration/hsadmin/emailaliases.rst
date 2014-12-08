========================
HSAdmin-Modul emailalias
========================

Das HSAdmin-Modul ``emailalias`` verfügt über folgende Optionen:

+---------------+------------------------------------------------------------------------+
| Option        | Erläuterung                                                            |
+===============+========================================================================+
| name          | Name des E-Mail-Alias                                                  |
+---------------+------------------------------------------------------------------------+
| target        | Ziel einer E-Mail-Adresse; mehrere Ziele werden durch Kommata getrennt |
+---------------+------------------------------------------------------------------------+

Beispiel:

.. code-block:: console

    xyz00@hsadmin> emailalias.add ({set:{name:'xyz00',target:'webmaster@hs-example.de'}})

