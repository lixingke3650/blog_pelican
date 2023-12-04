# python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hanbin'
SITENAME = 'lixingke3650'
SITEURL = 'http://192.168.56.101:55180/blog/preview'

# PATH = 'content'
#FEED_DOMAIN = 'static'
#ARTICLE_URL = 'static'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'http://github.com/lixingke3650/'
DISQUS_SITENAME = 'lixingke3650-githubblog'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('MyGitHub', 'https://github.com/lixingke3650/'))

SOCIAL = (('github', 'http://github.com/lixingke3650'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# code blocks with line numbers
# PYGMENTS_RST_OPTIONS = {'linenos': 'inline'} # {'linenos': 'table'}  {'linenos': 'none'}
# PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# OUTPUT_PATH = '/root/home/hanbin/web/MySite/blog/'
# OUTPUT_PATH = 'lixingke3650.github.io/output'
OUTPUT_PATH = './preview/blog'

DISPLAY_PAGES_ON_MENU = 0
DISPLAY_CATEGORIES_ON_MENU = 1

THEME = './themes/elegant'

# For Elegant theme
HOSTED_ON = {
    "name": 'Lixingke3650',
    "url": 'http://192.168.56.101:55180'
}

LANDING_PAGE_TITLE = "Welcome to lixingke3650's personal blog!"
