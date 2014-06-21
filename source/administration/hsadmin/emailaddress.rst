=========================
HSAdminmodul emailaddress 
=========================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|



Das HSAdminmodul ``emailaddress`` verfügt über folgende Optionen:

+---------------+----------------------------------------------------------------------+
| Option        | Erläuterung                                                          |
+===============+======================================================================+
| domain        | Name einer  Domain                                                   |
+---------------+----------------------------------------------------------------------+
| localpart     | bezeichnet den lokalen  Part einer Domain (Part vor '@')             |
+---------------+----------------------------------------------------------------------+
| target        | Ziel einer E-Mail-Adresse, mehrere Ziele werden durch Komma getrennt |
+---------------+----------------------------------------------------------------------+

Beispiel:

.. code-block:: console

    $ emailaddress.add ({set:{domain:'hs-example.de',localpart:'info',target:'ihre@emailadresse.de'}})

