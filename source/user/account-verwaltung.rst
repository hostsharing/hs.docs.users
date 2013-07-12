==============
Userverwaltung
==============

:Authors: - Uwe Müeller
:Date: 2013-03-01

HSadmin WebFrontend
--------------------
Das Webfrontend ist unter (http:// ) zu erreichen. Eine Beschreibung zum Webfrontend findet sich
unter (http:// hsadmin webfrontend ).

HSadmin shell (CLI)
--------------------

User anlegen
------------

hsadmin --call user.add -s name=xyz-user --set password=12345 --set comment=example --set shell=/bin/bash


User update
------------

Beispiel: Änderung des Passwortes:
 
hsadmin --call user.update --where name=xyz00-user --set password=12345

User löschen
------------

hsadmin -c user.delete xyz00-test

User suchen
------------

hsadmin -c user.search

(http// hsadmin allg. cheetset)


Rechte des Paketadmins annehmen
-------------------------------

hsadmin -u hsh00-xyz -r xyz00 -c Befehl Parameter 


Identiätswechsel
-----------------
sudo -u xyz00-user -i
Der Paketadmin kann die Rechte eines seiner Paketuser annehmen, ohne dessen Passwort kennen zu müssen. 

sudo -u xyz00-user -s
Für Paketuser, die keine reguläre shell (z.B. "/bin/passwd") besitzen, kann der Paketadmin eine reguläre Shell bekommen. 

su xyz00-user
Regulären Benutzern ist ein Identitätswechel (z.B. zum Paketadmin) möglich, wenn das Passwort bekannt ist.

hsadmin -r hsh00-xyz -u xyz00 -c ...
Mit dem Mitgliedsaccount Rechte des Paketadmins annehmen. 
