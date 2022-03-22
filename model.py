
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
#Base = descriptive_base()

# Models


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True, nullable=False)
    user_name = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class log(db.Model):
    log_id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    timestamp = db.Column(db.String(150),nullable=False,unique=False)
    value = db.Column(db.Integer , primary_key=False,unique =False)
    notes = db.Column(db.String(150) , primary_key=False,unique =False)
    tracker_id =db.column(db.Integer,db.ForeignKey('tracker_id'),nullable=False)
    user_id = db.column(db.Integer,db.ForeignKey('user_id'),nullable=False)

    
class tracker(db.Model):
    tracker_id = db.Column(db.Integer , primary_key=True,unique =True,autoincrement=True, nullable=False)
    name = db.Column(db.String(150) , primary_key=False,unique =False)
    description = db.Column(db.String(150) , primary_key=False,unique =False)
    tracker_type = db.Column(db.String(150) , primary_key=False,unique =False,nullable=False)
    settings = db.Column(db.String(150) , primary_key=False,unique =False)
    user_id = db.column(db.Integer,db.ForeignKey('user_id'))
    
