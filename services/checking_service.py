# Links
from models.model import Checking  
from services.log_service import delete_check_log
from models.model import CheckingSchema   
from datetime import datetime, date

# Packages
from flask import render_template, request, json

checking_schema = CheckingSchema()

def add_checking(data):
    user_id = 1
    if data['che_type'] == "Withdraw":
        amount = -float(data['che_amount'])
        # amount = amount * -1
        # amount = round(amount, 2)
    elif data['che_type'] == "Deposit":
        amount = data['che_amount']
    new_checking = Checking(
    che_date=data['che_date'],
    che_type=data['che_type'],
    che_amount=amount,
    che_description=data['che_description'],
    user_id=user_id
    )
    new_checking.save()

def delete_checking(id):
    user_id = 1
    record = Checking.query.filter_by(id=id).first()
    if record:
        delete_check_log(id, user_id)
        return {'Message': record.delete()}
    else:
        message = "No checking transaction"
        return {'Message': message}

def edit_checking(id):
    data = Checking.query.filter_by(id=id).first()
    edit = checking_schema.dump(data)
    return edit

def update_checking(data):
    trans = Checking.query.filter_by(id=data['id']).first()
    trans.che_date = data['che_date']
    trans.che_type = data['che_type']
    trans.che_amount = data['che_amount']
    trans.che_description = data['che_description']
    message = trans.update()
    return {'Message': message}
    