
from tkinter import *
import sys
import os
import cap
import webbrowser
from datetime import datetime
import pandas as pd
from tkinter import messagebox
import gistyc
from tkinter.messagebox import askyesno
global gist_api
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
def aset():
    def btn_clicked():
        print("Button Clicked")
    def Close():
        acs.destroy()
    def forms():
        webbrowser.open("https://forms.gle/VkHR9uCtkb4FYA6S8")
    def discord():
        webbrowser.open('https://discord.gg/QbWru2bFtf')
    def capt():
        try:
            try:
                os.remove('user.csv')
                os.rename('userdata','user.csv')
                os.rename('user.csv','userdata')
                cap.procap()
            except:
                os.rename('userdata','user.csv')
                os.rename('user.csv','userdata')
                cap.procap()
        except:
            messagebox.showwarning(parent=acs,title="status",message="Please Login to change password!")
            Close()
    def Sug():
        webbrowser.open('https://forms.gle/8p8yzu7LtdW1oYPG8')
    def delac():
        try:
            try:
                os.remove('user.csv')
                os.rename('userdata','user.csv')
                os.rename('user.csv','userdata')
            except:
                os.rename('userdata','user.csv')
                os.rename('user.csv','userdata')
            answer = askyesno(parent=acs,title='Account Warning !',
                            message='Deletion of Account is Permanent, want to continue ? ')
            if answer:
                try:
                    os.rename('userdata','user.csv')
                except:
                    pass
                geb=pd.read_csv("user.csv")
                gist_list = gist_api.get_gists()
                tm=gist_list[5]['files']['dbase.csv']['raw_url']
                n=pd.read_csv(tm)
                u=str(geb.loc[0,'0'])
                dein=n.index[n['user']==u].values
                n=n.drop(int(dein))
                n.to_csv('dbase.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dbase.csv')
                os.rename('dbase.csv','cache')
                os.remove('cache')
                os.rename('user.csv','cache')
                os.remove('cache')
                messagebox.showinfo(parent=acs,title="status",message="Account Deleted Successfully!")
                Close()
            else:
                pass
            
        except :
            messagebox.showinfo(parent=acs,title="status",message="Please Log in to Delete Account")
            Close()
    acs = Toplevel()
    acs.overrideredirect(True)
    acs.geometry("1280x720")
    acs.configure(bg = "#000000")
    def center_screen():
        global screen_height, screen_width, x_cordinate, y_cordinate
        screen_width = acs.winfo_screenwidth()
        screen_height = acs.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (1280/2))
        y_cordinate = int((screen_height/2) - (720/2))
        acs.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))
        
    center_screen()
    canvas = Canvas(
        acs,
        bg = "#000000",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("acsbg.png"))
    background = canvas.create_image(
        640.0, 363.5,
        image=background_img)

    img0 = PhotoImage(file =img_resource_path("exit.png"))
    ext = Button(acs,
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
    mail = Button(acs,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = forms,
        relief = "flat")

    mail.place(
        x = 1174, y = 540,
        width = 83,
        height = 69)
    ytim = PhotoImage(file = img_resource_path("nytb.png"))
    ytb = Button(acs,
        image = ytim,
        borderwidth = 0,
        highlightthickness = 0,
        command = myt,
        relief = "flat")

    ytb.place(
        x = 1183, y = 365,
        width = 62,
        height = 43)
    img2 = PhotoImage(file =img_resource_path("discord.png"))
    dis = Button(acs,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = discord,
        relief = "flat")

    dis.place(
        x = 1167, y = 429,
        width = 99,
        height = 93)

    img3 = PhotoImage(file =img_resource_path("cap.png"))
    tcap = Button(acs,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = capt,
        relief = "flat")

    tcap.place(
        x = 143, y = 347,
        width = 461,
        height = 134)

    img4 = PhotoImage(file =img_resource_path("sug.png"))
    su = Button(acs,
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = Sug,
        relief = "flat")

    su.place(
        x = 676, y = 341,
        width = 460,
        height = 140)

    img5 = PhotoImage(file =img_resource_path("delac.png"))
    dea = Button(acs,
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = delac,
        relief = "flat")

    dea.place(
        x = 431, y = 509,
        width = 461,
        height = 134)
    acs.grab_set()
    acs.resizable(False, False)
    acs.mainloop()
