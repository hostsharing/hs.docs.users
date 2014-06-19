=========
Allgemein
=========

:Authors: - Uwe Müller

.. |date| date:: %d. %m. %Y
.. |time| date:: %H:%M


Das Zonefile enthält die Konfiguration des Domain-Name-Service (DNS) einer Domain. Im Zonefile wird hinterlegt welche Hostnamen innerhalb einer Domain existieren und auf welche IP-Adressen 
diese zeigen und welches Mailsystem für eine Domain zuständig ist. 
Das Standardzonefile ist für jede Domain unter ``/etc/bind/pri.example.de`` zu finden. 

Es ist möglich ein :doc:`eigenes Zonefile<eigenes-zonefile>` für eine Domain zu eingesetzt. Für diesen Zweck werden Platzhalter verwendet, die es ermöglichen einen jeweils spezifischen Teil eines Zonefile zu ändern.


