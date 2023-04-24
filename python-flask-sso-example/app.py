import json
import os
from urllib.parse import urlparse, parse_qs
from flask import Flask, session, redirect, render_template, request, url_for
import workos


# Flask Setup
DEBUG = False
app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

# WorkOS Setup

workos.api_key = os.getenv("WORKOS_API_KEY")
workos.project_id = os.getenv("WORKOS_CLIENT_ID")
workos.base_api_url = "http://localhost:7000/" if DEBUG else workos.base_api_url

# Enter Connection ID here

CUSTOMER_ORGANIZATION_ID = ""


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True, indent=4)


app.jinja_env.filters["tojson_pretty"] = to_pretty_json


@app.route("/")
def login():
    try:
        return render_template(
            "login_successful.html",
            first_name=session["first_name"],
            raw_profile=session["raw_profile"],
        )
    except KeyError:
        return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():

    login_type = request.form.get("login_method")

    params = {"redirect_uri": url_for("auth_callback", _external=True), "state": {}}

    if login_type == "saml":
        print("saml")
        params["organization"] = CUSTOMER_ORGANIZATION_ID
    else:
        params["provider"] = login_type

    print(params)

    authorization_url = workos.client.sso.get_authorization_url(**params)

    return redirect(authorization_url)


@app.route("/auth/callback")
def auth_callback():

    code = request.args.get("code")
    profile = workos.client.sso.get_profile_and_token(code)
    p_profile = profile.to_dict()
    session["first_name"] = p_profile["profile"]["first_name"]
    session["raw_profile"] = p_profile["profile"]
    session["session_id"] = p_profile["profile"]["id"]
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    session["raw_profile"] = ""
    return redirect("/")
