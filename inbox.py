import imaplib
import email
from dotenv import load_dotenv
from pip import main
load_dotenv()
import os

host = 'imap.gmail.com'
username = os.environ.get('User')
password = os.environ.get('Password')

def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select('inbox')
    _, search_data = mail.search(None, 'UNSEEN')

    my_message = []
    for num in search_data[0].split():
        email_data = {}
        print(num)
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
    return my_message

if __name__ == '__main__':
    my_inbox = get_inbox()
    print(my_inbox)