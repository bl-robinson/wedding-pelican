#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Ben Robinson'
SITENAME = 'Leah and Ben '
SITEDESCRIPTION = 'this is just an example page for the pelican-fh5co-marble theme.'
# SITEURL = 'http://localhost:8081'

# plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = '../wedding-theme'
# I18N_GETTEXT_LOCALEDIR = '../pelican-fh5co-marble/locale/'
# I18N_GETTEXT_DOMAIN = 'messages'
# I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/London'
# DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
# I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']

# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.svg'

# special content
HERO = [
  {
    'image': '/images/hero/background-1.jpg',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'Some special content',
    },
    'text': {
      'en': 'Any special content you want to tease here',
    },
    'links': [
      {
        'icon': 'icon-code',
        'url': 'https://github.com/claudio-walser/pelican-fh5co-marble',
        'text': 'Github'
      }
    ]
  }, {
    'image': '/images/hero/background-2.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'Uh, special too',
    # keep it a string if you dont need multiple languages
    'text': 'Keep hero.text and hero.title a string if you dont need multilanguage.',
    'links': []
  }, {
    'image': '/images/hero/background-3.jpg',
    'title': 'No Blogroll yet',
    'text': 'Because of space issues in the man-nav, i didnt implemented Blogroll links yet.',
    'links': []
  }, {
    'image': '/images/hero/background-4.jpg',
    'title': 'Ads missing as well',
    'text': 'And since i hate any ads, this is not implemented as well',
    'links': []
  }
]

ABOUT = {
  'image': '/images/about/about.jpeg',
  'mail': 'info@gitcd.io',
  # keep it a string if you dont need multiple languages
  'text': {
    'en': 'Learn more about the creator of this theme or just drop a message.',
  },
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Zürich, Schweiz',
  'phone': '+555-shoe'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
# PAGE_ORDER_BY = 'order'

# setup google maps
GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'
