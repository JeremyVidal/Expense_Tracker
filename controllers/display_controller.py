# Links
from models.model import Checking , Savings, CheckingSchema, SavingsSchema, db
from services.totals_services import checking_totals, dash_totals, savings_totals
from datetime import datetime
import os
# Packages
from flask import Blueprint, request, Response, json, render_template, redirect, session
from sqlalchemy import extract, desc

display_blueprint = Blueprint('display_api', __name__)

checking_schema = CheckingSchema()
savings_schema = SavingsSchema()

# HTML link routes ----------------------------------

@display_blueprint.route('/menu')
def menu():
    return render_template('menu.html')

@display_blueprint.route('/dis_401')
def dis_401():
    return render_template('401.html')

# Display routes -----------------------------------

@display_blueprint.route('/dashboard')
def dashboard():
    mon_withdraw, mon_deposit, mon_balance, yr_withdraw, yr_deposit, yr_balance, cur_balance, sav_balance, net_worth = dash_totals()
    return render_template('dashboard.html', mon_withdraw=mon_withdraw, mon_deposit=mon_deposit, mon_balance=mon_balance, yr_withdraw=yr_withdraw, yr_deposit=yr_deposit, yr_balance=yr_balance, cur_balance=cur_balance, sav_balance=sav_balance, net_worth=net_worth)

@display_blueprint.route('/checking')
def checking():
    curr_year = datetime.now().year
    user_id = 1
    records = Checking.query.filter_by(user_id=user_id).order_by(desc(Checking.che_date)).order_by(desc(Checking.id)).filter(extract('year', Checking.che_date)>=curr_year).all()  
    record = checking_schema.dump(records, many=True)
    # records = json.dumps(record)
    balance = checking_totals(record)
    return render_template('checking.html', records=records, balance=balance)

@display_blueprint.route('/savings')
def savings():
    curr_year = datetime.now().year
    user_id = 1
    records = Savings.query.filter_by(user_id=user_id).order_by(desc(Savings.sav_date)).order_by(desc(Savings.id)).filter(extract('year', Savings.sav_date)>=curr_year).all()  
    record = savings_schema.dump(records, many=True)
    # records = json.dumps(record)
    balance = savings_totals(record)
    return render_template('savings.html', records=records, balance=balance)