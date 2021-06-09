import os
import datetime
import hashlib
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object('config')


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

@app.route("/public/")
def COVID_public():
    return render_template("public_page.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
