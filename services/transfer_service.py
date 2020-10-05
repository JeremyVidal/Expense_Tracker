# Links
from models.model import Checking, Savings 
from models.model import Checking , Savings, CheckingSchema, SavingsSchema
from datetime import datetime, date

def transfer_rec(dict_list):
    date = datetime.now()
    user_id = 1
    if dict_list['trans_type'] == 'Checking to Savings':
        amount = -float(dict_list['trans_amount'])
        amount = round(amount, 2)
        # Add to checking
        description = "Transfer to Savings"
        new_checking = Checking(
        che_date=date,
        che_type= "RemoveTransfer",
        che_amount=amount,
        che_description=description,
        user_id=user_id
    )
        new_checking.save()
        # Add to savings
        amount = float(dict_list['trans_amount'])
        amount = round(amount, 2)
        description = "Transfer from Checking"
        new_savings = Savings(
            sav_date=date,
            sav_type= "AddTransfer",
            sav_amount=amount,
            sav_description=description,
            user_id=user_id
        )
        new_savings.save()

    elif dict_list['trans_type'] == 'Savings to Checking':
        description = "Transfer from Savings"
        amount = float(dict_list['trans_amount'])
        amount = round(amount, 2)
        # Add to checking
        description = "Transfer From Savings"
        new_checking = Checking(
        che_date=date,
        che_type= "AddTransfer",
        che_amount=amount,
        che_description=description,
        user_id=user_id
    )
        new_checking.save()
        # Add to savings
        amount = -float(dict_list['trans_amount'])
        amount = round(amount, 2)
        description = "Transfer to Checking"
        new_savings = Savings(
            sav_date=date,
            sav_type= "RemoveTransfer",
            sav_amount=amount,
            sav_description=description,
            user_id=user_id
        )
        new_savings.save()


