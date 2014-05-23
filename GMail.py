#!/usr/bin/env python
import smtplib
import datetime
from email.mime.text import MIMEText

#change to actual username, or use function below
user = 'username'
pwd = 'password'
now = datetime.datetime.now()
def email(fr, to, sub, mes): #function for sending email
    #set variables
    FROM = fr
    TO = to
    SUBJECT = sub
    TEXT = mes + '\n sent at: ' + str(now)

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

    print (message) #print the message
    s = smtplib.SMTP('smtp.gmail.com', 587) #connect to server
    s.ehlo()
    s.starttls()
    s.login(user, pwd) #login
    print('Connected') #print conformation
    s.sendmail(FROM,TO,message) #send message
    s.quit() #disconnect from server
    print('Finished') #print conformation of email being sent

def set_username(u): #set username
    global user
    user = u

def set_password(p): #set password
    global pwd
    pwd = p
