=====
Netze
=====

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Michael Hierweck
          - Veit Schiele
:Date: |date|, |time|

Separierte Netzwerke
--------------------

Die Aufteilung in private, abgeschottete Netze (VLANs) zwischen den
Managed Servern eines Nutzers erlaubt effiziente und sichere Verbindungen. 

Dabei wird zwischen den folgenden Netzen unterschieden, die nicht
nur durch VLANs, sondern zusätzlich durch Verkabelung und separate Switches oder
Router getrennt sind:

Frontend-Netzwerk
    Dieses Netzwerk ist für allgemeine Anfragen gedacht. Die Firewall erlaubt
    aktuell den Zugang zu allen Adressen in diesem Netzwerk. Mittelfristig ist
    geplant, nur beabsichtigt belegte Ports freizugeben.
Server-Netzwerk
    Physikalisch getrenntes Netzwerk zur Kommunikation der Anwendungen
    untereinander. In diesem Netzwerk lassen sich VLANs aufschalten, um den
    Traffic zwischen verschiedenen Anwendungskomponenten sicher übertragen zu
    können. Darüberhinaus können auch verschiedene Traffic-Arten einer Anwendung
    separiert werden, so z.B. die Verbindung einer Anwendung zur Datenbank
    von derjenigen zu einem Cache oder Load-Balancer.
Speichernetzwerk
    Dieses Netzwerk wird verwendet für Storage-Traffic. Es basiert auf dedizierten
    Punkt-zu-Punkt Verkabelungen, die von außen nicht erreichbar sind. Das
    Netzwerk nutzt private IPv4-Adressen und ist nicht nur von außen nicht
    erreichbar sondern auch nur zugänglich für die Backup-Server, nicht jedoch
    für die Managed Server.
Management-Netzwerk
    Dieses physikalische Netzwerk wird verwendet für den Zugang zu IPMI-
    Controllern (Intelligent Platform Management Interface-Controller), RAC
    (Remote Access Controller), Switches und Routern. Es verwendet private IPv4-
    Adressen, die von außen nicht erreichbar sind. Es wird auch noch verfügbar
    sein, wenn Probleme in den anderen Netzen auftauchen.

