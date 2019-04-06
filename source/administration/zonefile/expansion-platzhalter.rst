=========================
Expansion der Platzhalter
=========================


Der Platzhalter für das Gesamtzonefile {DEFAULT_ZONFILE} wird in drei Schritten folgermaßen expandiert.

Zunächst wird der Gesamtplatzhalter Platzhalter durch Platzhalter für die Resource Records ersetzt:

::

        {HEADER}

        {SOA_RR}

        {NS_RR}

        {MX_RR}

        {A_RR}
        {AAAA_RR}

        {SPF_RR}

        {WILDCARD_MX_RR}

        {WILDCARD_A_RR}
        {WILDCARD_AAAA_RR}

        {WILDCARD_SPF_RR}

Dann werden die Platzhalter für Resource Records durch Platzhalter für Konfigurationsdaten ersetzt:

::

        {DOM_HOSTNAME}.   IN  SOA  {SOA_HOSTNAME}. {SOA_EMAIL}. ({SIO} {REFRESH} {RETRY} {EXPIRE} {MINIMUM})

        {DOM_HOSTNAME}.   IN  NS   {DNS1_HOSTNAME}.
        {DOM_HOSTNAME}.   IN  NS   {DNS2_HOSTNAME}.
        {DOM_HOSTNAME}.   IN  NS   {DNS3_HOSTNAME}.

        {DOM_HOSTNAME}.   IN  MX   30 {MX1_HOSTNAME}.
        {DOM_HOSTNAME}.   IN  MX   30 {MX2_HOSTNAME}.
        {DOM_HOSTNAME}.   IN  MX   30 {MX3_HOSTNAME}.

        {DOM_HOSTNAME}.   IN  A    {DOM_IP4NUMBER}
        {DOM_HOSTNAME}.   IN  AAAA {DOM_IP6NUMBER}                    ; in Kürze verfügbar

        {DOM_HOSTNAME}.   IN  TXT  "{SPF_POLICY}"                     ; in Kürze verfügbar

        *.{DOM_HOSTNAME}. IN  MX   30 {MX1_HOSTNAME}.
        *.{DOM_HOSTNAME}. IN  MX   30 {MX2_HOSTNAME}.
        *.{DOM_HOSTNAME}. IN  MX   30 {MX3_HOSTNAME}.

        *.{DOM_HOSTNAME}. IN  A    {DOM_IP4NUMBER}
        *.{DOM_HOSTNAME}. IN  AAAA {DOM_IP6NUMBER}                    ; in Kürze verfügbar

        *.{DOM_HOSTNAME}. IN  TXT  "{SPF_POLICY}"                     ; in Kürze verfügbar


Zuletzte werden die Platzhalter für Konfigurationsdaten durch Werte aus der Systemkonfiguration ersetzt:

::

        $TTL 6H

        <FQDN>.   IN  SOA  <HIVE>.hostsharing.net. hostmaster.hostsharing.net. (<SEKUNDEN 6H 1H 1W 1H)

        <FQDN>.   IN  NS   dns1.hostsharing.net.
        <FQDN>.   IN  NS   dns2.hostsharing.net.
        <FQDN>.   IN  NS   dns3.hostsharing.net.

        <FQDN>.   IN  MX   30 mailin1.hostsharing.net.
        <FQDN>.   IN  MX   30 mailin2.hostsharing.net.
        <FQDN>.   IN  MX   30 mailin3.hostsharing.net.

        <FQDN>.   IN  TXT  "v=spf1 include:spf.hostsharing.net ?all"  ; in Kürze verfügbar

        <FQDN>.   IN  A    <IP4>
        <FQDN>.   IN  AAAA <IP6>                                      ; in Kürze verfügbar

        *.<FQDN>. IN  MX   30 mailin1.hostsharing.net.
        *.<FQDN>. IN  MX   30 mailin2.hostsharing.net.
        *.<FQDN>. IN  MX   30 mailin3.hostsharing.net.

        *.<FQDN>. IN  TXT  "v=spf1 include:spf.hostsharing.net ?all"  ; in Kürze verfügbar

        *.<FQDN>. IN  A    <IP4>
        *.<FQDN>. IN  AAAA <IP6>                                      ; in Kürze verfügbar
