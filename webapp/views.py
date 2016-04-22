from webapp import app

from flask import Flask, render_template, request, url_for, redirect, session
from dbconnect import connection

from wtforms import Form, TextField, validators, PasswordField, BooleanField
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
from functools import wraps

import gc

import platsannonser


@app.route("/", methods = ["GET", "POST"])
def homepage():

    error = None

    try:

        query = request.form["search"]
        ads = platsannonser.search(query)

        return render_template("main.html", ADS = ads)
    
    except Exception as e:

        error = str(e)
        #return error
        return render_template("main.html", ERROR = error)

@app.errorhandler(Exception)
def exception_handler(error):
    return repr(error)

@app.errorhandler(404)
def page_not_found(e):
    return("four oh four")

