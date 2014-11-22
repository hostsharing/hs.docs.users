===================
Webspace einrichten
===================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Michael Hierweck
          - Uwe Müller
          - Christian Günter
          - Veit Schiele
:Date: |date|, |time|

Ordnerstruktur
==============

Im folgenden die exemplarische Struktur des Home-Verzeichnisses eines Domain-
Admins::

    ├── doms
    │   ├── domain1.tld
    │   │   ├── app
    │   │   ├── app-ssl
    │   │   ├── cgi
    │   │   │   └── test.cgi
    │   │   ├── cgi-ssl -> cgi
    │   │   ├── etc
    │   │   │   └── pri.domain1.tld
    │   │   ├── fastcgi
    │   │   │   └── phpstub
    │   │   ├── fastcgi-ssl -> fastcgi
    │   │   ├── htdocs
    │   │   │   └── .htaccess
    │   │   ├── htdocs-ssl
    │   │   │   └── .htaccess
    │   │   ├── subs
    │   │   │   ├── example
    │   │   │   ├── pri.domain1.tld
    │   │   │   └── www
    │   │   ├── subs-ssl
    │   │   │   └── www
    │   │   └── var
    │   │       ├── config.err
    │   │       └── handles.domain1.tld
    │   └── domain2.tld
    │       ├── app
    │       └── …
    ├── Maildir
    ├── procmail.log
    ├── vacation.cache
    └── vacation.msg

``~/doms``
    Alle von Ihnen bestellten Domains liegen im Verzeichnis ``doms``.

    ``~/doms/domain1.tld``
        ``domain1`` steht für eine beliebige Domain und ``tld`` für eine beliebige top level domain z.B.
        ``com``, ``net``, ``org``, ``de``.
    ``~/doms/domain1.tld/app``
        Dieses Verzeichnis ist als ``PassengerAppRoot`` des Apache-Webserver-Moduls `Phusion Passenger
        <https://www.phusionpassenger.com/>`_ konfiguriert. 
    ``~/doms/domain1.tld/app-ssl``
        Auch dieses Verzeichnis ist als ``PassengerAppRoot`` des Apache-Webserver-Moduls konfiguriert.
    ``~/doms/domain1.tld/cgi``
        Dies ist das Basisverzeichnis für CGI-Skripte. Ein Alias bildet HTTP-Requests auf ``/cgi-bin/`` für
        alle Zugriffe auf den Virtual Host auf dieses Verzeichnisses ab.
    ``~/doms/domain1.tld/cgi-ssl``
        Dies ist in der Standardkonfiguration ein symbolischer Link auf ``~/doms/domain1.tld/cgi``.
    ``~/doms/domain1.tld/etc``
        Dieses Verzeichnis enthält Dateien für die Konfiguration der Domain wie etc.
    ``~/doms/domain1.tld/fastcgi``
        Dies ist das Basisverzeichnis für FastCGI-Skripte. Ein Alias bildet HTTP-Requests auf
        ``/fastcgi-bin/`` für alle Zugriffe auf den Virtual Host auf dieses Verzeichnis ab.
    ``~/doms/domain1.tld/htdocs``
        Dieses Verzeichnis ist als ``DocumentRoot`` des Apache Webserver konfiguriert. 

        Es dient auch zur Aufnahme statischer Inhalte im Zusammenhang mit der Nutzung von Phusion Passenger
        zur Auslieferung der statischen Dateien.

        ``~/doms/domain1.tld/htdocs/.htaccess``
            In der Standardkonfiguration enthält diese Datei die Weiterleitung auf die ``www``-Subdomain::

                Redirect permanent / http://www.domain1.tld/

            Die verwendeten Regeln werden auf **alle** Subdomains von ``domain1.tld`` aus. In der
            ``.htaccess`` können

            - eigene Fehlerseiten definiert,
            - MIME-Typen zugewiesen,
            - Passwortschutz eingerichtet,
            - Weiterleitungen durchgeführt werden. 

    ``~/doms/domain1.tld/subs``
        Dieses Verzeichnis enthält alle Subdomains. Hier findet sich auch die Subdomain *www.domain1.tld*.

        ``~/doms/domain1.tld/subs/example``
            Dies ist ein Beispiel für eine Subdomain, die Sie einfach selbst anlegen können. Sie müssen hierzu
            nur ein Verzeichnis anlegen und anschließend die Dateien in das Verzeichnis übertragen.
        ``~/doms/domain1.tld/subs/pri.domain1.tld``
            Mit dieser Datei können Sie ein Zonendatei für Ihre Domain selbst verwalten. Damit können z.B.
            einzelne Subdomains auf andere Server umgeleitet, eigene Mailserver angesprochen werden etc.
        ``~/doms/domain1.tld/subs/www``
            Dieses Verzeichnis wird automatisch angelegt und üblicherweise vom Webserver angesprochen, wenn
            keine Subdomain explizit genannt wird (also ``http://domain1.tld`` verweist üblicherweise auf
            ``http://www.domain1.tld``).

    ``~/doms/domain1.tld/var``
        in diesem Verzeichnis liegen die Log-Dateien z.B. 

        ``config.err``
            Konfigurationsfehler 
        ``web.err``
            http-Fehlermeldungen

Zugangsdaten und Einstellungen
==============================

Um Dateien in das Webpaket kopieren zu können, wird eine Client-Software
benötigt (z.B. FileZilla, WinSCP oder :term:`SCP`).

Server:   xyz00.hostsharing.net

Benutzer: xyz00-doms

Passwort: PASSWORT

z.B.: FTP FileZilla Client Software

.. image:: ftp-filezilla.jpg

Wechsel in den Ordner *www*:

.. image:: ftp-filezilla-www.jpg

