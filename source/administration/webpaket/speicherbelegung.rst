================
Speicherbelegung
================

Zum belegten Web-Paket-Speicher zählen neben der Verzeichnis-Struktur /home/pacs/xyz00 und den 
darin abgelegten Daten ebenfalls die Sicherungen der :doc:`Datenbanken<../datenbanken/index>`
unter /home/pacs/xyzoo/.bak/, gegebenenfalls  unter ``/home/restore`` 
vorhandene Dateien und temporäre Daten im Verzeichnis ``/tmp``.

Die Speicherbegrenzung für ein Web-Paket ist unter Linux durch eine Quota
für die Gruppe xyz00 realisiert. Die aktuelle Belegung der Quota
läßt sich mit dem Kommando

.. code-block:: console

    quota -gs
    
ermitteln. Die Ausgabe 
    
.. code-block:: console

    Disk quotas for group xyz00 (gid 999999): 
       Filesystem   space   quota   limit   grace   files   quota   limit   grace
       /dev/vda2   1433M   1536M   2304M           19761       0       0        

bedeutet:

- Es sind 1433 MB von 1536 MB  belegt
- Temporär dürfen bis zu 2304 MB in Anspruch genommen werden
- Außerdem sind 19761 Dateien angelegt worden
- Die maximale Anzahl der Dateien ist unbeschränkt
- Sobald die Quota überschritten wird, würde unter ``grace`` die verbleibende
  Zeit angezeigt, innerhalb derer wieder die Quota unterschritten sein muss.
  Sonst wird das Paket gesperrt, das heißt es können keine Dateien mehr 
  angelegt werden, E-Mails werden nicht mehr zugestellt.

