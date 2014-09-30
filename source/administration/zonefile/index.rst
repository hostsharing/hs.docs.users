============================
Zonefile
============================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M


:Authors: - Uwe Müller

:Date: |date|, |time|

Das Zonefile enthält die Konfiguration des Domain-Name-Service (DNS) einer :doc:`Domain<../domain/index>`. Im Zonefile wird hinterlegt welche Hostnamen innerhalb einer Domain existieren, auf welche IP-Adressen 
diese zeigen und welches Mailsystem für eine Domain zuständig ist. 
Das Standardzonefile ist für jede Domain unter ``/etc/bind/pri.example.de`` zu finden. 

Es ist möglich, ein :doc:`eigenes Zonefile<eigenes-zonefile>` für eine Domain einzusetzen.
Dabei können und sollen Platzhalter verwendet werden, die es ermöglichen, einen jeweils spezifischen Teil eines Zonefile zu ändern.


Inhalt: 


.. toctree::
        :maxdepth: 1
        
        expandiertes-standard-zonefile
        platzhalter
        expansion-platzhalter
        eigenes-zonefile
        kontrolle-aenderungen
        eigenes-zonefile-deaktivieren


