from models.model import Checking, CheckingSchema, Savings, SavingsSchema, User
from datetime import datetime
date = datetime.now()

def log_register_user(user_name, user_email):
    new_file = open("./logs/user_log.txt", "a")
    new_file.write(f'Registration: ({date}). User Name: {user_name}. User Email {user_email}.\n')
    new_file.close()

def log_login_user(user_email):
    new_file = open("./logs/user_log.txt", "a")
    new_file.write(f'Login: ({date}). User Email {user_email} .\n')
    new_file.close()


checking_schema = CheckingSchema()
savings_schema = SavingsSchema()


def delete_check_log(id,user_id):
    data = Checking.query.filter_by(id=id).first()
    data = checking_schema.dump(data)
    new_file = open("./logs/event_log.txt", "a")
    new_file.write(f"Checking Deletion - ({date}). UserID: {user_id} | {data}\n")
    new_file.close()

def delete_savings_log(id, user_id):
    data = Savings.query.filter_by(id=id).first()
    data = savings_schema.dump(data)
    new_file = open("./logs/event_log.txt", "a")
    new_file.write(f"Savings Deletion - ({date}). UserID: {user_id} | {data}\n")
    new_file.close()