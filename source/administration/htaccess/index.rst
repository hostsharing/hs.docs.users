========
htaccess
========

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Uwe Müller

:Date: |date|, |time|

Konfigurationen, die es ermöglichen das der Webserver Rechte anderer User erhalten kann, sind nicht erlaubt.
Dies betrifft folgende Funktionen: 



+-----------------------+
| Funktion              |
+=======================+
| Options FollowSymlink |
+-----------------------+
| Options +Index        | 
+-----------------------+
| Options -Index        |
+-----------------------+



