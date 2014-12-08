================
Eigenes Zonefile
================ 

Es können für :doc:`Domains<../domain/index>` jeweils eigene Zonefiles angelegt werden. In der Regel ist dies bei folgenden Anforderungen notwendig:

* Domain oder Sub-Domain extern aufschalten
* Dienste extern aufschalten (z.B. E-Mail)

In eigenen Zonefiles müssen Platzhalter verwendet werden. Diese Platzhalter ermöglichen das Ändern der DNS-Konfiguration seitens Hostsharing, ohne dass der Domain-Admin sein
Zonefile anpassen muss. Das Zonefile wird im Verzeichnis ``~/doms/example.com/etc/pri.example.com`` abgelegt und einige Minuten nach dem Speichern automatisch aktiv.

        .. warning::
 


                Das unsachgemäße Erstellen oder Fehler im eigenen Zonefile können zur Nichterreichbarkeit der Domain und zum Verlust von E-Mails führen!

Im Wiki der Mitglieder finden sich `Beispiele für eigene Zonefiles <https://wiki.hostsharing.net/index.php?title=Simple_Zonefile_Howto>`_.


