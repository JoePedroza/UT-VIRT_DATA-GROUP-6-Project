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
