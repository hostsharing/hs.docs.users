=========================
Expansion der Platzhalter
=========================


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

               
