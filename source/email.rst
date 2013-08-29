======
E-Mail
======

:Authors: - Uwe Müeller
:Date: 2013-03-01

Allgemein
---------
Jeder User-Account besitzt ein E-Mail-Konto und kann E-Mail empfangen und senden. E-Mails werden unterhalb des Verzeichnisses ``~/Maildir abgelegt``. Der Name des Ordners ``Maildir`` kann nicht verändert werden.
Jedes E-Mail-Konto ist POP3 und IMAP fähig. 

Hostsharing bietet folgende Konfigurationsmöglichkeiten:

- Anlegen und Löschen von E-Mailadressen
- Anlegen und Löschen von E-Mailaliasen
- Einrichtung von Weiterleitungen
- Automatisches Versenden einer E-Mail-Bestätigung (Vacation)
- Automatisches Filtern und Bearbeiten von E-Mails über Managesieve (http://wiki.managesieve) oder procmail (http:// wiki.procmail). 
- Mit Aliasen kann die Zustellung von Nachrichten in die Postfächer der Benutzer gesteuert werden.
- E-Mailkonten bei anderen Anbietern abfragen ( http://wiki.fetchmail).
- Es können Mailinglisten eingerichtet werden.


Der Zugriff auf das Mailkonto erfolgt über einen beliebigen E-Mailclient oder über das zentral installierte `Webmail <http://webmail.hostsharing.net>`_ . 
Informationen zum installierten Webmailclient und zur Einrichtung findet im Wiki der Mitglieder: `Roundcube <https://wiki.hostsharing.net/index.php?title=Webmail>`_ . 

Posteingangsserver
------------------

			    SSL	 STARTTLS     ungesichert
xyz00.hostsharing.net  POP3 995  -            110
		       IMAP 993  443          143
		       
Postausgangsserver
------------------

                            SSL   STARTTLS    ungesichert
xyz00.hostsharing.net  POP3 465    25 ?       25 
                       IMAP 465    25 ?	      25 ?          


E-Mailalias und Paketuser
-------------------------

Ein E-Mailalias in der E-Mailkonfiguration gleichen Namens wie ein Paketuser mit Mailbox hat Vorrang vor einem 
Paketuser gleichen Namens. Implementiert der E-Mailalias eine Weiterleitung, gehen in diesem
Fall in der Mailbox des Paketusers  keine E-Mails ein. 


Größenbeschränkung einer E-Mail
--------------------------------

Unsere Mail-Server akzeptieren E-Mails bis zu einer maximalen Größe von 128 MB,
Dateianhänge sollten daher die Größe von ca. 90 MB nicht überschreiten. 
(http:// wiki-größenbeschränkung email).


Mailrouting
===========

Von extern eingehende E-Mails
-------------------------
Eingehende E-Mails, die von extern an bei Hostsharing aufgeschalteten Domains  
gesendet werden, werden von den redundant ausgelegten Maileingangservern 

* mailin1.hostsharing.net
* mailin2.hostsharing.net
* mailin3.hostsharing.net

angenommen.

[Bild-Skizze: Extern --> mailin(1,2,3)--> xyz00.hostsharing.net --> IMAP, POP3, Webmail)

Ausgehende E-Mails
------------------

Ausgehende E-Mails von externen Nutzern können ausschließlich über die Webpakete (xyz00.hostsharing.net) mit
der Authentifizierung über SMTP Auth (Benutzername und Passwort) versand werden.   

[Bild-Skizze: SMTP/Webmail --> xyz00.hostsharing.net --> mailout(1,2,3)] --> extern

Webanwendungen versenden E-Mails über den lokalen Mailserver (localhost) 

[Bild-Skizze: Webanwendung --> localhost --> mailout(1,2,3) --> extern


