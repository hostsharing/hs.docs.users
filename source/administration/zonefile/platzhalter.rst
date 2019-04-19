===========
Platzhalter
===========

::

        Platzhalter         expandiert zu

        {DEFAULT_ZONEFILE}  {HEADER}
                            {SOA_RR}
                            {NS_RR}
                            {MX_RR}
                            {A_RR}
                            {AAAA_RR}
                            {WILDCARD_MX_RR}
                            {WILDCARD_A_RR}
                            {WILDCARD_AAAA_RR}

        {HEADER}    $TTL {TTL}

        {SOA_RR}    {DOM_HOSTNAME}.   IN SOA {SOA_HOSTNAME}. {SOA_EMAIL}. ({SIO} {REFRESH} {RETRY} {EXPIRE} {MINIMUM})

        {NS_RR}     {DOM_HOSTNAME}.   IN  NS  {DNS1_HOSTNAME}.
                    {DOM_HOSTNAME}.   IN  NS  {DNS2_HOSTNAME}.
                    {DOM_HOSTNAME}.   IN  NS  {DNS3_HOSTNAME}.

        {MX_RR}     {DOM_HOSTNAME}.   IN  MX  30 {MX1_HOSTNAME}.
                    {DOM_HOSTNAME}.   IN  MX  30 {MX2_HOSTNAME}.
                    {DOM_HOSTNAME}.   IN  MX  30 {MX3_HOSTNAME}.

        {A_RR}      {DOM_HOSTNAME}.   IN  A {DOM_IP4NUMBER}

        {AAAA_RR}   {DOM_HOSTNAME}.   IN  AAAA {DOM_IP6NUMBER}

        {WILDCARD_MX_RR}   *.{DOM_HOSTNAME}. IN  MX  30 {MX1_HOSTNAME}.
                           *.{DOM_HOSTNAME}. IN  MX  30 {MX2_HOSTNAME}.
                           *.{DOM_HOSTNAME}. IN  MX  30 {MX3_HOSTNAME}.

        {WILDCARD_A_RR}    *.{DOM_HOSTNAME}. IN  A {DOM_IP4NUMBER}

        {WILDCARD_AAAA_RR} *.{DOM_HOSTNAME}. IN  AAAA {DOM_IP6NUMBER}

        {TTL}              6H
        {SOA_HOSTNAME}     <HIVE>.hostsharing.net
        {SOA_EMAIL}        hostmaster.hostsharing.net
        {SIO}              <SEKUNDEN>
        {REFRESH}          6H
        {RETRY}            1H
        {EXPIRE}           1W
        {MINIMUM}          1H


Folgende Werte werden von Hostsharing verwaltet:

``<Sekunden>``  für die Anzahl der Sekunden, welche seit dem 01.01.1970 vergangen sind

``<FQDN>``  für den vollständigen, qualifizierten Domainnamen der Domain

``<IP>``  für die der Domain zugewiesene IP-Adresse


