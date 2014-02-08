===========
E-Mailalias
===========

:Authors: - Uwe Müeller
:Date: 2013-03-01

Ein E-Mailalias ist eine E-Mailadresse zur Weiterleitung von E-Mails.

An email alias is simply a forwarding email address. The term alias expansion is sometimes
used to indicate a specific mode of email forwarding, thereby implying a more generic
meaning of the term email alias as an address that is forwarded in a simplistic fashion.


E-Mailalias hinzufügen
----------------------

hsadmin --call:emailalias.add --set:name=xyz00-test --set:target='test@example.org'
 

Ziel eines E-Mailalias ändern
-----------------------------

hsadmin --call:emailalias.update --set:target='dummy@example.org' xyz00-test 


E-Mailalias löschen
-------------------
hsadmin --call emailalias.delete xyz00-test


E-Mailalias suchen
-------------------

hsadmin --call emailalias.search

Der Aufruf sucht nach vorhandenen E-Mailalias und gibt folgende Informationen
aus:

name		Name des E-Mailaliases      
id 		ID des HSadmin Auftrages
target          Ziel der Weiterleitung
hivename        Name des Hives
pac    		Name des Paketes

