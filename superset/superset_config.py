ENABLE_PROXY_FIX = True
SECRET_KEY = "MyVerySecretKey"
PREVENT_UNSAFE_DB_CONNECTIONS = False
TALISMAN_ENABLED = False
# 设置默认语言为中文
BABEL_DEFAULT_LOCALE = "zh"
# 启用语言切换
LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "zh": {"flag": "cn", "name": "中文"},
}
