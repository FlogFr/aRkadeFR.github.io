#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'aRkadeFR'
SITENAME = 'Programming under linux'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/aRkadeFR'),
        ('github', 'http://github.com/aRkadeFR'),)

DEFAULT_PAGINATION = 10

THEME = './pelican-bootstrap3'

MARKUP = ('md')

FAVICON = 'theme/images/favicon.png'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
