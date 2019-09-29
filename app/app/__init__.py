#!/usr/bin/env python3
# encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, user_logged_in, user_loaded_from_cookie
import os

app = Flask(__name__)
app.config.from_object('config.default')
db = SQLAlchemy(app)

from flask_bootstrap import Bootstrap

Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

from app.views import *

app.register_blueprint(home, url_prefix='')
app.register_blueprint(manage, url_prefix='/manage')
app.register_blueprint(user, url_prefix='/user')

from app.daemon import *

dm = Daemon()
if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    dm.loadall()
