# Links
from models.model import Checking , Savings, CheckingSchema, SavingsSchema
from datetime import datetime

# Packages
from sqlalchemy import extract

checking_schema = CheckingSchema()
savings_schema = SavingsSchema()

def checking_totals(dict_list):
    withdraw = 0
    for i in dict_list:
        if i['che_type'] == 'Withdraw' or i['che_type'] == "RemoveTransfer":
            withdraw += float(i['che_amount'])
    deposit = 0
    for i in dict_list:
        if i['che_type'] == 'Deposit'  or i['che_type'] == "AddTransfer":
            deposit += float(i['che_amount'])
    balance = deposit + withdraw
    balance = round(balance, 2)
    return (balance)

def savings_totals(dict_list):
    user_id = 1
    dict_list = Savings.query.filter_by(user_id=user_id).all()  
    dict_list = savings_schema.dump(dict_list, many=True)
    sav_balance = 0
    for i in dict_list:
        sav_balance += float(i['sav_amount'])
    sav_balance = round(sav_balance, 2)
    return (sav_balance)
 

def dash_totals():
    user_id = 1
    # Monthly totals------------------------
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    dict_list = Checking.query.filter_by(user_id=user_id).filter(extract('year', Checking.che_date)>=curr_year).filter(extract('month', Checking.che_date)>=curr_month).all()  
    dict_list = checking_schema.dump(dict_list, many=True)
    mon_withdraw = 0
    for i in dict_list:
        if i['che_type'] == 'Withdraw' or i['che_type'] == "RemoveTransfer":
            mon_withdraw += float(i['che_amount'])
    mon_deposit = 0
    for i in dict_list:
        if i['che_type'] == 'Deposit'  or i['che_type'] == "AddTransfer":
            mon_deposit += float(i['che_amount'])
    mon_balance = mon_deposit + mon_withdraw
    mon_balance = round(mon_balance, 2)

    # Yealry totals------------------------    
    curr_year = datetime.now().year
    dict_list = Checking.query.filter_by(user_id=user_id).filter(extract('year', Checking.che_date)>=curr_year).all()  
    dict_list = checking_schema.dump(dict_list, many=True)
    yr_withdraw = 0
    for i in dict_list:
        if i['che_type'] == 'Withdraw' or i['che_type'] == "RemoveTransfer":
            yr_withdraw += float(i['che_amount'])
    yr_deposit = 0
    for i in dict_list:
        if i['che_type'] == 'Deposit'  or i['che_type'] == "AddTransfer":
            yr_deposit += float(i['che_amount'])
    yr_balance = yr_deposit + yr_withdraw
    yr_balance = round(yr_balance, 2)

    # Current balance total------------------------    
    dict_list = Checking.query.filter_by(user_id=user_id).all()  
    dict_list = checking_schema.dump(dict_list, many=True)
    cur_withdraw = 0
    for i in dict_list:
        if i['che_type'] == 'Withdraw' or i['che_type'] == "RemoveTransfer":
            cur_withdraw += float(i['che_amount'])
    cur_deposit = 0
    for i in dict_list:
        if i['che_type'] == 'Deposit'  or i['che_type'] == "AddTransfer":
            cur_deposit += float(i['che_amount'])
    cur_balance = cur_deposit + cur_withdraw
    cur_balance = round(cur_balance, 2)

    # Savings balance total------------------------
    dict_list = Savings.query.filter_by(user_id=user_id).all()  
    dict_list = savings_schema.dump(dict_list, many=True)
    sav_balance = 0
    for i in dict_list:
        sav_balance += float(i['sav_amount'])
    sav_balance = round(sav_balance, 2)
    
    net_worth = cur_balance + sav_balance

    return (mon_withdraw, mon_deposit, mon_balance, yr_withdraw, yr_deposit, yr_balance, cur_balance, sav_balance, net_worth)