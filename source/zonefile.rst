========
Zonefile
========

:Authors: - Uwe Müller
:Date: 2013-28-08

[Anmerkung: Bild-skizze(n) einfügen]

Allgemein
---------

Das Zonefile enthält die Konfiguration des Domain Name Service (DNS)der Domain. Im Zonefile wird hinterlegt, welche Hostnamen innerhalb der Domain existieren und auf welche IP-Adressen 
diese zeigen und welches Mailsystem für die Domain zuständig ist. Das Standardzonefile ist für jede Domain unter /etc/bind/pri.example.com zu finden. 

Das expandierte Standardzonefile
--------------------------------
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



Eigenes Zonefile
---------------- 

Es können für Domains/Subdomains jeweils eigene Zonefiles angelegt werden, in der Regel ist dies bei folgenden
Anforderungen notwendig:

- Domain oder Subdomain extern Aufschalten
- Dienste extern aufschalten (z.B. E-Mail)
  
In eigenen Zonenfiles müssen Platzhalter verwendet werden. Diese Platzhalter ermöglichen
das Ändern der DNS-Konfiguration seitens Hostsharing, ohne das der Domain-Admin sein
Zonefile anpassen muss. Das Zonefile wird im Verzeichnis ~/doms/example.com/etc/pri.example.com abgelegt und . 
einige Minuten nach dem Speichern automatisch aktiv.
[http://wiki.hostsharing.net beispiele eigenes zonefile]


Platzhalter
-----------
::
        
        Platzhalter             expandiert zu

        {DEFAULT_ZONEFILE}	{HEADER}
        			{SOA_RR}
                                {NS_RR}
                                {MX_RR}	
                                {A_RR}
                                {WILDCARD_MX_RR}
                                {WILDCARD_A_RR}

        {HEADER}		$TTL {TTL}
        
        {SOA_RR}		{DOM_HOSTNAME}. IN SOA {SOA_HOSTNAME}. {SOA_EMAIL}. (
                                        {SIO}		; serial secs since Jan 1 1970
                                        {REFRESH}	; refresh (>=10000)
                                        {RETRY}		; retry (>=1800)
                                        {EXPIRE}	; expire
                                        {MINIMUM}	; minimum
                                )	

        {NS_RR}			{DOM_HOSTNAME}.		IN	NS	{DNS1_HOSTNAME}.
                                {DOM_HOSTNAME}.		IN	NS	{DNS2_HOSTNAME}.
                                {DOM_HOSTNAME}.		IN	NS	{DNS3_HOSTNAME}.

        {MX_RR} 		{DOM_HOSTNAME}.		IN	MX	30 {MX1_HOSTNAME}.
                                {DOM_HOSTNAME}.		IN	MX	30 {MX2_HOSTNAME}.
                                {DOM_HOSTNAME}.		IN	MX	30 {MX3_HOSTNAME}.

        {A_RR}			{DOM_HOSTNAME}.		IN	A	{DOM_IPNUMBER}

        {WILDCARD_MX_RR} 	*.{DOM_HOSTNAME}.	IN	MX	30 {MX1_HOSTNAME}.
                                *.{DOM_HOSTNAME}.	IN	MX	30 {MX2_HOSTNAME}.
                                *.{DOM_HOSTNAME}.	IN	MX	30 {MX3_HOSTNAME}.

        {WILDCARD_A_RR} 	*.{DOM_HOSTNAME}.	IN	A	{DOM_IPNUMBER}


        {TTL} 			6H
        {SOA_HOSTNAME} 		<HIVE>.hostsharing.net
        {SOA_EMAIL}		hostmaster.hostsharing.net
        {SIO} 			<SEKUNDEN>
        {REFRESH} 		6H
        {RETRY} 		1H
        {EXPIRE} 		1W
        {MINIMUM} 		1H

        {DNS1_HOSTNAME} 	dns1.hostsharing.net
        {DNS2_HOSTNAME} 	dns2.hostsharing.net
        {DNS3_HOSTNAME} 	dns3.hostsharing.net

        {MX1_HOSTNAME} 		mailin1.hostsharing.net
        {MX2_HOSTNAME} 		mailin2.hostsharing.net
        {MX3_HOSTNAME} 		mailin3.hostsharing.net

        {DOM_HOSTNAME} 		<FQDN>
        {DOM_IPNUMBER}  	<IP>


Folgende Werte werden von Hostsharing verwaltet:

<Sekunden> 	für die Anzahl der Sekunden, welche seit dem 01.01.1970 vergangen sind

<FQDN> 		für den vollständigen, qualifizierten Domainnamen der Domain

<IP> 		für die der Domain zugewiesene IP-Adresse


Expansion der Platzhalter
-------------------------

Der Platzhalter für das Gesamtzonefile {DEFAULT_ZONFILE} wird in drei Schritten folgermaßen expandiert. Zunächst werden die komplexen Platzhalter ersetzt.
::

        {DOM_HOSTNAME}. IN SOA {SOA_HOSTNAME}. {SOA_EMAIL}. (
                {SIO}           ; serial secs since Jan 1 1970
                {REFRESH}       ; refresh (>=10000)
                {RETRY}		; retry (>=1800)
                {EXPIRE}	; expire
        	{MINIMUM}	; minimum
        	)
        {DOM_HOSTNAME}.		IN	NS	{DNS1_HOSTNAME}.
        {DOM_HOSTNAME}.		IN	NS	{DNS2_HOSTNAME}.
        {DOM_HOSTNAME}.		IN	NS	{DNS3_HOSTNAME}.

        {DOM_HOSTNAME}.		IN	MX	30 {MX1_HOSTNAME}.
        {DOM_HOSTNAME}.		IN	MX	30 {MX2_HOSTNAME}.
        {DOM_HOSTNAME}.		IN	MX	30 {MX3_HOSTNAME}.

        {DOM_HOSTNAME}.		IN	A	{DOM_IPNUMBER}

        *.{DOM_HOSTNAME}.	IN	MX	30 {MX1_HOSTNAME}.
        *.{DOM_HOSTNAME}.	IN	MX	30 {MX2_HOSTNAME}.
        *.{DOM_HOSTNAME}.	IN	MX	30 {MX3_HOSTNAME}.

        *.{DOM_HOSTNAME}.	IN	A	{DOM_IPNUMBER}

Anschließend werden die atomaren Platzhalter ersetzt.
::
        
        $TTL 6H

        <FQDN>. IN SOA <HIVE>.hostsharing.net. hostmaster.hostsharing.net. (
                <SEKUNDEN>	; serial secs since Jan 1 1970
                6H		; refresh (>=10000)
                1H		; retry (>=1800)
                1W		; expire
                1H		; minimum
                )

        <FQDN>.		IN	NS	dns1.hostsharing.net.
        <FQDN>.		IN	NS	dns2.hostsharing.net.
        <FQDN>.		IN	NS	dns3.hostsharing.net.

        <FQDN>.		IN	MX	30 mail1.hostsharing.net.
        <FQDN>.		IN	MX	30 mail2.hostsharing.net.
        <FQDN>.		IN	MX	30 mail3.hostsharing.net.

        <FQDN>.		IN	A	<IP>

        *.<FQDN>.	IN	MX	30 mail1.hostsharing.net.
        *.<FQDN>.	IN	MX	30 mail2.hostsharing.net.
        *.<FQDN>.	IN	MX	30 mail3.hostsharing.net.

        *.<FQDN>.	IN	A	<IP>

Kontrolle der Änderungen
------------------------

Durchgeführte Änderungen am Zonefile können mit Hilfe der Logdatei named.log überprüft werden:

.. code-block:: console
   
    $ tail -f /var/log/named/named.log 
    $ tail -f /var/log/named/named.log | grep example.com
 
Zur Überprüfung von Änderungen am Zonefile sollte immer die Seriennummer in den DNS-Servern mit der aktuellen Seriennummer im Zonefile verglichen werden:

.. code-block:: console

   $ dig -t SOA @dns1 example.com | grep '^example.com.*SOA' | awk '{ print $7 }'
   $ grep serial /etc/bind/pri.example.com | awk '{ print $1 }' 


Das eigene Zonefile deaktivieren/zurücksetzen
---------------------------------------------

Im Verzeichnis ~/doms/example.com/etc/ das vorhandene Zonefile (pri.example.com) leeren (0 Bytes). Das leere Zonefile wird durch einen Robot gelöscht und es gilt das Standardzonefile. 
