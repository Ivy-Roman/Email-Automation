import email
import sys 
from formatting import format_msg
from send_mail import send_mail

def send(name, website=None, Verbose = False, to_email=None):
    assert to_email != None
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if Verbose:
        print(name,website,to_email)

    send_mail(text = msg, to_emails=[to_email], html=None)

# if __name__ == "__main__":
#     print(sys.argv)
#     name = "Unknown"
#     if len(sys.argv) > 1:
#         name = sys.argv[1]
#     email = None
#     if len(sys.argv) > 2:
#         email = sys.argv[2]
#     response = send(name, to_email=email, Verbose=True)
#     print(response)

d = dict()
with open("Test_Emails.csv") as f:
    for line in f:
        line = line.strip('\n')
        (key, val) = line.split(",")
        d[key] = val
print (d)

for key, val in d.items():
    send(name = key, to_email=val)
print ('Done')