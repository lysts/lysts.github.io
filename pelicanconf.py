AUTHOR = 'lysts'
SITENAME = 'lysts'
SITEURL = 'https://lysts.xyz'

THEME = 'theme'
PATH = 'content'

#PAGE_PATHS = ['pages']
#ARTICLE_URL = '{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/archives.html'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%b %d %Y'
INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'

# SITEURL = 'http://localhost:8000'
# RELATIVE_URLS = True


MENUITEMS = (
     ('about', 'pages/about-me.html'),
     ('CV', 'pages/cv.html')
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
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# # Legal
# SITE_LICENSE = 'x'
# HOSTED_ON = {"name": "GitHub Pages", "url": "https://www.githubpages.io/"}

# # SEO
# SITE_DESCRIPTION = ("a theme for Pelican, originally created by lysts")
