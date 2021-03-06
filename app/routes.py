from flask import render_template, redirect, url_for, session, g, request
from app import app, db
from app.models import User, Transfer, Note
from app.forms import LoginForm, NoteForm

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
  
@app.route('/logout')
def logout():
  session.pop('user_id', None)
  return redirect(url_for('login'))

@app.route('/transfers/<transfer_id>', methods=['get', 'post'])
def transfer(transfer_id):
  if g.current_user:
    transfer = db.session.query(Transfer).join(User).filter(User.id == g.current_user.id, Transfer.id == int(transfer_id)).first()
    if transfer:
      form = NoteForm()
      if form.validate_on_submit():
        note = Note(body=form.note.data, transfer=transfer)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('transfer', transfer_id=transfer.id))
      return render_template("transfer.html", transfer=transfer, form=form)
