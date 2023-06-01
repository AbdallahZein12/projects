from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template("Index.html",content=name,r=2,list1=["tim","joe","bill"])


if __name__ == "__main__":
    app.run()