===========
Replikation
===========

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Michael Hierweck
:Date: |date|, |time|

Hostsharing repliziert mit Hilfe der Software DRBD die Festplatteninhalte
aller Produktivsysteme in Echtzeit auf ein Standby-System (RAID 1 über
das Netzwerk).

Auf diese Weise stellt Hostsharing sicher, dass im Fall eines Hardwareschadens
der Betrieb mit allen persistent gespeicherten Daten unverzüglich fortgesetzt
werden kann, ohne dass durch das Einspielen des Backups Datenänderungen,
die sich in der Zwischenzeit ergeben haben - etwa eingegangene
E-Mails oder Datenbanktransaktionen - verloren gehen.
