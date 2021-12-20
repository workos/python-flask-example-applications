import os

from flask import (Flask, session, redirect, render_template, request, url_for)
import workos


# Flask Setup
DEBUG = False
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

# WorkOS Setup

workos.api_key = os.getenv('WORKOS_API_KEY')
workos.project_id = os.getenv('WORKOS_CLIENT_ID')
workos.base_api_url = 'http://localhost:7000/' if DEBUG else workos.base_api_url

# Enter Connection ID here

CUSTOMER_CONNECTION_ID = 'xxx'


@app.route('/')
def login():
    if session:
        return render_template('login_successful.html', first_name=session['first_name'], raw_profile=session['raw_profile'])
    else:
        return render_template('login.html')

@app.route('/auth')
def auth():

    authorization_url = workos.client.sso.get_authorization_url(
        redirect_uri = url_for('auth_callback', _external=True),
        state = {},
        connection = CUSTOMER_CONNECTION_ID 
    )

    return redirect(authorization_url)
    

@app.route('/auth/callback')
def auth_callback():
    code = request.args.get('code')
    profile = workos.client.sso.get_profile_and_token(code)
    p_profile = profile.to_dict()
    session['first_name'] = p_profile['profile']['first_name']
    session['raw_profile'] = p_profile['profile']
    session['session_id'] = p_profile['profile']['id']
    print('session', session)
    return redirect('/')
    

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.clear()
    print(session)
    return redirect('/')
