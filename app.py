# Links
from models import db, ma, login

from controllers import bcrypt, auth_blueprint, checking_blueprint, savings_blueprint, display_blueprint, transfer_blueprint

# Packages
from flask import Flask, render_template, url_for

import os

app = Flask(__name__, static_folder="static", template_folder="templates")

app.config.from_object('config.Development')

db.init_app(app)
ma.init_app(app)
bcrypt.init_app(app)
login.init_app(app)

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(checking_blueprint, url_prefix="/checking")
app.register_blueprint(savings_blueprint, url_prefix="/savings")
app.register_blueprint(display_blueprint, url_prefix="/display")
app.register_blueprint(transfer_blueprint, url_prefix="/transfer")



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/doc')
def doc():
    return render_template('documentation.html')

if __name__ == "__main__":
    app.run()