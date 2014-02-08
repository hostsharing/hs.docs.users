

Mailrouting-----------Von Extern eingehende E-Mails===========================



==Eingehende E-Mails, die von extern an bei Hostsharing aufgeschaltet

en Domains gesendet werden, werden von den redundant ausgelegten Maileingangservern * mailin1.hostsharing.net* mailin2.hostsharing.net* mailin3.hostsharing.netang





enommen.* Extern --> mailin(1,2,3)-->  xyz00.hostsharing.net --> IMA


P, POP3, WebmailAusgehende E-Mails==================Ausgehende E-





Mails von externen Nutzern können ausschließlich über ein Webpaket (xyz00.hostsharing.net) mit einer Authentifizierung über SMTP-Auth (Benutzername und Passwort) versand werden.   * SMTP/Webmail -->
xyz00.hosts

haring.net --> mailout(1,2,3) --> externWebanwendungen versenden E-Ma

ils über den lokalen Mailserver (``localhost``) * Webanwendung --> l

ocalhost --> mailout(1,2,3) --> extern



