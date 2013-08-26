===
SSL
===

:Authors: - Uwe Müeller
:Date: 2013-03-01

Standardkonfiguration 
=====================

Pro Webpaket ist ein Zertifikat möglich.

SSL-Inhalte werden durch die Verzeichnisse

- cgi-ssl
- fastcgi-ssl

  - htdocs-ssl

von Nicht-SSL-Inhalten getrennt.

.. note::
        Hostsharing stellt ein SSL-Zertifikat für die Domain *.hostsharing.net zur Verfügung das mit der Paketdomain xyz00.hostsharing.net genutzt werden kann.  Bei einer Nutzung abseits der Paketdomain muss das Zertifikat vom Browser explizit bestätigt werden, da das Zertifikat nicht zur aufgerufenen Domain passt.
::


Mögliche Varianten
==================

SSL-Seiten und Nicht-SSL Seiten in einem Verzeichnis 
----------------------------------------------------

Sollen SSL und Nicht-SSL Seiten innerhalb eines Verzeichnis verwaltet werden, können die SSL-Verzeichnisse gelöscht und
Symbolische Links auf Nicht-SSL Verzeichnisse angelegt werden. Dies gilt selektiv auch für Unterverzeichnisse. Symbolische Links erlauben es Seiten mit und ohne SSL abzurufen. 

Automatisch auf SSL
-------------------

Soll nur auf bestimmten Seiten der Zugriff mit SSL erlaubt und automatisch auf SSL umschaltet werden, muss dies in einer entsprechenden .htaccess Datei für die betroffenen Verzeichnisse konfiguriert werden. 


Eigene SSL Zertifikate 
======================

Für die Installation eigener Zertifikate einer Zertifizierungsstelle muss der Paketadmin einen "Private Key" und einen CSR  (Certificate Signing Request) erzeugen. 
Die Vorgehensweise ist in der Regel auf den Webseiten der Zertifizierungsstelle beschrieben. Weitere Hinweise sind im Hostsharing Wiki beschrieben (http:// HS-wiki ssl).
(Anmerkung: Existiert ein "Standard" in welchem Ordner wo die pem Datei im Paket gespeichet werden sollte (Apache, Paketadmin, User? / xyz00.pem,  xyz00.chain.pem)

Für die Aktivierung des Zertifikates wird ein Auftrag an service@hostsharing.net mit der Bitte um Aktivierung gesendet.
