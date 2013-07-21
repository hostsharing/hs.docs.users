============
Verarbeitung
============

:Authors: - Christian Theune
          - Jens Vagelpohl
          - Michael Hierweck
          - Veit Schiele
:Date: 2013-07-21

`Riemann <http://riemann.io/>`_ aggregiert Events von Servern und Anwendungen.

Installation
------------

::

 $ wget http://aphyr.com/riemann/riemann-0.2.1.tar.bz2
 $ tar xvjf riemann-0.2.1.tar.bz2

Riemann-Desktop-Package
~~~~~~~~~~~~~~~~~~~~~~~

#. ::

    $ apt-get install ruby1.9.1-dev
    $ mkdir -p riemann-desktop/gems
    $ cd riemann-desktop
    $ gem install --install-dir ./gems/ riemann-client riemann-tools riemann-dash

#. Nun können Sie im Browser folgende Adresse aufrufen:
   ``http://localhost:4567``.
#. Mit ``e`` erhalten Sie eine Editieransicht, in der Sie z.B. ``Grid`` und als
   Query ``true`` eingeben können. Damit werden Ihnen die Events aus
   ``scales.py`` angezeigt.

Konfiguration
-------------

::

 $ cd riemann/etc
 $ vim riemann.config

Öffenen des Port 2003 für das graphite-Orotokoll::

 (let [host "127.0.0.1"]
 …
 (graphite-server :host host))


Testing
-------

Riemann ist auch gut geeignet für Test-Driven Development. Siehe hierzu z.B.
die Riemann-Konfiguration des Guardian: `Testing changes
<https://github.com/guardian/riemann-config/blob/master/README.md#testing-changes>`_.
Dabei ist die wichtigste Anlaufstelle `main.clj
<https://github.com/guardian/riemann-config/blob/master/main.clj>`_ für
Initialisierung und Protokollierung.

