#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Karlie Vanes'
SITENAME = u"Karlie's Childminding Services"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './theme'

INDEX_SAVE_AS = 'blog.html'

PLUGIN_PATHS=['./plugins']
PLUGINS = ['assets']

ASSET_CONFIG=(
    ('less_bin', '/usr/bin/lessc'),
    ('less_run_in_debug', True)
)

ASSET_BUNDLES=(
    ('less', ['test.less'], {'filters': 'less'}),
)

DISPLAY_PAGES_ON_MENU=False

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
