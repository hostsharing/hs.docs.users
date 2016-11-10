================
Speicherbelegung
================
Zum belegten Web-Paket-Speicher zählen neben den Verzeichnissen und den darin abgelegten Daten ebenfalls die angelegten :doc:`Datenbanken<../datenbanken/index>`, Dateien unter ``/home/restore`` und temporäre
Daten im Verzeichnis ``/tmp``.

Quota
=====

Die Größe des von Ihnen belegten Speicherplatz können Sie sich ausgeben lassen mit::

    quota -s
    Disk quotas for user xyz00-user (uid 103045): 
         Filesystem   space   quota   limit   grace   files   quota   limit   grace
          /dev/vda2   1433M   1536M   2304M           19761       0       0        

D.h.:

- Es sind 1433 MB von 1536 MB  belegt
- Temporär dürfen bis zu 2304 MB in Anspruch genommen werden
- Außerdem sind 19761 Dateien angelegt worden
- Die maximale Anzahl der Dateien ist unbeschränkt
- Sobald die Quota überschritten wird, würde unter ``grace`` die verbleibende
  Zeit angezeigt, innerhalb derer wieder die Quota unterschritten sein muss.

Temporäre Dateien löschen
=========================

Gegebenenfalls können Sie temporäre Dateien auch regelmäßig mit enem Cronjob
löschen, z.B. mit dem folgenden Eintrag in der crontab::

    TMP=/tmp/user/$UID/
    @reboot find $TMP -delete >/dev/null 2>&1

Falls Sie ältere Dateien in Ihrem ``TMP``-Verzeichnis häufiger löschen wollen, 
können Sie dies z.B. folgendermaßen tun::

    */10 * * * * find $TMP -mmin +10 -delete >/dev/null 2>&1

.. note:: Beachten Sie jedoch bitte, dass einige Programme dort temporäre Dateien anlegen, 
   die sie während der gesamten Laufzeit verwenden, z.B. Caches.

.. note:: Viele Programme, insbesondere sog. Daemons, erzeugen temporäre
   Dateien, halten diese geöffnet und *unlink* diese. Dies hat den Vorteil, dass
   temporäre Dateien so automatisch gelöscht werden, sobald sie
   geschlossen/losgelassen werden, z.B. wenn das Programm abrupt beendet wird.
   Solche *unlinked* Dateien werden mit ``ls`` oder ``du`` nicht erfasst; sie
   können jedoch mit ``lsof`` (list open files) anzeigen lassen::

    lsof -s | awk '$5 == "REG"' | sort -n -r -k 7,7 | head -n 50

   zeigt die größten offenen Dateien an.

    lsof | awk '$5 == "REG" {freq[$2]++ ; names[$2] = $1 ;} END {for (pid in freq) print freq[pid], names[pid], pid ; }' | sort -n -r -k 1,1

   zeigt die Prozess mit den meisten geöffneten Dateien an.

Sparse-Dateien
==============

Gelegentlich können Festplattenspeicherbelegung und tatsächliche Größe
einer Datei differieren; falls ``du`` deutlich größere Werte anzeigt als
``du --apparent-size``, handelt es sich vmtl: um ein sog. `Sparse-Dateien
<https://de.wikipedia.org/wiki/Sparse-Datei>`_, bei dem Teile des
reservierten Platzes unbestimmt sind. Um diesen Platz freizugeben kann z.B.
folgendes angegeben werden::

    $ sync; echo 3 >/proc/sys/vm/drop_caches
