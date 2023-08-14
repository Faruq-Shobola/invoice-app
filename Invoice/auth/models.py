from invoice import db

class User(db.Model):
  id = db.Column(db.Integer, primary=True)
  username = db.Column(db.String(), unique=True, nullable=False)
  email = db.Column(db.String(), unique=True)
  password = db.Column(db.String(), nullable=False)