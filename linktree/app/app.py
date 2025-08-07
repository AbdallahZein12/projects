from flask import Flask, render_template

app = Flask(__name__)

# Example data: replace with your actual info
profile = {
    "name": "Abdallah Abdelmoneim",
    "bio": "Data Engineer | Fed Intern | Macro Enjoyer",
    "avatar": "/static/pfp.jpeg",  # Change this to your image URL
    "links": [
        {"name": "Resume", "url": "https://docs.google.com/document/d/1ebHeu6Cnu3tR0tHj0ldb2QFXTETQ3qdcqcBzbBciGk0/edit?usp=sharing"},
        {"name": "GitHub", "url": "https://github.com/AbdallahZein12"},
        {"name": "LinkedIn", "url": "https://linkedin.com/in/abdallah-abdel"},
        {"name": "Email", "url": "mailto:abdallahabdelmoneim7@gmail.com"},
        {"name": "LIU Club Website", "url": "https://liuclub.liucscs.us"},
    ]
}

@app.route("/")
def index():
    return render_template("index.html", profile=profile)
