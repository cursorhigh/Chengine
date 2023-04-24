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
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def clear(gen):
    gen.delete("0","end")
def sig():    
    global gist_api
    gist_api = gistyc.GISTyc(auth_token='<auth_token_here>')
    def Close():
        swindow.destroy()
    def forms():
        webbrowser.open("https://forms.gle/VkHR9uCtkb4FYA6S8")
    def discord():
        webbrowser.open('https://discord.gg/QbWru2bFtf')
    def confirm():
        answer = askyesno(parent=swindow,title='someting went wrong..',
                        message='Sign up Failed! user already exist,Want to get to dashboard?')
        if answer:
            swindow.destroy()
        else:
            clear(user)
            clear(password)
            
    def meca():
        global u,p
        p=password.get()
        u=user.get()
        if len(p)!=0 and len(u)!=0:
            gist_list = gist_api.get_gists()
            tm=gist_list[5]['files']['dbase.csv']['raw_url']
            t=pd.read_csv(tm)       
            a=[]
            for x in t['user']:
                a.append(x)
            if u in a:
                confirm()
            if u not in a :
                now = datetime.now()
                dooc = now.strftime("%d/%m/%Y %H:%M:%S")
                q=len(t)
                t.loc[q,'user']=u
                t.loc[q,'rank']=int(q+1)
                t.loc[q,'doc']=dooc
                t.loc[q,'ls']=0
                t.loc[q,'Online WINs']=0
                t.loc[q,'Offline WINs']=0
                t.loc[q,'TOTAL WINs']=0
                t.loc[q,'password']=p
                t.to_csv('dbase.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dbase.csv')
                os.rename('dbase.csv','cache')
                os.remove('cache')
                messagebox.showinfo(parent=swindow,title="Sign up status",message="Signned up successfull!")
                swindow.destroy()
        if len(p)==0 or len(u)==0:
            messagebox.showwarning(parent=swindow,title="Sign up status",message="User or Password cannot be left empty!")

    swindow = Toplevel()
    swindow.overrideredirect(True)
    swindow.geometry("1280x720")
    swindow.configure(bg = "#000000")
    def center_screen():
        global screen_height, screen_width, x_cordinate, y_cordinate
        screen_width = swindow.winfo_screenwidth()
        screen_height = swindow.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (1280/2))
        y_cordinate = int((screen_height/2) - (720/2))
        swindow.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))
 
    center_screen()
    scanvas = Canvas(
        swindow,
        bg = "#000000",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    scanvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("signbg.png"))
    background = scanvas.create_image(
        640.0, 363.5,
        image=background_img)

    entry0_img = PhotoImage(file =img_resource_path("signptb.png"))
    entry0_bg = scanvas.create_image(
        639.5, 437.0,
        image = entry0_img)

    password = Entry(swindow,font=('Open Sans',20),
        fg = '#ffffff',
        bd = 0,
        bg = "#191919",
        highlightthickness = 0)

    password.place(
        x = 490.0, y = 406,
        width = 299.0,
        height = 60)

    entry1_img = PhotoImage(file =img_resource_path("signutb.png"))
    entry1_bg = scanvas.create_image(
        638.5, 307.0,
        image = entry1_img)

    user = Entry(swindow,font=('Open Sans',20),
        fg = '#ffffff',
        bd = 0,
        bg = "#191919",
        highlightthickness = 0)
    
    user.place(
        x = 489.0, y = 276,
        width = 299.0,
        height = 60)
    img0 = PhotoImage(file =img_resource_path("exit.png"))
    ext = Button(swindow,
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
    ytb = Button(swindow,
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
    mail = Button(swindow,
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
    dis = Button(swindow,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = discord,
        relief = "flat")

    dis.place(
        x = 1167, y = 429,
        width = 99,
        height = 93)

    img3 = PhotoImage(file =img_resource_path("signbutton.png"))
    sign = Button(swindow,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = meca,
        relief = "flat")

    sign.place(
        x = 540, y = 498,
        width = 203,
        height = 104)
    swindow.grab_set()
    swindow.resizable(False, False)
    swindow.mainloop()
