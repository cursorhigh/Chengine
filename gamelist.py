from tkinter import *
import sys
import os
import webbrowser
from datetime import datetime
import pandas as pd
from tkinter import messagebox
import gistyc
from tkinter.messagebox import askyesno
import xaim
import ofxo
import cmg
def myt():
        webbrowser.open('https://youtube.com/playlist?list=PLht9SD0-LyQLGnW2bdHGIqf4Ni55PuoFx')
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def btn_clicked():
    print("Button Clicked")
def Close():
        glist.destroy()
def forms():
    webbrowser.open("https://forms.gle/VkHR9uCtkb4FYA6S8")
def discord():
    webbrowser.open('https://discord.gg/QbWru2bFtf')
def triger1():
    xaim.tttmp()
def triger2():
    ofxo.ofaim()
def triger3():
    cmg.cdgame()
def gmain():
    global glist
    glist = Toplevel()
    glist.geometry("1280x720")
    glist.overrideredirect(True)
    glist.configure(bg = "#000000")
    def center_screen():
        global screen_height, screen_width, x_cordinate, y_cordinate
        screen_width = glist.winfo_screenwidth()
        screen_height = glist.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (1280/2))
        y_cordinate = int((screen_height/2) - (720/2))
        glist.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))

    center_screen()
    canvas = Canvas(
        glist,
        bg = "#000000",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("glbg.png"))
    background = canvas.create_image(
        640.0, 358.5,
        image=background_img)

    img0 = PhotoImage(file =img_resource_path("exit.png"))
    ext = Button(glist,
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
    ytb = Button(glist,
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
    mail = Button(glist,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command =forms,
        relief = "flat")

    mail.place(
        x = 1174, y = 540,
        width = 83,
        height = 69)

    img2 = PhotoImage(file =img_resource_path("discord.png"))
    dis = Button(glist,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = discord,
        relief = "flat")

    dis.place(
        x = 1167, y = 429,
        width = 99,
        height = 93)

    img3 = PhotoImage(file =img_resource_path("ttton.png"))
    tttmp = Button(glist,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = triger1,
        relief = "flat")

    tttmp.place(
        x = 138, y = 283,
        width = 400,
        height = 61)

    img4 = PhotoImage(file =img_resource_path("tttof.png"))
    ttsp = Button(glist,
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = triger2,
        relief = "flat")

    ttsp.place(
        x = 138, y = 360,
        width = 400,
        height = 61)
    img5 = PhotoImage(file =img_resource_path("cm.png"))
    cm = Button(glist,
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = triger3,
        relief = "flat")

    cm.place(
        x = 146, y = 429,
        width = 390,
        height = 55)
    glist.grab_set()
    glist.resizable(False, False)
    glist.mainloop()
