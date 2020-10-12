import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_paranoid import Paranoid
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import SCRIPTS, EXECUTABLES, UploadSet, configure_uploads, AllExcept, patch_request_class
from flask_dropzone import Dropzone


app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
    paranoid = Paranoid(app)
    paranoid.redirect_view = '/'
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")
print(f'ENV is set to: {app.config["ENV"]}')


db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'bp_users.login'
login_manager.login_message_category = 'info'
login_manager.session_protection = None

filehost = UploadSet('filehost', AllExcept(SCRIPTS + EXECUTABLES))
configure_uploads(app, filehost)
patch_request_class(app, size=500*1024*1024)

dropzone = Dropzone(app)



from portfolio.bp_main.routes import bp_main

app.register_blueprint(bp_main)

from portfolio.bp_users.routes import bp_users

app.register_blueprint(bp_users)

from portfolio.bp_homescreen.routes import bp_homescreen

app.register_blueprint(bp_homescreen)

from portfolio.bp_errors.routes import bp_errors

app.register_blueprint(bp_errors)

from portfolio.bp_filehost.routes import bp_filehost

app.register_blueprint(bp_filehost)

from portfolio.bp_al.routes import bp_al

app.register_blueprint(bp_al)
