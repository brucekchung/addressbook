from application import db


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  street = db.Column(db.String(120), nullable=False)
  city = db.Column(db.String(30), nullable=False)
  state = db.Column(db.String(15), nullable=False)
  zipcode = db.Column(db.String(15), nullable=False)

  def __repr__(self):
    return f"Post('{self.id}', '{self.name}', '{self.street}', '{self.city}', '{self.state}', '{self.zipcode}')"

