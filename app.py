from flask import Flask, render_template
from flask import url_for

app=Flask(__name__)



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)    