
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.debug = True
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
 
# Models
class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    user_name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150), unique=True,nullable=False)
    password = db.Column(db.String(150),nullable=False)
 
# function to render index page
@app.route('/')
def index():
    return render_template('signup.html')
 
if __name__ == '__main__':
    app.run()
