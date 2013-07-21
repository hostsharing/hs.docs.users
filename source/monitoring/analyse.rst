=======
Analyse
=======

:Authors: - Christian Theune
          - Jens Vagelpohl
          - Michael Hierweck
          - Veit Schiele
:Date: 2013-07-21

Separater Client, der komplexere Auswertungen durchführen kann. Diese können
auf Basis von `Riemann <http://riemann.io/>`_ ’s Index und/oder aus
Langzeitdaten, die z.B. aus `logstash <http://logstash.net/>`_  kommen,
erstellt werden. S.a. :doc:`archivierung`.

Die Ergebnisse dieser Auswertungen können dann als Event wieder an Riemann
übergeben werden, sodass diese im Dashboard angezeigt werden können. Damit
kann das Riemann-Dashboard dann auch zum Monitoring von *business processes*
verwendet werden.

``riemann-actual``
------------------

`riemann-actual <https://bitbucket.org/gocept/riemann-actual>`_ ist ein
Hilfsprogramm für Tests höherer Ordnung, die auf dem aktuellen, von
`Riemann <http://riemann.io/>`_ erstellten Index, basieren. Dabei nutzt es
`Bernhard <https://github.com/banjiewen/bernhard>`_ als Python-Client für
Riemann.

Das Ziel von ``riemann-actual`` ist die Verwendung der Ergebnisse von
niedrigschwelligen Tests zum Erstellen von umfassenderen Berwertungen,   
die dann auch für Benachrichtigungen verwendet werden können. 

