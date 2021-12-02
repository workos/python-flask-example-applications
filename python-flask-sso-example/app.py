import os

from flask import (Flask, redirect, render_template, request, url_for)
import workos


# Flask Setup
DEBUG = False
app = Flask(__name__)

# WorkOS Setup

workos.api_key = os.getenv('WORKOS_API_KEY')
workos.project_id = os.getenv('WORKOS_CLIENT_ID')
workos.base_api_url = 'http://localhost:7000/' if DEBUG else workos.base_api_url

# Enter Connection ID here
CUSTOMER_CONNECTION_ID = 'xxx'

@app.route('/')
def login():
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
    print(code)
    profile = workos.client.sso.get_profile_and_token(code)
    p_profile = profile.to_dict()
    first_name = p_profile['profile']['first_name']

    raw_profile = p_profile['profile']

    return render_template('login_successful.html', first_name=first_name, raw_profile=raw_profile)