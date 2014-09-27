======
Backup
======

.. |date| date:: %d.%m.%Y 
.. |time| date:: %H:%M  
   
:Authors: - Michael Hierweck
          - Uwe Müller  
   
:Date: |date|, |time|


Hostsharing führt täglich Sicherungen der Daten der Produktivsysteme durch.
Die Datensicherungen werden in einem vom Produktivrechenzentrum rund 500km
entfernten Rechenzentrum aufbewahrt.
Die Datenübertragung zwischen den Standorten erfolgt über einen
verschlüsselten SSH-Tunnel.
Die Backups jedes Produktivsystems werden separat archiviert und können
nur von diesem System zur Rücksicherung angefordert werden.
Ferner wird gewährleistet, dass Backups nicht nachträglich kompromittiert
 werden können.

In der Regel werden mindestens 15 Backups vorgehalten. 
