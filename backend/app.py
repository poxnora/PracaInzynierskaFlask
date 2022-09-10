import os

from flask import Flask
from flask_migrate import Migrate

from backend.configuration.login import login_manager
from configuration import Config
from backend.configuration.database import db
from backend.views.views import views_blueprint

app = Flask(__name__, template_folder=Config.Config.TEMPLATES_FOLDER,
            static_folder=Config.Config.STATIC_FOLDER)
app.register_blueprint(views_blueprint)
app.config.from_object(Config.DevConfig)
db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

login_manager.init_app(app)
login_manager.login_view = 'login'
app.run(use_reloader=True)
