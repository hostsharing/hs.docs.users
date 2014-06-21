================
Traffic-Log-File
================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller
          
:Date: |date|, |time|

               
Der im :doc:`Web-Paket<../webpaket/index>` erzeugte Traffic wird dem :doc:`Paket-Admin<../benutzer/paket-admin>` unter ``/home/pacs/xyz00/var/traffic-iptables-YYYY-MM.log`` zugänglich gemacht.
Das Logfile hat folgenden Aufbau:

+----------+-------+-------------+------------+--------------+---------------+----------+--------------+----------+
| Datum    | Paket | Monatslimit | Tageslimit | Trafficsumme | IP-Adresse 1  |Traffic 1 | IP-Adresse 2 | Traffic 2|
+==========+=======+=============+============+==============+===============+==========+==============+==========+
|2012-08-01| xyz00 |  10240      | 341.333    |   89.367     | 83.223.79.125 | 89.367   |              | 0.000    |
+----------+-------+-------------+------------+--------------+---------------+----------+--------------+----------+


Bedeutung der einzelnen Spalten:

* Datum:        Datum der Messung
* Paket:        Name des Webpakets
* Monatslimit:  Gebuchter Gesamttraffic pro Monat in Megabyte
* Tageslimit:   Tägliches Traffic-Kontingent bei gleichmäßigem Verbrauch in Megabyte 
* Trafficsumme: Gesamtsumme des angefallenen Traffic bis zum angegebenen Tag in Megabyte
* IP-Adresse 1: Primäre IP-Adresse des Webpakets 
* Traffic 1:    Über die primäre IP-Adresse angefallener Traffic in Megabyte
* IP-Adresse 2: Sekundäre IP-Adresse des Pakets 
* Traffic 2:    Über die sekundäre IP-Adresse angefallener Traffic in Megabyte



