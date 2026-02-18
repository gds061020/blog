AUTHOR = '葛得胜'
SITENAME = '葛得胜的秘密基地'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# 指定主题路径
THEME = 'themes/elegant'

# 启用 typogrify（如果安装了）
TYPOGRIFY = True

# Elegant 主题的额外选项（可选，根据需要添加）
# DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']
# PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None}
