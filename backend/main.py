import os

from flask import Flask
from backend import views


app = Flask(__name__,template_folder=os.path.join(os.getcwd(),'frontend','templates'), static_folder=os.path.join(os.getcwd(),'frontend','static'))
app.register_blueprint(views.views_blueprint)
app.run(debug = True,use_reloader=True)