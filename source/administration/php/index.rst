===
PHP
===

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|


PHP ist standardmäßig über FastCGI konfiguriert. Es findet sich in den Ordnern  ``fastcgi`` und ``fastcgi-ssl`` unterhalb des Domainordners eine phpstub-Datei, der Webserver liefert php-Dateien mit den
Rechten des Users aus.

Eigene PHP Konfiguration
------------------------

Im Ordner ``fastcgi`` oder ``fastcgi-ssl`` wird die Datei php.ini angelegt. 
In dieser Datei werden die Änderungen gegenüber den  Standardwerten eingetragen.

Eine Übersicht über die Standardwerte von PHP können unter ``/etc/php5/cgi/php.ini`` eingesehen werden.
