from application import app
from flask import render_template
from application.mockdata import mockdata


@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', contacts=mockdata) 

@app.route('/addcontact')
def addcontact():
  return render_template('addcontact.html')
