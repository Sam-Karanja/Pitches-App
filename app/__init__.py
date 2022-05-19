from flask import Config_options
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy() 

def create_app(config_name):
    app = Flask(__name__)
   
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix ='/authenticate') 

    return app