# Links
from . import bcrypt
from models.model import User
from services.log_service import log_register_user, log_login_user
from datetime import datetime
# Packages
from flask import Blueprint, request, redirect, render_template, json, url_for, session, flash

auth_blueprint = Blueprint('auth_api', __name__)

# HTML link routes ----------------------------------

@auth_blueprint.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@auth_blueprint.route('/index')
def index():
    return render_template('login.html')

# Parsing routes -----------------------------------

@auth_blueprint.route('/register', methods=['POST'])
def register():
    try:
        body = request.form
        user_email = body['user_email']
        user_name = body['user_name']
        user_password = bcrypt.generate_password_hash(body['user_password']).decode('utf-8')
        user = User.query.filter_by(user_email=user_email).first()
        if user: 
            message = 'Error: Account already created with that email!'
            return render_template('sign_up.html', message=message, mes_color="PaleVioletRed")
        elif not user:
            new_user = User(user_email, user_name, user_password)
            if new_user.save():
                log_register_user(user_name, user_email)
            message = "Account registered, Thank you!"
            return render_template('/login.html', message=message, mes_color="greenyellow")
        else: 
            message = 'Error: Problem creating account!'
            return render_template('sign_up.html', message=message, mes_color="PaleVioletRed")
    except Exception as e:
        return render_template('sign_up.html')

@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        body = request.form
        user_email = body['user_email']
        user_password = body['user_password']
        user = User.query.filter_by(user_email=user_email).first()
        if user:
            if bcrypt.check_password_hash(user.user_password, user_password):
                log_login_user(user_email)
                return redirect('/display/menu')
        elif not user:
            message = 'Error: Incorrect credentials!'
            return render_template('login.html', message=message, mes_color="PaleVioletRed")
    except Exception as e:
        return redirect('/')

@auth_blueprint.route('/logout')
def logout():
    pass