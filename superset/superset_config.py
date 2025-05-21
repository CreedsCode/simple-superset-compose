import os

# Superset specific config
ROW_LIMIT = int(os.environ.get('SUPERSET_ROW_LIMIT', '5000'))
SUPERSET_WEBSERVER_PORT = int(os.environ.get('SUPERSET_WEBSERVER_PORT', '8088'))

# Explicitly set PREFERRED_URL_SCHEME for Flask App Builder
PREFERRED_URL_SCHEME = os.environ.get('PREFERRED_URL_SCHEME', 'https')

# The SQLAlchemy connection string to your database
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SUPERSET_DB_URI',
    f"postgresql+psycopg2://{os.environ.get('DATABASE_USER', 'superset')}:{os.environ.get('DATABASE_PASSWORD', 'secretsecret')}@{os.environ.get('DATABASE_HOST', 'db')}:{os.environ.get('DATABASE_PORT', '5432')}/{os.environ.get('DATABASE_DB', 'superset')}"
)

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False

# Flask App Builder configuration
# Your App secret key
SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY', 'MyVerySecretKey')

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = os.environ.get('MAPBOX_API_KEY', '')

# Security settings
PREVENT_UNSAFE_DB_CONNECTIONS = False
TALISMAN_ENABLED = False

# Role configuration
PUBLIC_ROLE_LIKE = "Gamma"

# HTTP headers
HTTP_HEADERS = {}

# Localization
BABEL_DEFAULT_LOCALE = "zh"
LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "zh": {"flag": "cn", "name": "中文"},
}

# Feature flags
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_REMOVE_FILTERS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "HORIZONTAL_FILTER_BAR": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_RBAC": True,
}

# Webserver configuration
ENABLE_PROXY_FIX = True
WEBSERVER_THREADS = int(os.environ.get('WEBSERVER_THREADS', '8'))
WEBSERVER_TIMEOUT = int(os.environ.get('WEBSERVER_TIMEOUT', '120'))
GUNICORN_CMD_ARGS = os.environ.get('GUNICORN_CMD_ARGS', "--timeout 120 --limit-request-line 0 --limit-request-field_size 0")

# CORS and domain configuration
SUPERSET_WEBSERVER_DOMAINS = ["esk80gskogcoo4kk8sk4os08.orbit.joinwebzero.com"]
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['https://esk80gskogcoo4kk8sk4os08.orbit.joinwebzero.com']
}

# Session Cookie settings
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

# Other settings
APP_NAME = os.environ.get("APP_NAME", "Superset")
APP_ICON = os.environ.get("APP_ICON", "/static/assets/images/superset-logo-horiz.png")

print("Loaded consolidated configuration.")
print(f"SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI[:50]}...")
print(f"SECRET_KEY set: {bool(SECRET_KEY and SECRET_KEY != 'MyVerySecretKey')}")
print(f"SUPERSET_WEBSERVER_DOMAINS: {SUPERSET_WEBSERVER_DOMAINS}")
print(f"FEATURE_FLAGS: {FEATURE_FLAGS}")
