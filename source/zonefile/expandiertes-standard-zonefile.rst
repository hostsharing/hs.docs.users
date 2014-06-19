================================
Das expandierte Standardzonefile
================================

:Authors: - Uwe Müller

.. |date| date:: %d. %m. %Y
.. |time| date:: %H:%M




::

        $TTL 6H
        example.com. IN SOA h00.hostsharing.net. hostmaster.hostsharing.net. (
                1303649373      ; serial secs since Jan 1 1970  
                6H              ; refresh (>=10000)
                1H              ; retry (>=1800)
                1W              ; expire
                1H              ; minimum
                )

        example.com.    IN      NS      dns1.hostsharing.net.
        example.com.    IN      NS      dns2.hostsharing.net.
        example.com.    IN      NS      dns3.hostsharing.net.
        example.com.    IN      MX      30 mailin1.hostsharing.net.
        example.com.    IN      MX      30 mailin2.hostsharing.net.
        example.com.    IN      MX      30 mailin3.hostsharing.net.
        example.com.    IN      A       83.223.95.160
        *.example.com.  IN      MX      30 mailin1.hostsharing.net.
        *.example.com.  IN      MX      30 mailin2.hostsharing.net.
        *.example.com.  IN      MX      30 mailin3.hostsharing.net.
        *.example.com.  IN      A       83.223.95.160



