# Links
from services.checking_service import add_checking, edit_checking, update_checking, delete_checking
from datetime import datetime, date
from models.model import Checking
# Packages
from flask import Blueprint, request, Response, json, render_template, redirect, session

checking_blueprint = Blueprint('checking_api', __name__)

# HTML link routes ----------------------------------
@checking_blueprint.route('/confirm/<int:rec_id>', methods=['GET'])
def confirm(rec_id):
    record = Checking.query.filter_by(id=rec_id).first()
    return render_template('del_checking.html',record=record)

@checking_blueprint.route('/edit/<int:rec_id>', methods=['GET'])
def edit(rec_id):
    record = Checking.query.filter_by(id=rec_id).first()
    return render_template('edit_checking.html',record=record)

# Parsing routes -----------------------------------
@checking_blueprint.route('/new', methods=['POST'])
def new():
    try:
        data = request.form
        add_checking(data)
        return redirect('/display/checking')
    except Exception as e:
        return redirect('/display/checking')
    
@checking_blueprint.route('/update', methods=['POST'])
def update():
    data = request.form
    update_checking(data)
    return redirect('/display/checking')

@checking_blueprint.route('/delete/<int:rec_id>', methods=['GET'])
def delete(rec_id):
    delete_checking(rec_id)
    return redirect('/display/checking')

def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )