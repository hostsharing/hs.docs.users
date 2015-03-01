=======
HSAdmin
=======
HSAdmin ist ein Werkzeug zur Verwaltung von Nutzern, E-Mail-Adressen, E-Mail-Aliases, Domains, Datenbanken und Datenbank-Nutzern.
Die Bedienung erfolgt über ein :doc:`Webfrontend<webfrontend>` oder mit dem HSAdmin-Client ``hsscript`` in der Konsole:

.. code-block:: console

    $ hsscript -u xyz00 -i 


 
HSAdmin verfügt über folgende Module:

+---------------------------------------+-----------------------------------------------------+
| Modul                                 | Erläuterung                                         |
+=======================================+=====================================================+
| :doc:`user<user>`                     | Modul zur Nutzerverwaltung                          |
+---------------------------------------+-----------------------------------------------------+
| :doc:`mysqldb<mysqldb>`               | Modul zur Verwaltung von MySQL-Datenbanken          |
+---------------------------------------+-----------------------------------------------------+
| :doc:`mysqluser<mysqluser>`           | Modul zur Verwaltung vom MySQL-Datenbanknutzern     |
+---------------------------------------+-----------------------------------------------------+
| :doc:`postgresqldb<postgresqldb>`     | Modul zur Verwaltung von PostgreSQL-Datenbanken     |
+---------------------------------------+-----------------------------------------------------+
| :doc:`postgresqluser<postgresqluser>` | Modul zur Verwaltung von PostgreSQL-Datenbanknutzer |
+---------------------------------------+-----------------------------------------------------+
| :doc:`emailaddress<emailaddress>`     | Modul zur Verwaltung von E-Mail-Adressen            |
+---------------------------------------+-----------------------------------------------------+
| :doc:`emailalias<emailaliases>`       | Modul zur Verwaltung von E-Mail-Aliasen             |
+---------------------------------------+-----------------------------------------------------+
| :doc:`domain<domain>`                 | Modul zur Verwaltung von Domains in einem Web-Paket |
+---------------------------------------+-----------------------------------------------------+
| :doc:`q<q>`                           | Modul zur Suche von Systemaufträgen von HSAdmin     |
+---------------------------------------+-----------------------------------------------------+


Die HSAdmin-Module verfügen über folgenden Funktionen:

+----------------+---------------+
| Funktion       | Erläuterung   |
+================+===============+
| search         | suchen        |
+----------------+---------------+
| add            | hinzufügen    |    
+----------------+---------------+
| update         | aktualisieren |
+----------------+---------------+
| remove         | löschen       |
+----------------+---------------+


.. toctree::
    :maxdepth: 1
    
    syntax
    user 
    mysqldb
    mysqluser
    postgresqldb
    postgresqluser
    emailaddress
    emailaliases
    domain
    q
    webfrontend               


