from tkinter import *
import webbrowser
import os
import sys
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def spyt():
    def myt():
        webbrowser.open('https://youtube.com/playlist?list=PLht9SD0-LyQLG1xfG7gYeVuiy4KlZ3n_8')

    yt = Toplevel()

    yt.geometry("602x661")
    yt.configure(bg = "#000000")
    canvas = Canvas(
        yt,
        bg = "#000000",
        height = 661,
        width = 602,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file =img_resource_path("tbg.png"))
    background = canvas.create_image(
        305.5, 324.0,
        image=background_img)

    ytim = PhotoImage(file = img_resource_path("ytb.png"))
    ytb = Button(yt,
        image = ytim,
        borderwidth = 0,
        highlightthickness = 0,
        command = myt,
        relief = "flat")

    ytb.place(
        x = 269, y = 533,
        width = 62,
        height = 43)
    yt.grab_set()
    yt.resizable(False, False)
    yt.mainloop()
