AUTHOR = 'lysts'
SITENAME = 'lysts'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['posts'] 
THEME = 'theme'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = (
    ('about', '/pages/about.html'),
    ('posts', '/posts.html'),
    ('github', 'https://github.com/lysts'),
    ('cv', '"https://drive.google.com/file/d/1qM2QVLAN3qGenRw3dmDLyhvCo    Lo2h06N/view?usp=sharing')
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