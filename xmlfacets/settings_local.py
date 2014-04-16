######################
# Required variables #
######################

SECRET_KEY = '0gc4wi0r9jc)i!)4_*$w%f^@t(qjc$iw-5^q19)r^9y)e(b2jb'
POSTGRES_DB = {
    'NAME': 'xmlfacets',
    'USER': 'xmlfacets',
    'PASSWORD': 'xmlfacets',
    'HOST': '127.0.0.1',
    'PORT': '5432'
}

ELASTICSEARCH_ENABLED = True
ELASTICSEARCH_INDEX_NAME = 'xmlfacets'
ELASTICSEARCH_URLS = 'http://127.0.0.1:9200'
# As defined in pyelasticsearch, ELASTICSEARCH_URLS should be:
#
# A URL or iterable of URLs of ES nodes. These are full URLs with port numbers,
# like ``http://elasticsearch.example.com:9200``.
#

SITE_URL = '127.0.0.1'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jean-Daniel Fekete', 'jdfekete@gmail.com'),
)
MANAGERS = ADMINS


#############
# Overrides #
#############

# TIME_ZONE = ''
# LANGUAGE_CODE = ''
# DATETIME_FORMAT = ''
# USE_L10N = True
# USE I18N = True


# Edit STORAGE_PATH to change where uploads, static files, and search indexes
# will be stored, or change each of the settings individually.
# STORAGE_PATH = '/home/fekete/src/cendari/cendari-vre/'

# MEDIA_ROOT = ''
# STATIC_ROOT = ''
# HAYSTACK_XAPIAN_PATH = ''

# Point this to the Less CSS compiler if it is not on PATH
# LESSC_BINARY = ''


######################
# Optional variables #
######################

# Define locally installed apps here
LOCAL_APPS = (
)

