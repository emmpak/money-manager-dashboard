from flask import render_template, redirect, url_for, session, g
from app import app
from app.models import User, Transfer
from app.forms import LoginForm

@app.before_request
def before_request():
  g.current_user = None
  if 'user_id' in session:
    g.current_user = User.query.get(int(session['user_id']))

@app.route('/')
@app.route('/index')
@app.route('/transfers')
def index():
  if not g.current_user:
    return redirect(url_for('login'))

  return render_template('index.html')

@app.route('/login', methods=['post', 'get'])
def login():
  if g.current_user:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      return redirect(url_for('login'))
    session['user_id'] = user.id
    return redirect(url_for('index'))
  return render_template('login.html', form=form)

@app.route('/transfers/<transfer_id>')
def transfer(transfer_id):
  user = User(username='user')
  transfer = Transfer(currency="USD", amount=100, originator=user)
  transfer = Transfer.query.filter_by()
