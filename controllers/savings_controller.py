# Links
from services.savings_service import add_savings, edit_savings, update_savings, delete_savings
from datetime import datetime, date
from models.model import Savings, SavingsSchema

# Packages
from flask import Blueprint, request, Response, json, render_template, redirect, session

savings_blueprint = Blueprint('savings_api', __name__)

savings_schema = SavingsSchema()

# HTML link routes ----------------------------------
@savings_blueprint.route('/confirm/<int:rec_id>', methods=['GET'])
def confirm(rec_id):
    record = Savings.query.filter_by(id=rec_id).first()
    return render_template('del_savings.html',record=record)

@savings_blueprint.route('/edit/<int:rec_id>', methods=['GET'])
def edit(rec_id):
    record = Savings.query.filter_by(id=rec_id).first()
    return render_template('edit_savings.html',record=record)

# Parsing routes -----------------------------------

@savings_blueprint.route('/new', methods=['POST'])
def new():
    try:
        data = request.form
        add_savings(data)
        return redirect('/display/savings') 
    except Exception as e:
        return redirect('/display/savings')  

@savings_blueprint.route('/update', methods=['POST'])
def update():
    data = request.form
    update_savings(data)
    return redirect('/display/savings')

@savings_blueprint.route('/delete/<int:rec_id>', methods=['GET'])
def delete(rec_id): 
    delete_savings(rec_id)
    return redirect('/display/savings')

def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )