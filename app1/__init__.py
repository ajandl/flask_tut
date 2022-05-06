from flask import Flask

app = Flask(__name__)
'''creates an instance of Flask, many optional parameters are omitted here.
One optional parameter omitted above is template_folder.
This defaults to templates'''

from app1 import routes
