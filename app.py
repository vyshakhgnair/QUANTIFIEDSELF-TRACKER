from flask import Flask, render_template, url_for, redirect, request, flash
from model import *


usernam=None
user_idd=0
all = User.query.all()


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.form:
        global usernam
        usernam = request.form['user']
        pass_word = request.form.get('password')
        x = User.query.filter_by(user_name=usernam, password=pass_word).first()
        if(x is None):
            error = "Wrong credentials"
        else:
            return redirect(url_for('dash'))
    return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global user_idd
    if request.form and len(all) == 0:
        user_id = 100
        usernm = request.form['user']
        email_id = request.form['email']
        pass_key = request.form['password']

        missing = User.query.filter_by(user_name=usernm).first()

        if missing is None:

            data = User(user_id=100, user_name=usernm,
                        password=pass_key, email=email_id)
            db.session.add(data)
            db.session.commit()
            user_idd=user_id
            return redirect(url_for('index'))
    else:
        if request.form:
            usernm = request.form['user']
            email_id = request.form['email']
            pass_key = request.form['password']

            missing = User.query.filter_by(user_name=usernm).first()

            if missing is None:
                data = User(user_name=usernm,
                            password=pass_key, email=email_id)
                db.session.add(data)
                db.session.commit()
                user_idd=user_id
                return redirect(url_for('index'))

    return render_template('signup.html')


@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')


@app.route('/addtrack', methods=['GET', 'POST'])
def addtracker():
    global user_idd
    if request.form:
        name_add = request.form['tracknm']
        description_add=request.form['description']
        trackertype=request.form['type']
        settings_add = request.form['setting']
        user_obj=User.query.filter_by(user_name=usernam).first()
        if user_obj is not None:
            user_idd=user_obj.user_id


        data=tracker(name=name_add,description=description_add,tracker_type=trackertype,settings=settings_add,user_id=user_idd)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('dash'))
    return render_template('add_tracker.html')   

if __name__ == '__main__':
    app.run(debug=True)
