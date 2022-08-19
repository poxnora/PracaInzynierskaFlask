import os
import re

from flask import Flask, render_template, request, Blueprint, flash

from backend import Scraping

views_blueprint = Blueprint('views', __name__,template_folder=(os.path.abspath(os.path.join(__file__, "../..",'frontend','templates'))), static_folder=(os.path.abspath(os.path.join(__file__, "../..",'frontend','static'))))

@views_blueprint.route('/')
def main():
    return render_template('main_page.html')


@views_blueprint.route('/search',  methods=['POST'])
def search():
    if request.method == "POST":
        query = request.form.get('query')
        max_value = request.form.get('max_value')
        start = request.form.get('start_date')
        end = request.form.get('end_date')
        advanced = request.form.get('check')
        if not re.match('^[a-zA-Z0-9]', query):
            flash("Invalid company!")
        if advanced != "on":
            query = query.replace(" ", "")
            query = "#"+query
        Scraping.get_tweets(query,max_value,start,end)
        return render_template('main_page.html')
