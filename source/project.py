# -*- coding: utf-8 -*-
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import date

# General information about the project.
code = 'hsusers'
project = u'Benutzerhandbuch'
author = u'Hostsharing eG'

published = date.today()
copyright = u'2000-{year}, {author}'.format(year=published.year, author=author)
today = published.strftime('%-d. %B %Y')
release = published.strftime('%Y-%m-%d')
version = published.strftime('%Y-%m-%d')
