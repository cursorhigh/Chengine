import base64
from tkinter import *
import sys
import os
import main
from tkinter import messagebox
def Close():
    os.system("taskkill /f /im chengine.exe")
    messagebox.showinfo(parent=splash,title='ah oh!',message="please rename the file to 'chengine.exe' and dont rename it")
def img_resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
try:
    splash = Tk()
    splash.iconbitmap(img_resource_path('new.ico'))
    splash.geometry("400x400")
    splash.title("Chengine")
    splash.configure(bg = "#FFFFFF")
    canvas = Canvas(
        splash,
        bg = "#FFFFFF",
        height = 400,
        width = 400,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("splbg.png"))
    background = canvas.create_image(
        200.0, 200.0,
        image=background_img)

    img0 = PhotoImage(file =img_resource_path("epi.png"))
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = Close,
        relief = "flat")

    b0.place(
        x = 97, y = 140,
        width = 201,
        height = 114)
    splash.iconify()
    try:
        main.mainig()
    except:
        exit()
    splash.resizable(False, False)
    splash.mainloop()
except:
    pass
