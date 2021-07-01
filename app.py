from flask import (Flask, Blueprint, render_template)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bp = Blueprint('app', __name__)

#Database
user='okkmzdmn'
password='ZvFIeK9-lrRFH22s3WohwW9oDvlCPV5Q'
host='tuffi.db.elephantsql.com'
database='okkmzdmn'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False