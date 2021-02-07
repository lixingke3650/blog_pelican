# python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hanbin'
SITENAME = 'lixingke3650'
SITEURL = 'http://127.0.0.1/blog'

# PATH = 'content'
#FEED_DOMAIN = 'static'
#ARTICLE_URL = 'static'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'jp'

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
OUTPUT_PATH = './html/'

DISPLAY_PAGES_ON_MENU = 0
DISPLAY_CATEGORIES_ON_MENU = 1

THEME = './themes/elegant'

# For Elegant theme
HOSTED_ON = {
    "name": 'Lixingke3650',
    "url": 'http://133.167.106.55'
}

LANDING_PAGE_TITLE = "Welcome to lixingke3650's personal blog!"

PROJECTS = [
    {
        'name': 'OrTunnel',
        'url': 'hhttps://github.com/lixingke3650/OrTunnel',
        'description': 'Secure data transmission on Ethernet',
    },
    {
        'name': 'OrHttpConnect',
        'url': 'https://github.com/lixingke3650/OrHttpConnect',
        'description': 'Network breakthrough over HTTP proxy',
    },
    {
        'name': 'ORRO',
        'url': 'https://github.com/lixingke3650/ORRO',
        'description': 'HTTP Proxy for Python, can be deployed on cloud server',
    },
    {
        'name': 'OrWG',
        'url': 'https://github.com/lixingke3650/OrWG',
        'description': 'Fast, modern, secure kernel VPN tunnel, forks from WireGuard',
    },
    {
        'name': 'OrWG-Go',
        'url': 'https://github.com/lixingke3650/OrWG-Go',
        'description': 'Fast, modern, secure kernel VPN tunnel - Go Implementation, forks from WireGuard',
    },
    {
        'name': 'OrWG-tools',
        'url': 'https://github.com/lixingke3650/OrWG-tools',
        'description': 'tools for configuring OrWG and OrWG-Go, forks form WireGuard',
    },
    {
        'name': 'blog_pelican',
        'url': 'https://github.com/lixingke3650/blog_pelican',
        'description': 'My static blog powered by Pelican',
    },
    {
        'name': 'OrWebSite',
        'url': 'https://github.com/lixingke3650/OrWebSite',
        'description': 'My web site powered by Django',
    },
]
