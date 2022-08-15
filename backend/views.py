import os

from flask import Flask, render_template, request, Blueprint

views_blueprint = Blueprint('views', __name__,template_folder=os.path.join(os.getcwd(),'frontend','templates'), static_folder=os.path.join(os.getcwd(),'frontend','static'))

@views_blueprint.route('/')
def main():
    print(views_blueprint.static_folder)
    return render_template('main_page.html')


@views_blueprint.route('/search',  methods=['POST'])
def search():
    print(request.form['query'])
    return render_template('main_page.html')
