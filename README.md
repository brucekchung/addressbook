# AddressBook

Address Book application. Can add/delete entries and browse contacts. When adding a 5-digit zipcode, the application will query the USPS api and autofill the City and State inputs.

Built with Python/Flask with a SQLAlchemy database.

![Homepage](/application/static/images/AddressBook.png?raw=true "Homepage with contact added")


### Run AddressBook

Clone the repository and run ```export FLASK_APP=run.py``` or ```export FLASK_APP=run.py FLASK_DEBUG=true` to see live changes.  Then enter ```flask run``` into terminal.

The application will be on ```http://localhost:5000/```

