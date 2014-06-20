============================
Benutzer
============================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
         
:Date: |date|, |time|
 

Für unterschiedliche Aufgaben werden Rollen vergeben, die durch die Vergabe von Rechten auf Betriebssystemebene definiert werden. 
Die Hierarchie gliedert sich in absteigender Reihenfolge:

* :doc:`Mitglieds-Account <mitglied>` zur Verwaltung der Mitgliedschaft und *aller* gebuchten :doc:`Webpakete</administration/webpaket/index>`,
* :doc:`Paket-Admin <paket-admin>` zur Verwaltung eines Webpaketes,
* :doc:`Domain-Admin <domain-admin>` zur Verwaltung einer oder mehrerer Domains *in* einem Webpaket,
* :doc:`E-Mail-Account <userohneshell>` ohne die Zuweisung einer Shell.  
* :doc:`Datenbank-Nutzer<datenbanknutzer>` zur Verwaltung einer oder mehrerer Datenbanken.

Die Verwaltung von Domains (Registrierung, Transfer, DNS-Server etc.) erfolgt durch den

* :doc:`Domain-Account <domainaccount>`.

im externen Verwaltungstool und ist unabhängig von den oben genannten Rollen. 


Inhalt: 

.. toctree::
        :maxdepth: 1
        
        allgemein        
        mitglied
        paket-admin
        domain-admin
        userohneshell
        datenbanknutzer
        domainaccount
