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
       /dev/vda2   5587M   6144M   9216M            103k   6292k   6292k     

bedeutet:

- Es sind 5587 MB von 6144 MB  belegt
- Temporär dürfen bis zu 9216 MB in Anspruch genommen werden
- Außerdem sind 103.000 Dateien angelegt worden
- Die maximale Anzahl der Dateien ist auf 6.292.000 beschränkt
- Sobald die Quota überschritten wird, würde unter ``grace`` die verbleibende
  Zeit angezeigt, innerhalb derer wieder die Quota unterschritten sein muss.
  Sonst wird das Paket gesperrt, das heißt es können keine Dateien mehr 
  angelegt werden, E-Mails werden nicht mehr zugestellt.

