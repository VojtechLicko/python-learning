# import getpass  # to get password
# import imaplib
import smtplib

# simple mail transfer protocol
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()

email = input("Enter your email : ")
password = input("Password please :")
smtp_object.login(email, password)
from_address = email
to_address = email
subject = input("Enter the subject line :")
message = input("Enter the message")
msg = "Subject: " + subject+"\n"+message
smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()

# u can also explore your inbox
"""
M = imaplib.IMAP4_SSL('imap.gmail.com')

user = input("Enter your email: ")
# Remember , you may need an app password if you are a gmail user
#
password = getpass.getpass("Enter your password: ")
M.login(user, password)
M.list()
M.select("inbox")
typ ,data = M.search(None,'SUBJECT "this is a test email for python"')
We can now save what it has returned:

typ
'OK'
data
[b'28298']
The data will be a list of unique ids.

# typ, data = M.fetch(data[0],"(RFC822)")
result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
We can use the built in email library to help parse this raw string.

import email
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
"""
