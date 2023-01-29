# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

# THINGS TO CONFIGURE
# ---------------------------------------------------------------------

SITENAME = "Союз Марксистов"
SITESUBTITLE = ""
AUTHOR = SITENAME
SITEURL = "/"
DEFAULT_LANG = "ru"


LANDING_PAGE_ABOUT = {
    "title": "My news",
    "details": """<p>This website contains Info that might be interesting for you, enjoy!</p>""",
}


"""
PROJECTS = [
    {
        "name": "news-o-matic",
        "url": "https://github.com/iranzo/news-o-matic",
        "description": "Canned news automation for quickly setting up a news with Pelican",
    },
    {
        "name": "Citellus",
        "url": "https://citellus.org",
        "description": "Troubleshooting automation tool with easy to contribute rules",
    },
    {
        "name": "Pablo Iranzo news",
        "url": "https://iranzo.github.io",
        "description": "Other projects at Github website",
    },
    {
        "name": "Redken Telegram BOT",
        "url": "https://t.me/redken_bot",
        "description": "A Telegram bot with support for Karma, RSS Feeds, Quotes, etc",
    },
]


LINKS = (
    ("Redken on telegram", "https://t.me/redken_bot"),
    ("RHJobs channel on TG", "https://t.me/rhjobs"),
)
"""

# Keep 'name' like 'twitter' with what 'FontAwesome has for putting the right icon'

SOCIAL = (
    ("Twitter", "http://twitter.com/iranzop"),
    ("github", "http://github.com/iranzo"),
    ("linkedin", "https://www.linkedin.com/in/iranzo/"),
)

# Extra files customization
EXTRA_PATH_METADATA = {}

# Photo Gallery plugin
PHOTO_LIBRARY = "gallery-source/"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = "© Pablo Iranzo Gómez (https://iranzo.github.io)"
PHOTO_WATERMARK_IMG = ""
PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True
PHOTO_EXIF_COPYRIGHT = "COPYRIGHT"
# PHOTO_EXIF_COPYRIGHT_AUTHOR = 'Your Name Here' (Defaults to Author)

# ONLY TOUCH IF YOU KNOW WHAT YOU'RE DOING!
# ---------------------------------------------------------------------

STATIC_PATHS = ['content/posts', 'content/pages']
STATIC_EXCLUDES = ['plugins', 'theme']
PAGE_EXCLUDES = STATIC_EXCLUDES
ARTICLE_EXCLUDES = STATIC_EXCLUDES
ARTICLE_PATHS = ['content/posts']
PAGE_PATHS = ['content/pages']

TIMEZONE = "Europe/Moscow"

# Put as draft content in the future
WITH_FUTURE_DATES = True

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

DISPLAY_PAGES_ON_MENU = False

CACHE_CONTENT = False
CACHE_PATH = ".cache"
LOAD_CONTENT_CACHE = False

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

# 'better_codeblock_line_numbering'
# 'better_figures_and_images'

THEME = "theme"

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

# elegant
TYPOGRIFY = True
RECENT_ARTICLE_SUMMARY = True
RESPONSIVE_IMAGES = True

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

DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = ""

FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"
USE_FOLDER_AS_CATEGORY = False

SEARCH_BOX = False

# URL Settings to be compatible with octopress
ARTICLE_URL = "news/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

ARTICLE_LANG_URL = "news/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/"
ARTICLE_LANG_SAVE_AS = "news/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html"

YEAR_ARCHIVE_URL = "news/archive/{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "news/archive/{date:%Y}/index.html"

MONTH_ARCHIVE_URL = "news/archive/{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "news/archive/{date:%Y}/{date:%m}/index.html"

CATEGORY_URL = "news/category/{slug}/"
CATEGORY_SAVE_AS = "news/category/{slug}/index.html"

TAG_URL = "news/tag/{slug}/"
TAG_SAVE_AS = "news/tag/{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

TAGS_URL = "tags"
TAGS_SAVE_AS = "tags/index.html"
AUTHORS_URL = "authors"
AUTHORS_SAVE_AS = "authors/index.html"
CATEGORIES_URL = "categories"
CATEGORIES_SAVE_AS = "categories/index.html"
ARCHIVES_URL = "archives"
ARCHIVES_SAVE_AS = "archives/index.html"

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 0

PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

SITE_UPDATED = datetime.date.today()

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ("Tags", TAGS_URL, TAGS_SAVE_AS),
    ("Archives", ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
