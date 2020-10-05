# Links
from . import db, login
from datetime import datetime

# Packages
from marshmallow import Schema, fields
from flask_login import UserMixin
#----------------------------------------------User----------------------------------------------
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(50), nullable= False)
    user_password = db.Column(db.String(300), nullable=False)
    user_name = db.Column(db.String(30), nullable=False)

    def __init__(self, user_email, user_name, user_password):
        self.user_email = user_email
        self.user_password = user_password
        self.user_name = user_name

    def save(self):
        db.session.add(self)
        if db.session.commit():    
            return True
        else:
            return False

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

#----------------------------------------------Checking----------------------------------------------

class Checking(db.Model):
    __tablename__ = 'checking'

    id = db.Column(db.Integer, primary_key=True)
    che_date = db.Column(db.Date, nullable=False)
    che_type = db.Column(db.String(15), nullable=False)
    che_amount = db.Column(db.Float, nullable=False)
    che_description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, che_date, che_type, che_amount, che_description, user_id):
        self.che_date = che_date
        self.che_type = che_type
        self.che_amount = che_amount
        self.che_description = che_description
        self.user_id = user_id

    def save(self):
        
        db.session.add(self)
        db.session.commit()
        # if db.session.commit():
        #     return True
        # else: 
        #     return False

    def update(self):
        if db.session.commit():
            return True
        else:
            return False

    def delete(self):
        db.session.delete(self)
        if db.session.commit():
            return True
        else:
            return False
    
class CheckingSchema(Schema):
    id = fields.Int(dump_only=True)
    che_date = fields.Date(required=True)
    che_type = fields.Str(required=True)
    che_amount = fields.Float(required=True)
    che_description = fields.Str(required=True)
    # user_id = fields.Int(required=True)

#----------------------------------------------Savings----------------------------------------------
class Savings(db.Model):
    __tablename__ = 'savings'

    id = db.Column(db.Integer, primary_key=True)
    sav_date = db.Column(db.Date, nullable=False)
    sav_type = db.Column(db.String(15), nullable=False)
    sav_amount = db.Column(db.Float, nullable=False)
    sav_description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, sav_date, sav_type, sav_amount, sav_description, user_id):
        self.sav_date = sav_date
        self.sav_type = sav_type
        self.sav_amount = sav_amount
        self.sav_description = sav_description
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        if db.session.commit():
            return True
        else:
            return False

    def update(self):
        if db.session.commit():
            return True
        else:
            return False

    def delete(self):
        db.session.delete(self)
        if db.session.commit():
            return True
        else:
            return False
        
class SavingsSchema(Schema):
    id = fields.Int(dump_only=True)
    sav_date = fields.Date(required=True)
    sav_type = fields.Str(required=True)
    sav_amount = fields.Float(required=True)
    sav_description = fields.Str(required=True)
    # user_id = fields.Int(required=True)