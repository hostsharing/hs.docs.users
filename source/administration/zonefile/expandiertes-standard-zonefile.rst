================================
Das expandierte Standardzonefile
================================


::

        $TTL 6H
        example.com.    IN      SOA     h00.hostsharing.net. hostmaster.hostsharing.net. (1303649373 6H 1H 1W 1H)
        example.com.    IN      NS      dns1.hostsharing.net.
        example.com.    IN      NS      dns2.hostsharing.net.
        example.com.    IN      NS      dns3.hostsharing.net.
        example.com.    IN      MX      30 mailin1.hostsharing.net.
        example.com.    IN      MX      30 mailin2.hostsharing.net.
        example.com.    IN      MX      30 mailin3.hostsharing.net.
        example.com.    IN      A       83.223.95.160
        example.com.    IN      AAAA    2a01:37:1000::53df:5fa0:0
        example.com.    IN      TXT     "v=spf1 include:spf.hostsharing.net ?all"
        *.example.com.  IN      MX      30 mailin1.hostsharing.net.
        *.example.com.  IN      MX      30 mailin2.hostsharing.net.
        *.example.com.  IN      MX      30 mailin3.hostsharing.net.
        *.example.com.  IN      A       83.223.95.160
        *.example.com.  IN      AAAA    2a01:37:1000::53df:5fa0:0
        *.example.com.  IN      TXT     "v=spf1 include:spf.hostsharing.net ?all"
