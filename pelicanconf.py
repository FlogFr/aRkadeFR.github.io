#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'aRkadeFR'
SITENAME = 'Tech blog of aRkadeFR / 1Avis.fr'
# SITEURL = 'http://localhost:8000'
SITEURL = 'http://arkadefr.github.io'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None


# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('RSS', '/feeds/all.atom.xml'),
          )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/aRkadeFR'),
        ('github', 'http://github.com/aRkadeFR'),)

PATH = 'content'
STATIC_PATHS = ['images', ]

DEFAULT_PAGINATION = 10

THEME = './pelican-bootstrap3'

MARKUP = ('md')

FAVICON = '/images/favicon.png'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
