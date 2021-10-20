import os
from flask import (Flask, render_template, url_for)
import workos

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
    users = workos.client.directory_sync.list_users(directory=directory_id)
    return render_template('users.html', users=users)


@app.route('/groups')
def directory_groups():
    groups = workos.client.directory_sync.list_groups(directory=directory_id)

    return render_template('groups.html', groups=groups)
