from flask import Flask, redirect, url_for, render_template, request
import os
from email.message import EmailMessage
import ssl
import smtplib


app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/home", methods=[ "GET"])
def home():
  return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
  return render_template("about.html")


@app.route("/calendar", methods=["GET"])
def calendar():
  return render_template("calendar.html")


@app.route("/contributions", methods=["GET"])
def contributions():
  return render_template("contributions.html")


@app.route("/resources", methods=["GET"])
def resources():
  return render_template("resources.html")

@app.route("/underconstruction")
def underconstruction():
  return "<img src='https://kidsarefrompluto.files.wordpress.com/2012/08/fr.jpg?w=584' style='position:absolute; top:0; bottom:0; right:0; left:0; margin:auto;'>"
