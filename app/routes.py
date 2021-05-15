from flask import render_template, redirect, url_for
from app import app
from app.models import User, Transfer
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/transfers')
def index():
  user = User(username='user')
  transfer = Transfer(currency="USD", amount=100, originator=user)
  return render_template('index.html', user=user)

@app.route('/login', methods=['post', 'get'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    return redirect(url_for('index'))
  return render_template('login.html', form=form)

@app.route('/transfers/<transfer_id>')
def transfer(transfer_id):
  user = User(username='user')
  transfer = Transfer(currency="USD", amount=100, originator=user)
  transfer = Transfer.query.filter_by()
