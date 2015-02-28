=============================
Verzeichnisebene Domain-Admin
=============================
Das Home-Verzeichnis des :doc:`Domain-Admins<../benutzer/domain-admin>` umfasst folgende Verzeichnisse:

+-----------------+-----------+--------+---------+----------------------------------------------------------------+
| Berechtigungen  | Nutzer    | Gruppe | Ordner  | Erläuterung                                                    |
+=================+===========+========+=========+================================================================+
| ` dr-xr-x--T `  | httpd     | xyz00  | doms    | Ablage der in diesem Web-Paket aufgeschaltenen Domains dieses Domain-Admin. |
+-----------------+-----------+--------+---------+----------------------------------------------------------------+
| ` drwx------ `  | xyz00-abc | xyz00  | Maildir | Mailordner des Domain-Admin.                                  |
+-----------------+-----------+--------+---------+----------------------------------------------------------------+


Unterhalb des Ordners *doms* findet sich für jede Domain ein weiterer Ordner mit dem Namen der Domain, zum Beispiel *example.com*, und darin befindet sich die Verzeichnisstruktur für die jeweilige Domain:


+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Berechtigungen | Nutzer    | Gruppe | Ordner      | Erläuterung                                                                                                                                   |
+================+===========+========+=============+===============================================================================================================================================+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | cgi         | Ablage externer Software zur Generierung dynamischer Webseiten in einem Webserver.                                                            |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | cgi-ssl     | Ablage externer Software zur Generierung dynamischer Webseiten, die verschlüsselt ausgeliefert werden (siehe auch :doc:`TLS</administration/tls/index>`). |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | fastcgi     | Ablage externer Software zur Generierung dynamischer Webseiten in einem Webserver.                                                            |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | fastcgi-ssl | Ablage externer Software zur Generierung dynamischer Webseiten, die verschlüsselt ausgeliefert werden (siehe auch :doc:`TLS</administration/tls/index>`). |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | htdocs      | Ablage für die Daten einer Webseite, wenn diese unverschlüsselt ausgeliefert werden soll.                                                     |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | subs        | Ablage für Sub-Domain aus htdocs, wenn diese unverschlüsselt ausgeliefert werden soll.                                                        |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | htdocs-ssl  | Ablage für die Daten einer Webseite, wenn diese verschlüsselt ausgeliefert werden soll (siehe auch :doc:`TLS</administration/tls/index>`). |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | subs-ssl    | Ablage für Sub-Domain aus htdocs-ssl, wenn diese verschlüsselt ausgeliefert werden soll.                                                      |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | etc         | Ablage für domaineigene Konfigurationsdateien (z.B. eigenes :doc:`Zonefile</administration/zonefile/index>`).                                 |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ` drwxr-xr-x ` | xyz00-abc |  xyz00 | var         | Ablage für Logfiles.                                                                                                                          |
+----------------+-----------+--------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+



