===========================
hsadmin Command-Line-Client
===========================

:Authors: - Uwe Müeller
:Date: 2013-03-01

Das Kommandozeilen-Programm ist dabei generisch für alle zu verwaltenden Module. 
userName=xyz00
passWord=geheim
passWord.xyz00=geheim
passWord.hsh00-xyz=geheim

Test:
hsadmin -c modules.version


hsadmin -c modules.search

hasadmin -c q.search

Lokal Installieren:
/usr/local/bin/hsadmin
/usr/local/lib/hostsharing/hsadmin/HSadminCLI.jar

Grundaufbau:
hsadmin LOKALE-OPTIONEN GLOBAL-REMOTE-OPTIONEN MODUL.FUNKTION REMOTE-OPTIONEN OIDS ...

lokale Optionen  Bedeutung

-u/ --user	Unix-Usernamen
-V/ --version	Versionsnummer des hsadmin cli-client
- 		liest Parameter von stdin ein

-c --call	Einleitung Funktionsaufruf

-w /--where:feld=wert Wertabfrage eines Feldes
-s  --set Setzt einen Wert
-d  --display	Spezifiziert das Ausgabeformat 

OIDS 		 Objekt-Identifier

User anlegen
------------

hsadmin - <<EOF
--call:user.add
--set:password=...
--set:name=xyz00-test
--set:shell=/bin/bash
EOF

Unterschied Kurz/lanform erklären. Im folgendem wird die Langform der Optionen (--set: statt -s) und ein temporäres Respose-File verwendet. Durch eingabe der Optionen in das Response-File landet das Passwort nicht in der Kommando-Zeile und damit in der Prozessliste - wo es alle einsehen könnten.
Im Response-File muss exakt ein Parameter je Zeile angegeben werden. 

kurzform ....

Bedeutung der Datenfelder

Feld	    Beschreibung
name:	    Der Login-Name .Der Name muss IMMER mit der Paket-ID + '-' anfangen, also z.B. xyz00-otto. Ein "-" im Namen ist nur direkt hinter dem Paket erlaubt. Als Trenner kann ein Punkt (.) verwendet werden. Der Name kann nachträglich nicht geändert werden.
id:	        ID für die interne Verwaltung; vorgegeben.
comment:	Hier kann man den realen Namen des Users eintragen, also z.B. "Otto Meier". (Auf neu aufgeschalteten Domains erscheint dieses Feld bei "Diese neue Website wurde gerade bei der Hostsharing eG für ... eingerichtet".)
password:	Leer, das Passwort wird nicht angezeigt.
pac:	    Paketname; vorgegeben
hivename:	ID des hives [http:// HS-Glossar, hs-technik]], auf dem sich Paket und User befinden. Kann nicht geändert werden.
userid:	    ID für die interne Verwaltung; vorgegeben.
shell:	    Dieses Feld enthält den kompletten Pfad der Login-Shell. Es sind nur wenige Shells möglich, i.d.R. wird man hier /usr/bin/passwd (damit kann der Domainuser sein Passwort jederzeit per ssh oder telnet beliebig ändern) /bin/bash (für vollen ssh/telnet-Zugang) oder /bin/badsh (für FTP-only) setzen. Man kann auch z.B. bin/false angeben, dann kann der User selbst gar nichts machen (außer FTP usw. natürlich)
homedir:	Das Homedirectory des Users; wird automatisch gesetzt.



Die Datenfelder name, comment und shell mit ":" getrennt ausgeben:
 hsadmin -c user.search -d '${name}:${comment}:${shell}\n'

