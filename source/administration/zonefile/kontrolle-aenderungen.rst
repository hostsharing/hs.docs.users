========================
Kontrolle der Änderungen
========================

Durchgeführte Änderungen am Zonefile können mit Hilfe der Logdatei named.log überprüft werden:

.. code-block:: console


    $ tail -f /var/log/named/named.log
    $ tail -f /var/log/named/named.log | grep example.com

Zur Überprüfung von Änderungen am Zonefile sollte immer die Seriennummer in den DNS-Servern mit der aktuellen Seriennummer im Zonefile verglichen werden:

.. code-block:: console

   $ dig -t SOA @dns1 example.com | grep '^example.com.*SOA' | awk '{ print $7 }'
   $ grep serial /etc/bind/pri.example.com | awk '{ print $1 }'



