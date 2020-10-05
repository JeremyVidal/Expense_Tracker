# Links
from models.model import Savings
from services.log_service import delete_savings_log
from models.model import SavingsSchema
from datetime import datetime, date

# Packages
from flask import render_template, request, json

savings_schema = SavingsSchema()

def add_savings(data):
    user_id = 1
    new_savings = Savings(
        sav_date=data['sav_date'],
        sav_type=data['sav_type'],
        sav_amount=data['sav_amount'],
        sav_description=data['sav_description'],
        user_id=user_id
    )
    new_savings.save()


def delete_savings(id):
    user_id = 1
    record = Savings.query.filter_by(id=id).first()
    if record:
        delete_savings_log(id, user_id)
        return {'Message': record.delete()}
    else:
        message = "No savings transaction"
        return {'Message': message}

def edit_savings(id):
    data = Savings.query.filter_by(id=id).first()
    edit = savings_schema.dump(data)
    return edit

def update_savings(data):
    trans = Savings.query.filter_by(id=data['id']).first()
    trans.sav_date = data['sav_date']
    trans.sav_type = data['sav_type']
    trans.sav_amount = data['sav_amount']
    trans.sav_description = data['sav_description']
    message = trans.update()
    return {'Message': message}