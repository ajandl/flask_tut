from flask import flash, redirect, render_template, url_for
from app1 import app
from app1.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adam2'}
    posts = [
        {
            'author': {'username': 'User1'},
            'body': 'User1 Post1'
        },
        {
            'author': {'username': 'User2'},
            'body': 'User2 Post2'
        }
    ]

    ''' render template knows to look in the templates folder based on the
    optional omitted parameter when creating the flask instance in __init__'''
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/data')
def return_data():
    return {'num1': 42, 'num2': 27}
