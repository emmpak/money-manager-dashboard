from datetime import datetime
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  transfers = db.relationship('Transfer', backref='originator', lazy='dynamic')

  def __repr__(self):
    return '<User {}>'.format(self.username)

class Transfer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  currency = db.Column(db.String(3))
  amount = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '<Transfer {}>'.format(f"{self.amount} {self.currency} from {self.originator}")