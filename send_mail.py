import smtplib
from dotenv import load_dotenv
load_dotenv()
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

username = os.environ.get('User')
password = os.environ.get('Password')

def send_mail(text = 'Email body', subject = 'Hello world', from_email = 'Ivy Roman <lifeoftheromanivy@gmail.com>', to_emails = None, html = None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)


    msg_str = msg.as_string() 
    
    with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_emails, msg_str)
        