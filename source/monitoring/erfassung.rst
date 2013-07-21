=========
Erfassung
=========

:Authors: - Christian Theune
          - Jens Vagelpohl
          - Michael Hierweck
          - Veit Schiele
:Date: 2013-07-21

Statistiken
-----------

System
``````

`collectd  <http://collectd.org/>`_ 
 The system statistics collection daemon

Installation
::::::::::::

::

 $ apt-get install collectd

Konfiguration
:::::::::::::

::

 $ vim /etc/collectd.conf

Die folgenden Absätze sollten auskommentiert werden::

 LoadPlugin write_graphite
 …
 <Plugin write_graphite>
  <Carbon>
   Host "localhost"
   …

Schließlich kann der Dienst neu gestartet werden mit::

 $ /etc/init.d/collectd restart

Netzwerk
````````

`statsD  <https://github.com/etsy/statsd/>`_ 
 A network daemon listens for statistics

Events
------

`Scales <https://github.com/Cue/scales>`_
`````````````````````````````````````````

Installation
::::::::::::

::

 $ python2.7 virtualenv scales_env
 $ cd scales_env
 $ ./bin/easy_install scales
 $ ./bin/easy_install flask


Beispiel
::::::::

Ein einfaches Beispielskript für ``scales`` kann z.B. folgendermaßen aussehen::

 from greplin import scales

 STATS = scales.collection('/web',
             scales.IntStat('errors'),
             scales.IntStat('success'))

 # In a request handler

 STATS.success += 1
 import logging
 logging.basicConfig(level=0)

 import greplin.scales.flaskhandler as statserver
 statserver.serveInBackground(8765, serverName='something-server-42')
 from greplin.scales import graphite
 pusher = graphite.GraphitePeriodicPusher('127.0.0.1', 2003, period=1)
 pusher.allow('*')
 pusher.start()

 import random
 import time
 while True:
     time.sleep(1)
     STATS.success = random.randint(1,10)
     print STATS.success

Der Aufruf des Skripts erfolgt dann mit::

 $ ./bin/python scales.py

