from flask import render_template
from app1 import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adam2'}

    ''' render template knows to look in the templates folder based on the
    optional omitted parameter when creating the flask instance in __init__'''
    return render_template('index.html', title='Home', user=user)


@app.route('/data')
def return_data():
    return {'num1': 42, 'num2': 27}
