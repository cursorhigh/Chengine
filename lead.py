from asyncio import exceptions
from tkinter import *
import sys
import os
import webbrowser
import pandas as pd
from tkinter import messagebox
import gistyc
import acset
def myt():
        webbrowser.open('https://youtube.com/playlist?list=PLht9SD0-LyQLGnW2bdHGIqf4Ni55PuoFx')
gist_api = gistyc.GISTyc(auth_token='<auth_token_here>')
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def ldod():
    def Close():
        lead.destroy()
    def forms():
        webbrowser.open("https://forms.gle/VkHR9uCtkb4FYA6S8")
    def discord():
        webbrowser.open('https://discord.gg/QbWru2bFtf')
    def raset():
        try:
            try:
                os.remove('user.csv')
                os.rename('userdata','user.csv')
                os.rename('user.csv','userdata')
                acset.aset()
            except:
                os.rename('userdata','user.csv')
                os.rename('user.csv','userdata')
                acset.aset()
        except:
            messagebox.showwarning(parent=lead,title="status",message="Please Login to change Account setings!")
            Close()
    lead = Toplevel()
    lead.overrideredirect(True)
    lead.geometry("1280x720")
    lead.configure(bg = "#000000")
    def center_screen():
        global screen_height, screen_width, x_cordinate, y_cordinate
        screen_width = lead.winfo_screenwidth()
        screen_height = lead.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (1280/2))
        y_cordinate = int((screen_height/2) - (720/2))
        lead.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))

    center_screen()
    canvas = Canvas(
        lead,
        bg = "#000000",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("lebg.png"))
    background = canvas.create_image(
        640.0, 363.5,
        image=background_img)

    img0 = PhotoImage(file =img_resource_path("exit.png"))
    ext = Button(lead,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = Close,
        relief = "flat")

    ext.place(
        x = 1174, y = 626,
        width = 88,
        height = 69)
    ytim = PhotoImage(file = img_resource_path("nytb.png"))
    ytb = Button(lead,
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
    mail = Button(lead,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = forms,
        relief = "flat")

    mail.place(
        x = 1174, y = 539,
        width = 83,
        height = 69)

    img2 = PhotoImage(file =img_resource_path("discord.png"))
    dis = Button(lead,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = discord,
        relief = "flat")
    img3 = PhotoImage(file =img_resource_path("acs.png"))
    b3 = Button(lead,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command =raset,
        relief = "flat")

    b3.place(
        x = 1056, y = 23,
        width = 200,
        height = 190)
    dis.place(
        x = 1167, y = 428,
        width = 99,
        height = 93)
    gist_list = gist_api.get_gists()
    jm=gist_list[5]['files']['dbase.csv']['raw_url']
    kt=pd.read_csv(jm)
    kt=kt.sort_values('Online WINs',ascending=False)
    kt[kt.columns[0]]=range(1,len(kt)+1)
    kt.index=range(0,len(kt))
    kt=kt[0:10]
    kt.drop('password',inplace=True,axis=1)
    kt.drop('doc',inplace=True,axis=1)
    kt.drop('ls',inplace=True,axis=1)
    lst=[("RANK","USER","Online Win","Offline Win","Total Win")]
    for x in range(0,len(kt)):
        lst.append(tuple(kt.loc[x]))
    total_rows = len(lst)
    total_columns = len(lst[0])
    for i in range(total_rows):
        for j in range(total_columns):      
            e = Entry(lead, width=10, fg='White',bg='black',disabledforeground="white",disabledbackground="black",
                        font=('Teko',19,'bold'))
            e.grid(row=i, column=j+200)
            e.place(x=j*140+285,y=i*34+280)
            e.insert(END, lst[i][j])
            e.config(state= "disabled")
    lead.resizable(False, False)
    lead.mainloop()
