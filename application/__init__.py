from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATBASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

#avoid circular import by putting at bottom
from application import routes
