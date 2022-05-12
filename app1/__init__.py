from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
'''creates an instance of Flask, many optional parameters are omitted here.
One optional parameter omitted above is template_folder.
This defaults to the templates folder'''
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app1 import routes, models
