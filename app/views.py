from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'marseilles'}
    members = [{
                    'fbname': 'Joshua Manu',
                    'stname': 'redsurfable',
                    'dbid': '0',
                    'lastseen': '7 months ago',
                },
                {
                    'fbname': 'Christopher Poenaru',
                    'stname': 'Swambulance',
                    'dbid': '0',
                    'lastseen': '7 months ago',
                },
                {
                    'fbname': 'Sam Cho',
                    'stname': 'Mikasa',
                    'dbid': '0',
                    'lastseen': '7 months ago',
                }]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           members=members)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
