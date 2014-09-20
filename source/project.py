# -*- coding: utf-8 -*-
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import date

# General information about the project.
code = 'hsdocs'
project = u'Hostsharing Handbuch für Anwender'
author = u'Hostsharing eG'
copyright = u'2010-{year}, {author}'.format(year=date.today().year, author=author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = date.today().strftime('%Y-%m-%d')
# The full version, including alpha/beta/rc tags.
release = date.today().strftime('%Y-%m-%d')
