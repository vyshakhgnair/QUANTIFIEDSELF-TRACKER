
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
 
# Models
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    user_name = db.Column(db.String(150),nullable=False,unique=True)
    email = db.Column(db.String(150), unique=True,nullable=False)
    password = db.Column(db.String(150),nullable=False)
 
