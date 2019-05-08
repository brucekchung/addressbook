from application import app
from application.forms import ContactForm
from flask import render_template
from application.mockdata import mockdata


# from application.models import Post

@app.route('/')
@app.route('/home')
def home():
  # actual = Post.query.all()
  # print('postdata: ', actual)
  return render_template('home.html', contacts=mockdata) 

@app.route('/addcontact', methods=['GET', 'POST'])
def addcontact():
  contact = ContactForm()
  if contact.validate_on_submit():
    print('worked!!')
  return render_template('addcontact.html', contact=contact)
