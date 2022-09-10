import os
import re

from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user, login_user, logout_user

from backend.configuration.Config import Config
from backend.configuration.database import db
from backend.models.User import User

from backend.services import Scraping

views_blueprint = Blueprint('views', __name__,
                            template_folder=Config.TEMPLATES_FOLDER,
                            static_folder=Config.STATIC_FOLDER)



@views_blueprint.route('/')
def main_page():
    return render_template('main_page.html')


@views_blueprint.route('/login' , methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/dashboard')
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        print(email)
        if len(password) < 8 and not len(password) == 0:
            flash("Invalid password!")
        if re.match('\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?', email):
            flash("Invalid email!")
        else:
            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                login_user(user)
                return render_template('dashboard.html')
    return render_template('login.html')


@views_blueprint.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        first = request.form.get('first')
        last = request.form.get('last')
        password1 = request.form.get('password1')
        if not re.match('^[a-zA-Z0-9]', first):
            flash("Invalid first name!")
        if not re.match('^[a-zA-Z0-9]', last):
            flash("Invalid last name!")
        if len(password) < 8:
            flash("Password must have at least 8 characters!")
        if password != password1:
            flash("Passwords must match!")
        if re.match('\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?', email):
            flash("Invalid email!")
        else:
            if User.query.filter_by(email=email):
                flash("That email already exists!")
            user = User(email=email, firstname=first,lastname=last)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return render_template('dashboard.html')
    return render_template('register.html')

@views_blueprint.route('/logout')
def logout():
    logout_user()
    return render_template('main_page.html')

@login_required
@views_blueprint.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@views_blueprint.route('/search', methods=['POST'])
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
            query = "#" + query
        Scraping.get_tweets(query, max_value, start, end)
        return render_template('main_page.html')
