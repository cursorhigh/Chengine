from asyncio import exceptions
from tkinter import *
import tkinter as tk
import webbrowser
import signup
import login
import os
import sys
import lead
import gistyc
import gamelist
import cred
from tkinter import messagebox
from tkinter.messagebox import askyesno
import pandas as pd
def mainig():
    def trigcred():
        cred.rcred()
    def img_resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    gist_api = gistyc.GISTyc(auth_token='<auth_token_here>')
    def labdo():
        try:
            try:
                os.remove('user')
                os.rename('userdata','user')
                os.rename('user','userdata')
                lead.ldod()
            except:
                os.rename('userdata','user')
                os.rename('user','userdata')
                lead.ldod()
        except :
            messagebox.showinfo(parent=window,title="Log in status",message="Please Log in to View Leaderboard")        
    def gamop():
        try:
            os.rename('userdata','user')
            os.rename('user','userdata')
            gamelist.gmain()
        except:
            messagebox.showinfo(parent=window,title="Log in status",message="Please Log in to Play Games") 
        
    def btn_clicked():
        print('lol')
    def Close():
        os.system("taskkill /f /im chengine.exe")
        window.destroy()
        sys.exit()
    def forms():
        webbrowser.open("https://forms.gle/VkHR9uCtkb4FYA6S8")
    def discord():
        webbrowser.open('https://discord.gg/QbWru2bFtf')
    def myt():
            webbrowser.open('https://youtube.com/playlist?list=PLht9SD0-LyQLGnW2bdHGIqf4Ni55PuoFx')

    def rebon():
        try:
            os.rename('userdata','user')
            os.rename('user','userdata')
            messagebox.showinfo(parent=window,title="Log in status",message="You're already logged in! logout to login again")
        except:
            login.ilog()
    def lout():
        try:
            os.remove('userdata')
            messagebox.showinfo(parent=window,title="Log out status",message="Logged out successfully!")
        
        except:
            messagebox.showinfo(parent=window,title="Log in status",message="You're already logged out!")

    window = Toplevel()
    window.title('Cursor High')
    window.overrideredirect(True)
    window.geometry("1280x720")
    window.configure(bg = "#000000")
    #window.state('zoomed')
    u1=''
    p1=''

    def center_screen():
            """ gets the coordinates of the center of the screen """
            global screen_height, screen_width, x_cordinate, y_cordinate
     
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
            x_cordinate = int((screen_width/2) - (1280/2))
            y_cordinate = int((screen_height/2) - (720/2))
            window.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))
     
    center_screen()
    canvas = Canvas(
        window,
        bg = "#000000",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("hbg.png"))
    background = canvas.create_image(
        640.0, 363.5,
        image=background_img)

    img0 = PhotoImage(file =img_resource_path("exit.png"))
    ext= Button(window,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = Close,
        relief = "flat")

    ext.place(
        x = 1174, y = 627,
        width = 88,
        height = 69)
    ytim = PhotoImage(file = img_resource_path("nytb.png"))
    ytb = Button(window,
        image = ytim,
        borderwidth = 0,
        highlightthickness = 0,
        command = myt,
        relief = "flat")

    ytb.place(
        x = 1183, y = 365,
        width = 62,
        height = 43)
    img1 = PhotoImage(file =img_resource_path("mail.png"))
    mail= Button(window,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = forms,
        relief = "flat")

    mail.place(
        x = 1174, y = 540,
        width = 83,
        height = 69)

    img2 = PhotoImage(file =img_resource_path("discord.png"))
    dis = Button(window,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = discord,
        relief = "flat")

    dis.place(
        x = 1167, y = 429,
        width = 99,
        height = 93)

    img3 = PhotoImage(file =img_resource_path("img3.png"))
    b3 = Button(window,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = trigcred,
        relief = "flat")

    b3.place(
        x = 550, y = 579,
        width = 166,
        height = 73)

    img4 = PhotoImage(file =img_resource_path("llimg.png"))
    lbod = Button(window,
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = labdo,
        relief = "flat")

    lbod.place(
        x = 496, y = 508,
        width = 272,
        height = 65)

    img5 = PhotoImage(file =img_resource_path("img5.png"))
    gam = Button(window,
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = gamop,
        relief = "flat")

    gam.place(
        x = 566, y = 430,
        width = 138,
        height = 62)

    img6 = PhotoImage(file =img_resource_path("img6.png"))
    b6 = Button(window,
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = lout,
        relief = "flat")

    b6.place(
        x = 556, y = 348,
        width = 157,
        height = 70)

    img7 = PhotoImage(file =img_resource_path("img7.png"))
    b7 = Button(window,
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command =rebon,
        relief = "flat")
    b7.place(
        x = 571, y = 273,
        width = 130,
        height = 67)

    img8 = PhotoImage(file =img_resource_path("img8.png"))
    b8 = Button(window,
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = signup.sig,
        relief = "flat")

    b8.place(
        x = 557, y = 199,
        width = 156,
        height = 66)

    window.resizable(False, False)
    window.mainloop()
