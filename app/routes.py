from flask import render_template
from app import app
from app.models import User, Transfer

@app.route('/')
@app.route('/index')
def index():
  user = User(username='user')
  transfer = Transfer(currency="USD", amount=100, originator=user)
  return render_template('index.html', user=user)