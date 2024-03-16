from flask import Flask, redirect, url_for, render_template, request
import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "longislanducs@gmail.com"
email_password = os.getenv("LIUCSPASS")

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
  if request.method == "POST":
    try:
      email_receiver = request.form["email"]
      name = email_receiver.split("@")[0]

      subject = "Invitation to LIUCS!"
      body = f""" Hello {name}!
            
            Thank you for your interest in joining us! Your invitation link is attached to this email below.

            LIU CS Club is a place for you to take on technical challenges and enhance your skills. We often post opportunities for internships and certifications for almost no cost at all for students at all levels. 

            We are glad to have you with us!
            
            ________________________
            
            INVITATION LINK
            
            https://discord.gg/BhfdJWCdJC
            
            ________________________
            
            Passionately from LIUCS & ZeinDev 
            """

      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_receiver
      em['Subject'] = subject
      em.set_content(body)
      context = ssl.create_default_context()

      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

      Success = "Invitation was sent successfully!"
    except Exception as er:
      Success = f"Error: {er}"

    return render_template("index.html")
  else:
    return render_template("index.html")


@app.route("/about", methods=["POST", "GET"])
def about():
  if request.method == "POST":
    try:
      email_receiver = request.form["email"]
      name = email_receiver.split("@")[0]

      subject = "Invitation to LIUCS!"
      body = f""" Hello {name}!
            
            Thank you for your interest in joining us! Your invitation link is attached to this email below.

            LIU CS Club is a place for you to take on technical challenges and enhance your skills. We often post opportunities for internships and certifications for almost no cost at all for students at all levels. 

            We are glad to have you with us!
            
            ________________________
            
            INVITATION LINK
            
            https://discord.gg/BhfdJWCdJC
            
            ________________________
            
            Passionately from LIUCS & ZeinDev 
            """

      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_receiver
      em['Subject'] = subject
      em.set_content(body)
      context = ssl.create_default_context()

      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

      Success = "Invitation was sent successfully!"
    except Exception as er:
      Success = f"Error: {er}"

    return render_template("about.html")
  else:
    return render_template("about.html")


@app.route("/calendar", methods=["POST", "GET"])
def calendar():
  if request.method == "POST":
    try:
      email_receiver = request.form["email"]
      name = email_receiver.split("@")[0]

      subject = "Invitation to LIUCS!"
      body = f""" Hello {name}!
            
            Thank you for your interest in joining us! Your invitation link is attached to this email below.

            LIU CS Club is a place for you to take on technical challenges and enhance your skills. We often post opportunities for internships and certifications for almost no cost at all for students at all levels. 

            We are glad to have you with us!
            
            ________________________
            
            INVITATION LINK
            
            https://discord.gg/BhfdJWCdJC
            
            ________________________
            
            Passionately from LIUCS & ZeinDev 
            """

      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_receiver
      em['Subject'] = subject
      em.set_content(body)
      context = ssl.create_default_context()

      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

      Success = "Invitation was sent successfully!"
    except Exception as er:
      Success = f"Error: {er}"

    return render_template("calendar.html")
  else:
    return render_template("calendar.html")


@app.route("/contributions", methods=["POST", "GET"])
def contributions():
  if request.method == "POST":
    try:
      email_receiver = request.form["email"]
      name = email_receiver.split("@")[0]

      subject = "Invitation to LIUCS!"
      body = f""" Hello {name}!
            
            Thank you for your interest in joining us! Your invitation link is attached to this email below.

            LIU CS Club is a place for you to take on technical challenges and enhance your skills. We often post opportunities for internships and certifications for almost no cost at all for students at all levels. 

            We are glad to have you with us!
            
            ________________________
            
            INVITATION LINK
            
            https://discord.gg/BhfdJWCdJC
            
            ________________________
            
            Passionately from LIUCS & ZeinDev 
            """

      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_receiver
      em['Subject'] = subject
      em.set_content(body)
      context = ssl.create_default_context()

      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

      Success = "Invitation was sent successfully!"
    except Exception as er:
      Success = f"Error: {er}"

    return render_template("contributions.html")
  else:
    return render_template("contributions.html")


@app.route("/resources", methods=["POST", "GET"])
def resources():
  if request.method == "POST":
    try:
      email_receiver = request.form["email"]
      name = email_receiver.split("@")[0]

      subject = "Invitation to LIUCS!"
      body = f""" Hello {name}!
            
            Thank you for your interest in joining us! Your invitation link is attached to this email below.

            LIU CS Club is a place for you to take on technical challenges and enhance your skills. We often post opportunities for internships and certifications for almost no cost at all for students at all levels. 

            We are glad to have you with us!
            
            ________________________
            
            INVITATION LINK
            
            https://discord.gg/BhfdJWCdJC
            
            ________________________
            
            Passionately from LIUCS & ZeinDev 
            """

      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_receiver
      em['Subject'] = subject
      em.set_content(body)
      context = ssl.create_default_context()

      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

      Success = "Invitation was sent successfully!"
    except Exception as er:
      Success = f"Error: {er}"

    return render_template("resources.html")
  else:
    return render_template("resources.html")


if __name__ == "__main__":
  app.run()
