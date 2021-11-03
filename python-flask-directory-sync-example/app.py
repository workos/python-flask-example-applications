import os
from flask import (Flask, render_template, request, Response)
import workos
from workos import client as workos_client

DEBUG = False
app = Flask(__name__)

workos.api_key = os.getenv('WORKOS_API_KEY')
workos.base_api_url = 'http://localhost:5000/' if DEBUG else workos.base_api_url
directory_id = os.getenv('DIRECTORY_ID')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def directory_users():
    users = workos_client.directory_sync.list_users(directory=directory_id)
    return render_template('users.html', users=users)


@app.route('/groups')
def directory_groups():
    groups = workos_client.directory_sync.list_groups(directory=directory_id)

    return render_template('groups.html', groups=groups)

@app.route('/webhooks', methods=['POST'])
def webhooks():
    payload = request.get_data()
    sig_header = request.headers['Workos-Signature']
    
    response = workos_client.webhooks.verify_event(
    payload = payload,
    sig_header = sig_header,
    secret = os.getenv('WEBHOOKS_SECRET')
    )
    # Validate the response is successful
    print(response)

    # Return a 200 to prevent retries based on validation
    return Response(status=200)
