==================
Postausgangsserver
==================

Für jedes Webpaket steht ein Postausgangsserver für reguäre E-Mails
und ein Postausgangsserver für den Massenversand von E-Mails bereit.

Unter Massenversand wird der Versand von Newslettern, Forenbenachrichtungen,
der Betrieb von Mailinglisten und ähnliche Nutzungen verstanden
im Rahmen des Zulässigen verstanden.


Angaben für den Postausgangsserver:

+-----------------------+-----------------------+-----------+---------------+--------------+
| Postausgangsserver    | Postfach/Benutzername | Protokoll | Port STARTTLS | Port SSL/TLS |
+=======================+=======================+===========+===============+==============+
| xyz00.hostsharing.net | xyz00-mailbox         | SMTP      | 587 oder 25   | 465          |
+-----------------------+-----------------------+-----------+---------------+--------------+

Die Konfigurationsvariante SMTP über Port 587 mit STARTTLS wird empfohlen.


Angaben für den Postausgangsserver für den Massenversand:

+-----------------------+-----------------------+-----------+---------------+--------------+
| Postausgangsserver    | Postfach/Benutzername | Protokoll | Port STARTTLS | Port SSL/TLS |
+=======================+=======================+===========+===============+==============+
| xyz00.hostsharing.net | xyz00-mailbox         | SMTP      | 487 oder 4025 | 465          |
+-----------------------+-----------------------+-----------+---------------+--------------+

Die Konfigurationsvariante SMTP über Port 4587 mit STARTTLS wird empfohlen.
