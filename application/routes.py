from application import app
from application.forms import ContactForm
from flask import render_template, flash, redirect, url_for
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
    flash(f'{contact.name.data} added to contacts!', 'success')
    return redirect(url_for('home'))
  return render_template('addcontact.html', contact=contact)
