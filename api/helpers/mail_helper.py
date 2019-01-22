
from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ireporterManuelDominic@gmail.com'
app.config['MAIL_PASSWORD'] = 'Godiswithusmatmanuel1'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def status_emailing(user_email,user_name,incident_Id,incident_status):
   msg = Message('Hello', sender = 'ireporterManuelDominic@gmail.com', recipients = [user_email])
   msg.body = "Hello {}, Incident's {} is {}. Thank you please.".format(user_name,incident_Id,incident_status)
   mail.send(msg)
   return  "Email sent"

