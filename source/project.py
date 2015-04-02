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
today = published.strftime('%-d. %B %Y').decode('utf-8')
release = published.strftime('%Y-%m-%d').decode('utf-8')
version = published.strftime('%Y-%m-%d').decode('utf-8')

orientation = 'portrait'
