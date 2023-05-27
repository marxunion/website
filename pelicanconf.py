# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

# THINGS TO CONFIGURE
# ---------------------------------------------------------------------

SITENAME = "Союз марксистов"
SITESUBTITLE = ""
AUTHOR = SITENAME
SITEURL = ""
DEFAULT_LANG = "ru"
DEFAULT_DATE = "fs"

# Photo Gallery plugin
PHOTO_LIBRARY = "gallery-source/"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = SITENAME
PHOTO_WATERMARK_IMG = ""
PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True
PHOTO_EXIF_COPYRIGHT = "CREATIVE COMMONS"

# ONLY TOUCH IF YOU KNOW WHAT YOU'RE DOING!
# ---------------------------------------------------------------------
DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "404")
INDEX_SAVE_AS = 'index.html'

PATH = "content"
STATIC_PATHS = ['content/posts', 'content/pages']
ARTICLE_PATHS = ['content/posts']
PAGE_PATHS = ['content/pages']

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
    "sitemap",
    "extract_toc",
    "liquid_tags.img",
    "neighbors",
    "render_math",
    "related_posts",
    "share_post",
    "series",
    # "assets",
    "post_stats",
    "photos",
]

# Localization
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'ru': {
        'OUTPUT_PATH': 'output'
        },
    'en': {
        'SITENAME': 'Marxunion',
        'SITESUBTITLE': '',
        'TIMEZONE': 'Europe/London',
        'OUTPUT_PATH': 'output/en'
        }
    }

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight", "linenums": True},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"permalink": "true"},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

SITE_UPDATED = datetime.date.today()
