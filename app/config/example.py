import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///db/db.db'
DEBUG = True
SECRET_KEY = os.urandom(2333)

MAIL_ENABLE = False
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'sta@mail.sqrt-1.me'
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = 'sta@mail.sqrt-1.me'

FREQ_SECOND = False
