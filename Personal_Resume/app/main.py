from flask import Flask, render_template, url_for,redirect,request


app = Flask(__name__)

@app.route("/",methods=["GET"])
@app.route("/home",methods=["GET"])
def home():
    return render_template("home.html",output="")

@app.route("/more")
def more():
    return render_template("more.html")