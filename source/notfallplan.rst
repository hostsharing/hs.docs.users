===========
Notfallplan
===========

:Authors: - Michael Hierweck
          - Veit Schiele
:Date: 2013-07-05

Der Notfallplan bietet einen Überblick über mögliche Notfallszenarien und wie
die Hostsharing e.G. und deren Mitarbeiter ggf. damit umgehen.

Für jedes einzelne Notfallszenario beschreiben wir:

- welche Vorsorgemaßnahmen wir getroffen haben, um das Eintreten dieses Szenarios
  zu vermeiden
- welche Maßnahmen wir treffen werden, um den gewünschten Zustand
  wiederherzustellen
- die Zeiten, die zur Wiederherstellung benötigt werden

Hardware-Fehler
===============

VM-Server
---------

Vorsorgemaßnahmen
 Es wurden verschiedene Maßnahmen getroffen, die die Ausfallzeiten
 gering halten sollen:

 - Hot-Standby-Server
 - SLA (Service Level Agreement) mit DELL

Maßnahmen im Notfall:
 Entsprechend werden im Notfall die folgenden zwei Maßnahmen
 getroffen:

 - Wechseln auf die Hot-Standby-Server
 - Inanspruchnahme des SLA mit Dell

Wiederherstellungszeit
 Die Wiederherstellung der Services ist dank Hot-Standby-Server in kurzer Zeit
 möglich

 Das SLA mit Dell sichert die *on-site*-Problembehebung binnen vier
 Stunden rund um die Uhr zu.

.. Netzwerk-Komponenten
   --------------------

   Vorsorgemaßnahmen
    TODO
   Maßnahmen im Notfall
    TODO
   Wiederherstellungszeit
    TODO

Höhere Gewalt
=============

.. Stromausfall
   ------------

   Vorsorgemaßnahmen
    Zukünftig zweiter Backup-Server in einem anderen Rechenzentrum
   Maßnahmen im Notfall
    TODO
   Wiederherstellungszeit
    TODO

Netzwerkausfall
---------------

Vorsorgemaßnahmen
 Das Berliner Rechenzentrum ist extern mehrfach redundant mit
 Glasfaser an die folgenden Internet-Knoten angeschlossen:

 - Level3
 - KPN
 - Cogent
 - LambdaNet
 - DFN
 - ECIX
 - BCIX
 - Plusline

 Das Frankfurter Rechenzentrum mit dem Backup-System ist mehrfach
 redundant mit Glasfaser an die folgenden Internet-Knoten
 angeschlossen:

 - ECIX Hamburg
 - ECIX Duesseldorf 
 - KleyRexx
 - DeCIX indirekt: 1 Hop

Maßnahmen im Notfall
 Das jeweilige Rechenzentrum übernimmt die Wiederherstellungsmaßnahmen im
 Notfall

.. Wiederherstellungszeit
    Automatische Änderung des Routings kann bis zu mehrere Minuten dauern.

Ausfall des Rechenzentrums
--------------------------

Vorsorgemaßnahmen
 Die beteiligten Rechenzentren unternehmen eine Reihe von Maßnahmen,
 um einen solchen Ausfall abzusichern.

 .. , namentlich:

    - TODO

 Das tägliche Backup der Daten in ein anderes Rechenzentrum erlaubt den
 Rückgriff auf Daten, der zwar mit dem Verlust aller Änderungen zwischen Backup-
 und Ausfallzeitpunkt einhergeht, in der Regel jedoch nur alle eingehenden
 E-Mails, Bestellungen oder andere Nutzeraktionen des Tages betreffen.

.. Maßnahmen im Notfall
    TODO
.. Wiederherstellungszeit
    TODO

Software-Fehler
===============

Konfigurationsfehler
--------------------

Vorsorgemaßnahmen
    - Versionierte und reproduzierbare Konfigurationsverwaltung.

      Zukünftig soll zusätzlich noch eine automatisierte
      Konfigurationsverwaltung hinzukommen.

    - ``sudo`` darf von den Hostmastern nur im 4-Augen-Prinzip angewendet werden.
    - Alle Shell-Aktionen der Hostmaster werden mit
      `ttyrec <0xcc.net/ttyrec/>`_ aufgezeichnet und sind damit nahvollziehbar.
    - Um die Nachvollziehbarkeit zu erhöhen werden zukünftig auch alle Aufrufe
      in HSAdmin aufgezeichnet. Dies erleichtert zusammen mit dem
      Protokollieren der Shell-Aktionen das Wiederherstellen einer bestehenden
      Konfiguration.

   Maßnahmen im Notfall
    Zurückrollen der Konfigurationsänderungen aus der Versionsverwaltung
    und Wiederherstellen der Daten aus dem letzten Backup sofern mit
    dem Konfigurationsfehler ein Datenverlust entstanden ist.

Wiederherstellungszeit
    maximal 1 Tag nach Bekanntwerden des Fehlers

Anwendungsfehler
----------------

Vorsorgemaßnahmen
 Automatisierte, versionierte und reproduzierbare Anwendungsentwicklung
Maßnahmen im Notfall
 Zurückrollen der Änderungen aus der Versionsverwaltung und Wiederherstellen der Daten
 aus dem letzten Backup sofern mit dem Fehler ein Datenverlust entstanden ist.
Wiederherstellungszeit
 maximal 2 Werktage nach Bekanntwerden des Fehlers


