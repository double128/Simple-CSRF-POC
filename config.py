import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "Hack-Something-2"

    # SECURE = True -> CSRF protection on forms is enabled
    # SECURE = False -> CSRF protection is disabled
    # NOTE: DO NOT SET WTF_CSRF_ENABLED MANUALLY. 
    SECURE = False
    if not SECURE:
        WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

