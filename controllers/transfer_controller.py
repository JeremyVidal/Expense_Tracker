# Links
from services.transfer_service import transfer_rec
from datetime import datetime, date
from models import login

# Packages
from flask import Blueprint, request, redirect, render_template, session

transfer_blueprint = Blueprint('transfer_api', __name__)


# HTML link routes ----------------------------------
@transfer_blueprint.route('/transfer', methods=['GET'])
def transfer():
    return render_template('transfer.html')

# Parsing routes -----------------------------------
@transfer_blueprint.route('/update', methods=['POST'])
def update():
    data = request.form
    transfer_rec(data)
    return redirect('/display/menu')



