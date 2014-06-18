=========
Allgemein
=========

:Authors: - Uwe Müller


.. |date| date:: %d. %m. %Y
.. |time| date:: %H:%M


Standardkonfiguration 
=====================

Pro Webpaket ist ein Zertifikat möglich.

SSL-Inhalte werden durch die Verzeichnisse

* cgi-ssl
* fastcgi-ssl
* htdocs-ssl

von Nicht-SSL-Inhalten getrennt.

   .. note::

        Hostsharing stellt ein SSL-Zertifikat für die Domain *.hostsharing.net zur Verfügung das mit der Paketdomain xyz00.hostsharing.net genutzt werden kann.
        Bei einer Nutzung abseits der Paketdomain muss das Zertifikat vom Browser explizit bestätigt werden, da das Zertifikat nicht zur aufgerufenen Domain passt.
