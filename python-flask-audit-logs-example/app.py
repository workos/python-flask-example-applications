import json
import os
from urllib.parse import urlparse, parse_qs
from flask import Flask, session, redirect, render_template, request, url_for
import workos
from datetime import datetime, timedelta
from audit_log_events import (
    user_signed_in,
    user_logged_out,
    user_connection_deleted,
    user_organization_deleted,
    user_organization_set,
)

# Flask Setup
DEBUG = False
app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

# WorkOS Setup

workos.api_key = os.getenv("WORKOS_API_KEY")
workos.project_id = os.getenv("WORKOS_CLIENT_ID")
workos.base_api_url = "http://localhost:7000/" if DEBUG else workos.base_api_url


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True, indent=4)


app.jinja_env.filters["tojson_pretty"] = to_pretty_json


@app.route("/", methods=["POST", "GET"])
def index():
    try:
        return render_template(
            "send_events.html",
            organization_id=session["organization_id"],
        )
    except KeyError:
        return render_template("login.html")


@app.route("/set_org", methods=["POST", "GET"])
def set_org():
    organization_id = request.form["org"]
    session["organization_id"] = organization_id
    organization_set = workos.client.audit_logs.create_event(
        organization_id, user_organization_set
    )
    return redirect("/")


@app.route("/send_event", methods=["POST", "GET"])
def send_event():
    event_type = request.form["event"]
    organization_id = session["organization_id"]
    events = [
        user_signed_in,
        user_logged_out,
        user_organization_deleted,
        user_connection_deleted,
    ]
    event = events[int(event_type)]
    organization_set = workos.client.audit_logs.create_event(organization_id, event)
    return redirect("/")


@app.route("/export_events", methods=["POST", "GET"])
def export_events():
    organization_id = session["organization_id"]
    return render_template("export_events.html", organization_id=organization_id)


@app.route("/get_events", methods=["POST", "GET"])
def get_events():
    organization_id = session["organization_id"]
    event_type = request.form["event"]
    today = datetime.today()
    last_month = today - timedelta(days=30)
    last_month_iso = last_month.isoformat()
    today_iso = today.isoformat()

    if event_type == "generate_csv":
        create_export_response = workos.client.audit_logs.create_export(
            organization=organization_id,
            range_start=last_month_iso,
            range_end=today_iso,
        )
        session["export_id"] = create_export_response.to_dict()["id"]

    if event_type == "access_csv":
        export_id = session["export_id"]
        fetch_export_response = workos.client.audit_logs.get_export(export_id)
        return redirect(fetch_export_response.to_dict()["url"])

    return redirect("export_events")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
