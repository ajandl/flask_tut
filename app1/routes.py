from app1 import app 


@app.route('/')
@app.route('/index')
def index():
    return "Hello World"


@app.route('/data')
def return_data():
    return {'num1': 42, 'num2': 27}
