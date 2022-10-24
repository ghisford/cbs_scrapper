
from re import TEMPLATE
from flask import Flask
from news.config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from  flask_migrate import Migrate
import os

# var instatiation
migrate = Migrate()
ma = Marshmallow()
db = SQLAlchemy()

# tell python where to find the templates folder

TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')

def create_app():
    app = Flask(__name__,template_folder=TEMPLATE_FOLDER)
    app.config.from_object(app_config['development'])
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)

    from .views.news_view import views as news
    app.register_blueprint(news)
    return app