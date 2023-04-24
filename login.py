from asyncio import exceptions
from tkinter import *
import sys
import os
import webbrowser
from datetime import datetime
import pandas as pd
from tkinter import messagebox
import gistyc
from tkinter.messagebox import askyesno
def myt():
        webbrowser.open('https://youtube.com/playlist?list=PLht9SD0-LyQLGnW2bdHGIqf4Ni55PuoFx')
global u,p
p=''
u=''
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def ilog():
    def clear(gen):
        gen.delete("0","end")
    global gist_api
    gist_api = gistyc.GISTyc(auth_token='<auth_token_here>')
    def btn_clicked():
        print("Button Clicked")
    def Close():
        lwindow.destroy()
    def forms():
        webbrowser.open("https://forms.gle/VkHR9uCtkb4FYA6S8")
    def discord():
        webbrowser.open('https://discord.gg/QbWru2bFtf')
    def confirm():
        answer = askyesno(parent=lwindow,title='someting went wrong..',
                        message='Log in Failed! user or password is incorrect,Want to get to dashboard?')
        if answer:
            lwindow.destroy()
        else:
            clear(user)
            clear(password)
    def loca():
        global u,p
        p=str(password.get())
        u=str(user.get())
        gist_list = gist_api.get_gists()
        tm=gist_list[5]['files']['dbase.csv']['raw_url']
        t=pd.read_csv(tm)       
        a=[]
        for x in t['user']:
            a.append(x)
        if u in a:
            d=t[t['user']==u].index.values
            gf=t.loc[d,'password'].values
            rk=t.loc[d,'rank'].values
            if p==gf:
                gm=gist_list[5]['files']['dbase.csv']['raw_url']
                n=pd.read_csv(gm)
                now = datetime.now()
                dooc = now.strftime("%d/%m/%Y %H:%M:%S")
                n.loc[n.index[n['user']==u].values,'ls']=dooc
                n.to_csv('dbase.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dbase.csv')
                df=pd.DataFrame(data=[])
                os.rename('dbase.csv','cache')
                os.remove('cache')
                df[0]=[u]
                df[1]=[p]
                df[3]=int(rk)
                df.to_csv('zi.csv',index=False)
                os.rename('zi.csv','userdata')
                messagebox.showinfo(parent=lwindow,title="Log in status",message="Logged in successfull!")
                lwindow.destroy()

            else:
                confirm()
        else:
            confirm()
    lwindow = Toplevel()
    lwindow.overrideredirect(True)
    lwindow.geometry("1280x720")
    lwindow.configure(bg = "#000000")
    def center_screen():
        global screen_height, screen_width, x_cordinate, y_cordinate
        screen_width = lwindow.winfo_screenwidth()
        screen_height = lwindow.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (1280/2))
        y_cordinate = int((screen_height/2) - (720/2))
        lwindow.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))
     
    center_screen()
    lcanvas = Canvas(
        lwindow,
        bg = "#000000",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    lcanvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("lbg.png"))
    background = lcanvas.create_image(
        640.0, 363.0,
        image=background_img)

    entry0_img = PhotoImage(file =img_resource_path("logptb.png"))
    entry0_bg = lcanvas.create_image(
        639.5, 437.0,
        image = entry0_img)

    password = Entry(lwindow,font=('Open Sans',20),
            fg = '#ffffff',
            bd = 0,
            bg = "#191919",
            highlightthickness = 0)

    password.place(
        x = 490.0, y = 406,
        width = 299.0,
        height = 60)

    entry1_img = PhotoImage(file =img_resource_path("logutb.png"))
    entry1_bg = lcanvas.create_image(
        638.5, 307.0,
        image = entry1_img)

    user = Entry(lwindow,font=('Open Sans',20),
            fg = '#ffffff',
            bd = 0,
            bg = "#191919",
            highlightthickness = 0)

    user.place(
        x = 489.0, y = 276,
        width = 299.0,
        height = 60)

    img0 = PhotoImage(file =img_resource_path("exit.png"))
    exit = Button(lwindow,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = Close,
        relief = "flat")

    exit.place(
        x = 1174, y = 627,
        width = 88,
        height = 69)
    ytim = PhotoImage(file = img_resource_path("nytb.png"))
    ytb = Button(lwindow,
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
    mail = Button(lwindow,
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
    dis = Button(lwindow,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = discord,
        relief = "flat")

    dis.place(
        x = 1167, y = 429,
        width = 99,
        height = 93)

    img3 = PhotoImage(file =img_resource_path("logbutton.png"))
    logi = Button(lwindow,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = loca,
        relief = "flat")

    logi.place(
        x = 540, y = 498,
        width = 203,
        height = 104)
    
    lwindow.grab_set()
    lwindow.resizable(False, False)
    lwindow.mainloop()


    
