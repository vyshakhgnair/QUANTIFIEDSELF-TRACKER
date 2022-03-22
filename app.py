from flask import Flask, render_template, url_for, redirect,request,flash
from model import  *

all=User.query.all()
@app.route('/',methods=['GET','POST'])
def index():
    error=None
    if request.form:
        
        usernam=request.form['user']
        pass_word=request.form.get('password')
        x=User.query.filter_by(user_name=usernam,password=pass_word).first()
        if(x is None):
            error="Wrong credentials"
        else :      
            return redirect(url_for('dash'))
    return render_template('login.html',error=error)


@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.form and len(all)==0:
        user_id=100
        usernm = request.form['user']
        email_id = request.form['email']
        pass_key = request.form['password']


        missing = User.query.filter_by(user_name=usernm).first()
       
        if missing is None:
            
            data = User(user_id=100, user_name=usernm,password=pass_key, email=email_id)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('index'))
    else:
        if request.form:
            usernm = request.form['user']
            email_id = request.form['email']
            pass_key = request.form['password']


            missing = User.query.filter_by(user_name=usernm).first()

            if missing is None:
                data = User(user_name=usernm,password=pass_key, email=email_id)
                db.session.add(data)
                db.session.commit()
                return redirect(url_for('index'))


    return render_template('signup.html') 


@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
