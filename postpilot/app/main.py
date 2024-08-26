from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("pages/home.html")


if __name__ == "__main__":
    app.run(debug=True)