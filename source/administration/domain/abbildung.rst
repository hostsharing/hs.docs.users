<proto>://<fqdn>/<path>

1. Virtual Host, der fqdn am genauesten entspricht.

2.a) Virtual Host == fqdn

  => root = htdocs (htdocs-ssl falls proto == https)

  b) Virtual Host != fqdn

  Suche in subs (subs-ssl falls proto == https) nach passender Sub-Domain

    a) gefunden
    
      => root = subs/subdomain (subs-ssl/subdomain falls proto == https)


    b) nicht gefunden

      htdocsfallbackfornotexistingsubs?

        a) ja

          => root = htdocs (htdocs-ssl falls proto == https)

        b) nein

          => 404

3.) path startet mit cgi-bin

  => root = cgi (cgi-ssl falls proto == https)

4.) path startet mit fastcgi-bin

  => root = fastcgi (fastcgi-ssl falls proto == https)

5.) path = noch nicht gematchter Teil des Pfades

6.) Existiert root + path im Dateisystem
  
  a) ja 
    => Auslieferung

  b) nein
    => 404

