from tkinter import *
import sys
import os
import webbrowser
from tkinter.messagebox import askyesno
def rcred():
        def myt():
                webbrowser.open('https://youtube.com/playlist?list=PLht9SD0-LyQLGnW2bdHGIqf4Ni55PuoFx')
        def Close():
                cred.destroy()
        def forms():
            webbrowser.open("https://forms.gle/VkHR9uCtkb4FYA6S8")
        def discord():
            webbrowser.open('https://discord.gg/QbWru2bFtf')
        def btn_clicked():
            print("Button Clicked")
        def img_resource_path(relative_path):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        cred = Toplevel()
        cred.overrideredirect(True)
        cred.geometry("1280x720")
        cred.configure(bg = "#000000")
        def center_screen():
            global screen_height, screen_width, x_cordinate, y_cordinate
            screen_width = cred.winfo_screenwidth()
            screen_height = cred.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (1280/2))
            y_cordinate = int((screen_height/2) - (720/2))
            cred.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))

        center_screen()
        canvas = Canvas(
            cred,
            bg = "#000000",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file =  img_resource_path("crebg.png"))
        background = canvas.create_image(
            640.0, 360.0,
            image=background_img)

        img0 = PhotoImage(file =  img_resource_path("cexit.png"))
        ext = Button(cred,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Close,
            relief = "flat")

        ext.place(
            x = 1174, y = 627,
            width = 88,
            height = 69)

        img1 = PhotoImage(file =  img_resource_path("cmail.png"))
        mail = Button(cred,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = forms,
            relief = "flat")

        mail.place(
            x = 1174, y = 540,
            width = 83,
            height = 69)

        img2 = PhotoImage(file =  img_resource_path("cdis.png"))
        dis = Button(cred,
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = discord,
            relief = "flat")

        dis.place(
            x = 1167, y = 429,
            width = 99,
            height = 93)
        ytim = PhotoImage(file = img_resource_path("nytb.png"))
        ytb = Button(cred,
            image = ytim,
            borderwidth = 0,
            highlightthickness = 0,
            command = myt,
            relief = "flat")

        ytb.place(
            x = 1183, y = 365,
            width = 62,
            height = 43)
        cred.resizable(False, False)
        cred.mainloop()
