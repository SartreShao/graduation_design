from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


# create_app是程序的工厂函数，因为我们需要延迟创建程序实例
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    db.app = app
    db.drop_all()
    db.create_all()
    # 附加路由和自定义错误界面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
