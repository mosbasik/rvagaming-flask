from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
from models import Site_User


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
#    user = {'nickname': 'marseilles'}
#    members = [{
#                    'fbname': 'Joshua Manu',
#                    'stname': 'redsurfable',
#                    'dbid': '0',
#                    'lastseen': '7 months ago',
#                },
#                {
#                    'fbname': 'Christopher Poenaru',
#                    'stname': 'Swambulance',
#                    'dbid': '0',
#                    'lastseen': '7 months ago',
#                },
#                {
#                    'fbname': 'Sam Cho',
#                    'stname': 'Mikasa',
#                    'dbid': '0',
#                    'lastseen': '7 months ago',
#                }]
    return render_template('index.html', title='Home', user=user, members=members)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname','email'])
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login.  Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user = None:
        nickname = resp.nickname
