from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATBASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from mainpage import routes
