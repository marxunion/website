# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime


SITENAME = "Союз марксистов"
SITESUBTITLE = ""
AUTHOR = SITENAME
SITEURL = ""
DEFAULT_LANG = "ru"
DEFAULT_DATE = "fs"

# Photo Gallery plugin
# PHOTO_LIBRARY = "gallery-source/"
# PHOTO_GALLERY = (1024, 768, 80)
# PHOTO_ARTICLE = (760, 506, 80)
# PHOTO_THUMB = (192, 144, 60)
# PHOTO_SQUARE_THUMB = False
# PHOTO_RESIZE_JOBS = 5
# PHOTO_WATERMARK = True
# PHOTO_WATERMARK_TEXT = SITENAME
# PHOTO_WATERMARK_IMG = ""
# PHOTO_EXIF_KEEP = False
# PHOTO_EXIF_REMOVE_GPS = True
# PHOTO_EXIF_COPYRIGHT = "CREATIVE COMMONS"

DIRECT_TEMPLATES = ["index", "join", "tags", "categories", "archives", "404"]
PAGINATED_TEMPLATES = {"index": 2}
INDEX_SAVE_AS = 'index.html'
OUTPUT_PATH = 'output'

PATH = "content"
STATIC_PATHS = ['content/posts', 'content/pages']
ARTICLE_PATHS = ['content/posts']
PAGE_PATHS = ['content/pages']
PATH_METADATA = 'pages/(?P<path>.*)\..*'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

STATIC_EXCLUDES = ['plugins', 'theme', 'output']
PAGE_EXCLUDES = STATIC_EXCLUDES
ARTICLE_EXCLUDES = STATIC_EXCLUDES
THEME = "theme"

TIMEZONE = "Europe/Moscow"

# Put full text in RSS feed
RSS_FEED_SUMMARY_ONLY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss"
TRANSLATION_FEED_ATOM = "feeds/{lang}.atom.xml"
TRANSLATION_FEED_RSS = "feeds/{lang}.rss"
AUTHOR_FEED_ATOM = "feeds/{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/{slug}.rss"
TAG_FEED_ATOM = "feeds/tag_{slug}.atom.xml"
TAG_FEED_RSS = "feeds/tag_{slug}.rss"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "i18n_subsites",
    "extract_toc",
    "page_hierarchy",
    "search"
]

# Localization
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Marxunion',
        'SITESUBTITLE': '',
        'TIMEZONE': 'Europe/London',
        'OUTPUT_PATH': 'output/en'
    },
    'de': {
        'SITENAME': 'Marxunion',
        'SITESUBTITLE': '',
        'TIMEZONE': 'Europe/Berlin',
        'OUTPUT_PATH': 'output/de'
    }
}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight",
                                           "linenums": True},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"permalink": "true"},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STORK_INPUT_OPTIONS = {
    "base_directory": ".",
    "url_prefix": SITEURL,
    "stemming": "Russian"
}

SITE_UPDATED = datetime.date.today()
