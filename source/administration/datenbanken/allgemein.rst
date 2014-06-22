=========
Allgemein
=========

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M


:Author: - Uwe Müller
         - Dominic Schlegel

:Date: |date|, |time|           



Jeder :term:`Hive` hat einen eigenen MySQL- und PostgresSQL-Datenbankserver. Daraus ergibt sich, dass 
der jeweilige MySQL- und PostgresSQL-Server von allen auf einem :term:`Hive` eingerichteten :doc:`Web-Paketen<../webpaket/index>` gemeinsam genutzt wird.

Der externe Zugriff auf die Datenbanken ist über einen SSH-Tunnel möglich.
