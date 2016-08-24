from webapp import app

from flask import Flask, render_template, request, url_for, redirect, session
#from dbconnect import connection

from wtforms import Form, TextField, validators, PasswordField, BooleanField
from passlib.hash import sha256_crypt
#from MySQLdb import escape_string as thwart
from functools import wraps

import gc

from webapp import get_job_ads


@app.route("/", methods = ["GET", "POST"])
def homepage():

    error = None
    job_categories = ['Ekonomi/juridik/inköp', 'Försäljning', 'Hotell/Resaurang', 'Industri/Tillverkning', 'IT', 'Kontor']

    try:

        query = request.form["search"]
        ads = get_job_ads.search(query)
        
        return render_template("main_results.html", ADS = ads, JOB_CATEGORIES = job_categories)
    
    except Exception as e:

        error = str(e)
        #return error
        return render_template("main.html", ERROR = error + "", JOB_CATEGORIES = job_categories)

@app.route("/omoss")
def about():
    return render_template("about.html")

@app.errorhandler(Exception)
def exception_handler(error):
    return repr(error)

@app.errorhandler(404)
def page_not_found(e):
    return("four oh four")

