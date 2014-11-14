from flask import render_template
from app import app


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
