import smtplib
from tkinter import *

def connect(self):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        print('Server connected!')
    except:
        print('Could not connect to Gmail server!')


def send_mail(self):
    user = input('Enter your user ID: ')
    passwd = input('Enter your password: ')
    receiver_id = input('Enter the receiver ID: ')
    msg = input('\nEnter the message do you want to send: ')

    try:
        server.login(user, passwd)
        print('Login successful!')
    except:
        print('Allow Less secure apps in GOOGLE ACCOUNT SETTINGS to use SMTP services')
        server.quit()
        exit()

    server.sendmail(user, receiver_id, msg)
    print('Your mail was sent!')


    print('Closing connection!')
    server.quit()
    print('Closed.')