=======
HSAdmin
=======

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|

HSAdmin ist ein Werkzeug zur Verwaltung von Nutzern, E-Mail-Adressen, E-Mailaliases, Domains, Datenbanken und Datenbank-Nutzern.
Die Bedienung erfolgt über ein :doc:`Webfrontend<webfrontend>` oder mit dem HSAdminclient ``hsscript`` in der Konsole:

.. code-block:: console

    $ hsscript -u xyz00 -i 

HSAdmin verfügt über mehrere :doc:`Module<module>` mit folgenden Funktionen:

+----------------+---------------+
| Funktion       + Erläuterung   |
+================+===============+
| search         | Suche         |
+----------------+---------------+
| add            | Zufügen       |    
+----------------+---------------+
| update         | Aktualisieren |
+----------------+---------------+
| remove         | Löschen       |
+----------------+---------------+


.. toctree::
    :maxdepth: 1
    
    syntax
    benutzerverwaltung
    datenbankverwaltung
    domainverwaltung
    emailalias
    emailalias-verwaltung
    emailverwaltung
    hsadmin-cheetset
    webfrontend               
