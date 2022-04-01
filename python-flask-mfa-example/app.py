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


@app.route('/')
def login():
    print(session)
    if session['factor_list']:
        return render_template('list_factors.html', factors=session['factor_list'])
    return render_template('list_factors.html')


@app.route('/enroll_sms_factor')
def enroll_sms_factor():
    print('hit enroll new factor')
    new_factor = workos.client.mfa.enroll_factor(
        type='sms',
        phone_number='9204703484'
    )
    print(new_factor)
    # will need to have logic to ADD the new factor to the list

    session['factor_list'].append(new_factor)
    print("this is factor list before redirect", session['factor_list'])
    session.modified = True
    return redirect('/')
