# -*- coding: utf-8 -*-
#
# These project configuration settings override the defaults
# provided by defaults.py.

from defaults import *

from datetime import date
from locale import getpreferredencoding


# General information about the project.

code = 'hsusers'
project = u'Benutzerhandbuch'
author = u'Hostsharing eG'
published = date.today()
orientation = 'portrait'


# Calculated copyright, release and versioning information.

copyright = u'2000-{year}, {author}'.format(year=published.year, author=author)
today = published.strftime(u'%-d. %B %Y').decode(getpreferredencoding())
release = published.strftime(u'%Y-%m-%d').decode(getpreferredencoding())
version = published.strftime(u'%Y-%m-%d').decode(getpreferredencoding())


# Project specific customization.
