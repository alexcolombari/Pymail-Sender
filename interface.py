import smtplib
import webbrowser
from tkinter import *

def main():

    def connect():
        #try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        print('Server connected!')
        msg_status.config(fg = 'green', text = 'Connected!')
        msg_status.place(relx = 0.44, y = 86)
        #except:
            #print('Could not connect to Gmail server!')

    root = Tk()
    root.title('Pymail Sender')
    root.geometry('700x500')
    root.resizable(False, False)
    windowWidth = 700
    windowHeight = 500
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))

    top_msg = Label(root, text = 'Welcome to Pymail Sender!')
    top_msg['font'] = ('Arial', '14')
    top_msg.pack()
    top_msg.place(relx = 0.33, rely = 0.03)

    btn_about = Button(root, text = 'About', width = 7, command = about)
    btn_about.pack()
    btn_about.place(x = 700 - 90, y = 10)

    # ----- BUTTON CONNECT / STATUS LABEL -----
    btn_connect = Button(root, text = 'Connect to server', command = connect)
    btn_connect.pack()
    btn_connect.place(relx = 0.39, y = 55)

    msg_status = Label(root, text = 'Disconnected', fg = 'red')
    msg_status.pack()
    msg_status.place(relx = 0.43, y = 86)
    
    return root

def about():

    def callback(url):
        webbrowser.open_new(url)
        
    window = Toplevel(root)
    window.title('About')
    window.geometry('200x130')
    window.resizable(False, False)

    windowWidth = 200
    windowHeight = 130
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
    window.geometry("+{}+{}".format(positionRight, positionDown))

    txt = Label(window, text = 'Created by:')
    txt.pack()
    txt.place(relx = 0.3, rely = 0.15)

    txt2 = Label(window, text = 'Alex Colombari')
    txt2.pack()
    txt2.place(relx = 0.25, rely = 0.42)

    txt3 = Label(window, text = 'github.com/alexcolombari', cursor = 'hand2')
    txt3['font'] = ('Arial', '11')
    txt3.pack()
    txt3.place(relx = 0.09, rely = 0.68)
    txt3.bind("<Button-1>", lambda e: callback("http://www.github.com/alexcolombari"))

    return window

root = main()
root.mainloop()