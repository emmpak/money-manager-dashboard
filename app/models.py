from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  transfers = db.relationship('Transfer', backref='originator', lazy='dynamic')

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return '<User {}>'.format(self.username)

class Transfer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  currency = db.Column(db.String(3))
  amount = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  notes = db.relationship('Note', backref='transfer', lazy='dynamic')

  def __repr__(self):
    return '<Transfer {}>'.format(f"{self.amount} {self.currency} from {self.originator}")

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(140))
  transfer_id = db.Column(db.Integer, db.ForeignKey('transfer.id'))

  def __repr__(self):
    return '<Note {}>'.format(self.body)