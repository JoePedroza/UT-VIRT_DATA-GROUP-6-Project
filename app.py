from os import path
import os
import psycopg2
import csv
import datetime
import hashlib
import subprocess
from flask import Flask, render_template
from werkzeug.utils import secure_filename
from database import list_counties

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app = Flask(__name__)
app.config.from_object('config')

script_dir = path.dirname(path.abspath(__file__))


@app.errorhandler(401)
def COVID_401(error):
    return render_template("page_401.html"), 401

@app.errorhandler(403)
def COVID_403(error):
    return render_template("page_403.html"), 403

@app.errorhandler(404)
def COVID_404(error):
    return render_template("page_404.html"), 404

@app.errorhandler(405)
def COVID_405(error):
    return render_template("page_405.html"), 405

@app.errorhandler(413)
def COVID_413(error):
    return render_template("page_413.html"), 413

@app.route("/")
def COVID_root():
    return render_template("index.html")

@app.route("/submitted/", methods=["GET", "POST"])
def COVID_index():
    return render_template('submitted.html')

@app.route("/dashboard/")
def COVID_dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
