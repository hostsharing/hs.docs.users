=================
E-Mail einrichten
=================

.. |date| date:: %d.%m.%Y
.. |time| date:: %H:%M

:Authors: - Michael Hierweck
          - Uwe Müller
          - Christian Günter
:Date: |date|, |time|

Wir legen nun zwei E-Mail-Adressen an.
Die erste wird an ein Postfach bei Hostsharing zugestellt und die zweite wird an eine externe E-Mail-Adresse weiter geleitet.

E-Mail-Adresse an Postfach bei HS
---------------------------------

Wir melden uns unter https://admin.hostsharing.net als Domain-Admin (xyz00-doms) an:

.. image:: login-domainadmin.jpg

Anschließend aktivieren wir den Tab *EMail Adressen* und sehen folgende Abbildung.

.. image:: email-domainadmin.jpg

Beim Domain bestellen werden per default die drei sichtbaren E-Mail-Adressen automatisch angelegt. (abuse@ postmaster@ und webmaster@)

Mit dem Button *EMail-Adresse anlegen* erhalten wir die folgende Maske:

.. image:: email-adresse-anlegen.jpg

Die Felder im einzelnen:

lokaler Teil: info (der Name vor dem @ Zeichen)

Sub-Domain:   bleibt hier leer da wir direkt für FQD eine E-Mail-Adresse anlegen

Haupt-Domain: hs-example.de

Ziel:         User (da die E-Mail-Adresse an ein Postfach gehen soll)  xyz00-doms

E-Mail-Adresse mit Weiterleitung an externe Mail-Adresse
--------------------------------------------------------

Um eine neue E-Mail-Adresse anzulegen die an eine andere (fremde) Mail-Adresse weiter geleitet wird, wird in der Maske bei:
Ziele: *EMail* ausgewählt und dahinter dann die externe Mail-Adresse im Bsp webmaster@web-panel.com

.. image:: email-adresse-extern-anlegen.jpg

Unsere Liste der Mail Adressen sieht nun so aus:

.. image:: email-adresse-liste.jpg
