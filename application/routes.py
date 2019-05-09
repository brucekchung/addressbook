from application import app, db
from application.forms import ContactForm
from application.models import Post
from application.mockdata import mockdata
from flask import render_template, flash, redirect, url_for



@app.route('/')
@app.route('/home', methods=['GET', 'DELETE'])
def home():
  contacts = Post.query.all()
  return render_template('home.html', contacts=contacts) 

@app.route('/addcontact', methods=['GET', 'POST'])
def addcontact():
  contact = ContactForm()
  if contact.validate_on_submit():
    contact_to_add = Post(
      name = contact.name.data,
      street = contact.street.data,
      city = contact.city.data,
      state = contact.state.data,
      zipcode = contact.zipcode.data
    ) 
    db.session.add(contact_to_add)
    db.session.commit()
    flash(f'{contact.name.data} added to contacts!', 'success')
    return redirect(url_for('home'))
  return render_template('addcontact.html', contact=contact)
