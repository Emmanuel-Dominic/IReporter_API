from os import environ

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = environ.get("MAIL_SERVER")
app.config['MAIL_PORT'] = environ.get("MAIL_PORT")
app.config['MAIL_USERNAME'] = environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = environ.get("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = environ.get("MAIL_USE_TLS")
app.config['MAIL_USE_SSL'] = environ.get("MAIL_USE_SSL")
mail = Mail(app)


def status_emailing(user_email, user_name, incident_Id, incident_status):
    msg = Message('Hello', sender='ireporterManuelDominic@gmail.com', recipients=[user_email])
    msg.body = "Hello {}, Incident's {} is {}. Thank you please.".format(user_name, incident_Id, incident_status)
    mail.send(msg)
    return "Email sent"
