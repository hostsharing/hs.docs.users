===========
Darstellung
===========

:Authors: - Christian Theune
          - Jens Vagelpohl
          - Michael Hierweck
          - Veit Schiele
:Date: 2013-07-21

Graphing
--------

Das Frontend `graphite-web <https://github.com/graphite-project/graphite-web>`_
scheint für unsere Zwecke nicht wirklich brauchbar: Es benötigt lokalen Zugriff
auf die Carbon-Caches, da es leider nicht remote über den Query-Port des
Carbon-Caches anfragt. Daher würde jeder Carbon-Cache ein Web-Frontend
benötigen und diese Web-Frontends müssten dann über einen sicheren Kanal
miteinander kommunizieren. Zudem würden diese Frontends gemeinsame
Memcache-Instanzen und eine gemeinsam genutzte Datenbank benötigen. Dies
verkompliziert das Szenario unseres Erachtens unnötig.

Alternativ zu ``graphite-web`` könnte eines der folgenden Module zum Einsatz
kommen:

- `graphiti <https://github.com/paperlesspost/graphiti>`_
- `graphene <https://github.com/jondot/graphene>`_
- `charcoal <https://github.com/cebailey59/charcoal>`_
- `gdash <https://github.com/ripienaar/gdash>`_,
  s.a. `R.I.Pienaar blog post
  <http://www.devco.net/archives/2011/10/08/gdash-graphite-dashboard.php>`_

- `tasseo <https://github.com/obfuscurity/tasseo>`_
- `etsy’s dashboard <https://github.com/etsy/dashboard>`_
- `Rickshaw <http://code.shutterstock.com/rickshaw/>`_
- `Descartes <https://github.com/obfuscurity/descartes>`_

Dashboard
---------

`Riemann <http://riemann.io/>`_

