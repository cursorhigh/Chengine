
from tkinter import *
import os
import webbrowser
from datetime import datetime
import pandas as pd
from tkinter import messagebox
import gistyc
from tkinter.messagebox import askyesno
global gist_api
import sys
def myt():
        webbrowser.open('https://youtube.com/playlist?list=PLht9SD0-LyQLGnW2bdHGIqf4Ni55PuoFx')
def img_resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
gist_api = gistyc.GISTyc(auth_token='<auth_token_here>')
def procap():
    def btn_clicked():
        print("Button Clicked")
    def Close():
        cap.destroy()
    def clear(gen):
        gen.delete("0","end")
    def forms():
        webbrowser.open("https://forms.gle/VkHR9uCtkb4FYA6S8")
    def discord():
        webbrowser.open('https://discord.gg/QbWru2bFtf')
    def chain():
        try:
            try:
                os.remove('user.csv')
                os.rename('userdata','user.csv')
                os.rename('user.csv','userdata')
            except:
                os.rename('userdata','user.csv')
                os.rename('user.csv','userdata')
            global opa,npa
            opa=str(oldp.get())
            npa=str(newp.get())
            if len(npa)!=0:
                try:
                    os.rename('userdata','user.csv')
                except:
                    pass
                nt=pd.read_csv('user.csv')
                u=str(nt.loc[0,'0'])
                gist_list = gist_api.get_gists()
                tm=gist_list[5]['files']['dbase.csv']['raw_url']
                t=pd.read_csv(tm)
                d=t[t['user']==u].index.values
                op=t.loc[d,'password'].values
                os.rename('user.csv','userdata')
                if opa==op and op!=npa:
                    t.loc[d,'password']=npa
                    t.to_csv('dbase.csv',index=False)
                    response_update_data = gist_api.update_gist(file_name='dbase.csv')
                    os.rename('dbase.csv','cache')
                    os.remove('cache')
                    os.remove('userdata')
                    messagebox.showinfo(parent=cap,title="password status changed",message="change complete ,login again")
                    Close()
                if opa!=op and op!=npa:
                    messagebox.showwarning(parent=cap,title="password status Unchanged",message="Incorrect old password,Try again")
                    clear(oldp)
                if opa==op and op==npa:
                    messagebox.showwarning(parent=cap,title="password status Unchanged",message="New password can't be same as old,Try again")
                    clear(newp)
                if opa!=op and op==npa:
                    messagebox.showwarning(parent=cap,title="password status Unchanged",message="old or new password are same or wrong,Try again")
                    clear(oldp)
                    clear(newp)
            if len(npa)==0:
                    messagebox.showwarning(parent=cap,title="status",message="New password cannot be left empty!")
        except:
            messagebox.showwarning(parent=cap,title="status",message="Please Login to change password!")
            Close
            
    cap = Toplevel()

    cap.geometry("1280x720")
    cap.overrideredirect(True)
    cap.configure(bg = "#000000")
    def center_screen():
        global screen_height, screen_width, x_cordinate, y_cordinate
        screen_width = cap.winfo_screenwidth()
        screen_height = cap.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (1280/2))
        y_cordinate = int((screen_height/2) - (720/2))
        cap.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))
        
    center_screen()
    canvas = Canvas(
        cap,
        bg = "#000000",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("pasres.png"))
    background = canvas.create_image(
        640.0, 363.5,
        image=background_img)
    ytim = PhotoImage(file = img_resource_path("nytb.png"))
    ytb = Button(cap,
        image = ytim,
        borderwidth = 0,
        highlightthickness = 0,
        command = myt,
        relief = "flat")

    ytb.place(
        x = 1183, y = 365,
        width = 62,
        height = 43)
    img0 = PhotoImage(file =img_resource_path("exit.png"))
    ext = Button(cap,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = Close,
        relief = "flat")

    ext.place(
        x = 1174, y = 627,
        width = 88,
        height = 69)

    img1 = PhotoImage(file =img_resource_path("mail.png"))
    mail = Button(cap,
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
    dis = Button(cap,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = discord,
        relief = "flat")

    dis.place(
        x = 1167, y = 429,
        width = 99,
        height = 93)

    entry0_img = PhotoImage(file =img_resource_path("ptbo.png"))
    entry0_bg = canvas.create_image(
        506.5, 399.5,
        image = entry0_img)

    oldp = Entry(cap,font=('Open Sans',20),
        fg = '#ffffff',
        bd = 0,
        bg = "#170423",
        highlightthickness = 0)

    oldp.place(
        x = 308.0, y = 360,
        width = 397.0,
        height = 77)

    entry1_img = PhotoImage(file =img_resource_path("ptbn.png"))
    entry1_bg = canvas.create_image(
        506.5, 519.0,
        image = entry1_img)

    newp = Entry(cap,font=('Open Sans',20),
        fg = '#ffffff',
        bd = 0,
        bg = "#170423",
        highlightthickness = 0)

    newp.place(
        x = 308.0, y = 478,
        width = 397.0,
        height = 80)

    img3 = PhotoImage(file =img_resource_path("subt.png"))
    submit = Button(cap,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = chain,
        relief = "flat")

    submit.place(
        x = 813, y = 393,
        width = 202,
        height = 113)
    cap.grab_set()
    cap.resizable(False, False)
    cap.mainloop()
