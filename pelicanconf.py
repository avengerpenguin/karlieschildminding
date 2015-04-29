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

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './theme'

INDEX_SAVE_AS = 'blog.html'

PLUGIN_PATHS=['./plugins']
PLUGINS = ['gallery.gallery', 'thumbnailer']


STATIC_PATHS = ['extra/CNAME', 'files', 'images']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    }


IMAGE_PATH='images/gallery'
THUMBNAIL_DIR='images'
THUMBNAIL_SIZES={
    'thumbnails': '134x120',
}
THUMBNAIL_KEEP_NAME=True
