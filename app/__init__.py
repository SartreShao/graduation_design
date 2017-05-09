from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = None
moment = None
db = None
manager = None
migrate = None


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    global bootstrap, moment, db, manager, migrate
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    db = SQLAlchemy(app)
    manager = Manager(app)
    migrate = Migrate(app, db)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
