from email.message import EmailMessage

import ssl
import smtplib
## This is the password of the email address that will be Gmail generated password
password=""
## This is the email address that will be used to send the email
email_sender=''

## This is the email address that will receive the email
email_reciver=''
subject="YOUR SUBJECT"
body="""
YOUR MESSAGE
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_reciver
em['Subject']=subject
em.set_content(body)


context= ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,email_reciver,em.as_string())