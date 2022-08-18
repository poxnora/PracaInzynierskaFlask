import os

from flask import Flask, render_template, request, Blueprint

views_blueprint = Blueprint('views', __name__,template_folder=(os.path.abspath(os.path.join(__file__, "../..",'frontend','templates'))), static_folder=(os.path.abspath(os.path.join(__file__, "../..",'frontend','static'))))

@views_blueprint.route('/')
def main():
    return render_template('main_page.html')


@views_blueprint.route('/search',  methods=['POST'])
def search():
    print(request.form['query'])
    return render_template('main_page.html')
