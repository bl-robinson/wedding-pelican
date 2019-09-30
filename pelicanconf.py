#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Ben Robinson'
SITENAME = 'Leah and Ben '
SITEDESCRIPTION = 'this is just an example page for the pelican-fh5co-marble theme.'

# plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = '../wedding-theme'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

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
      'en':'Leah And Ben',
    },
    'text': {
      'en': ' 14th April 2020',
    },
    'links': []
  }, {
    'image': '/images/hero/background-2.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'Skylark Fields Farm',
    'text': 'Shuckburgh Rd, Staverton, Daventry NN11 6JY',
    'links': []
  }
]

ABOUT = {
  'image': '/images/about/about.jpeg',
  'mail': 'benr@blrobinson.uk',
  # keep it a string if you dont need multiple languages
  'text': {"en": "If you need to contact us about anything, use these details."},
  'link': 'pages/contact.html',
  # the address is also taken for google maps
  'address': '25 Greenhill Road, Long Buckby, NN6 7PU',
  'phone': '+447593892972'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True

MD_EXTENSIONS = True
