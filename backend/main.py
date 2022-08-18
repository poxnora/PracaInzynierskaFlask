import os

from flask import Flask
from backend import views


app = Flask(__name__,template_folder=(os.path.abspath(os.path.join(__file__, "../..",'frontend','templates'))), static_folder=(os.path.abspath(os.path.join(__file__, "../..",'frontend','static'))))
app.register_blueprint(views.views_blueprint)
app.run(debug = True,use_reloader=True)