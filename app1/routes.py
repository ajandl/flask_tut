from app1 import app #How does it know to look in the __init__ file?

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

