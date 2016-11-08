===============
TLS Zertifikate
===============

Standardkonfiguration 
---------------------

Pro :doc:`aufgeschalteter Domaint<../../anleitung/domain>` ist ein Zertifikat möglich.

TLS-Inhalte werden durch die Verzeichnisse

* cgi-ssl
* fastcgi-ssl
* htdocs-ssl

von Nicht-TLS-Inhalten getrennt.

.. note::

        Hostsharing stellt ein TLS-Zertifikat für die Domain \*.hostsharing.net zur Verfügung, welches mit der Paketdomain xyz00.hostsharing.net genutzt werden kann. 
        Bei einer Nutzung abseits der Paketdomain muss das Zertifikat vom Browser explizit bestätigt werden, da das Zertifikat nicht zur aufgerufenen Domain passt.
         

Inhalt: 

.. toctree::       
        :maxdepth: 1                
         
        varianten 
        eigene-tls-zertifikate




