Mögliche Varianten
==================

:Authors: - Uwe Müller

.. |date| date:: %d. %m. %Y
.. |time| date:: %H:%M

   
SSL-Seiten und Nicht-SSL Seiten in einem Verzeichnis 
----------------------------------------------------

Sollen SSL und Nicht-SSL Seiten innerhalb eines Verzeichnis verwaltet werden, können die SSL-Verzeichnisse gelöscht und
Symbolische Links auf Nicht-SSL Verzeichnisse angelegt werden. Dies gilt selektiv auch für Unterverzeichnisse. 
Symbolische Links erlauben es Seiten mit und ohne SSL abzurufen. 

Automatisch auf SSL
-------------------

Soll nur auf bestimmten Seiten der Zugriff mit SSL erlaubt und automatisch auf SSL umschaltet werden, muss dies in einer 
entsprechenden .htaccess Datei für die betroffenen Verzeichnisse konfiguriert werden. 

