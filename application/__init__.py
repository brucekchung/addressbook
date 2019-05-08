from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a42e586fab48f8aa64ae99c15549654e'
app.config['SQLALCHEMY_DATBASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

#avoid circular import by putting at bottom
from application import routes
