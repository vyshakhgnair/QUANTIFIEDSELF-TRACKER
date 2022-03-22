
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
Base=descriptive_base()

# Models
class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    user_name = db.Column(db.String(150),nullable=False,unique=True)
    email = db.Column(db.String(150), unique=True,nullable=False)
    password = db.Column(db.String(150),nullable=False)
    
 class log(db.Model)
    log_id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    timestamp = db.Column(db.String(150),nullable=False,unique=False)
    value = db.Column(db.Integer , primary_key=False,unique =False)
    notes = db.Column(db.String(150) , primary_key=False,unique =False)
    tracker_id =  
    user_id = 
    added_date_time = db.Column(db.String(150) , primary_key=False, unique =False)
    
 class tracker(db.Model)
    tracker_id = db.Column(db.Integer , primary_key=True,unique =True)
    name = db.Column(db.String(150) , primary_key=False,unique =False)
    description = db.Column(db.String(150) , primary_key=False,unique =False)
    tracker_type = db.Column(db.String(150) , primary_key=False,unique =False)
    settings = db.Column(db.String(150) , primary_key=False,unique =False)
    user_id = 
    
