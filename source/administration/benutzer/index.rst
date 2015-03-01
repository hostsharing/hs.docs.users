========
Benutzer
========

Für unterschiedliche Aufgaben werden Rollen vergeben, die durch die Vergabe von Rechten auf Betriebssystemebene definiert werden. 
Die Hierarchie gliedert sich in absteigender Reihenfolge:

* :doc:`Mitgliedskennung <mitglied>` zur Verwaltung der Mitgliedschaft und *aller* gebuchten :doc:`Web-Pakete</administration/webpaket/index>`,
* :doc:`Paket-Admin <paket-admin>` zur Verwaltung eines :doc:`Web-Pakets</administration/webpaket/index>`,
* :doc:`Domain-Admin <domain-admin>` zur Verwaltung einer oder mehrerer Domains *in* einem Web-Paket,
* :doc:`E-Mail-Postfach <userohneshell>` ohne die Zuweisung einer shell.  
* :doc:`Datenbank-Nutzer<datenbanknutzer>` zur Verwaltung einer oder mehrerer :doc:`Datenbanken<../datenbanken/index>`.

Die Verwaltung von Domains (Registrierung, Transfer, DNS-Server etc.) erfolgt durch den

* :doc:`Domain-Verwalter <domainaccount>`

im externen Verwaltungstool und ist unabhängig von den oben genannten Rollen. 


Inhalt: 

.. toctree::
        :maxdepth: 1
        
        mitglied
        paket-admin
        domain-admin
        userohneshell
        datenbanknutzer
        domainaccount
