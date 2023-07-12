AUTHOR = 'lysts'
SITENAME = 'lysts'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['posts']
ARTICLE_PATHS = ['posts'] 
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
THEME = 'theme'
DEFAULT_METADATA = {
        'status': 'draft',
        }

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = (
    ('about', '/pages/about.html'),
    )

MENUXTRA = (
    ('github', 'https://github.com/lysts'),
    )

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
