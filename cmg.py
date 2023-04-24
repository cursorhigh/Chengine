from tkinter import *
import os
import time as t
from tkinter import *
import random 
import pandas as pd
from tkinter import messagebox
import gistyc
count = 0
ansl = []
ansd = {}
gist_api = gistyc.GISTyc(auth_token='<auth_token_here>')
import sys
def img_resource_path(relative_path):
        try:

        # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
        except Exception:
                base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
def cdgame():
        try:
                os.rename('userdata','gen.csv')
                gz=pd.read_csv("gen.csv")
                ny=str(gz.loc[0,'0'])
                os.rename('gen.csv','userdata')
        except:
                try:
                        os.remove('gen.csv')
                        os.rename('userdata','gen.csv')
                        gz=pd.read_csv("gen.csv")
                        ny=str(gz.loc[0,'0'])
                        os.rename('gen.csv','userdata')
                except:
                        pass
        
        def Close():
                cmw.destroy()


        cmw = Toplevel()
        cmw.overrideredirect(True)
        cmw.geometry("1280x720")
        def center_screen():
            global screen_height, screen_width, x_cordinate, y_cordinate
            screen_width = cmw.winfo_screenwidth()
            screen_height = cmw.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (1280/2))
            y_cordinate = int((screen_height/2) - (720/2))
            cmw.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))

        center_screen()
        cmw.geometry("1280x720")
        cmw.configure(bg = "#000000")
        canvas = Canvas(cmw,
            bg = "#000000",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file =img_resource_path("cmbg.png"))
        background = canvas.create_image(
            640.0, 355.0,
            image=background_img)

        img1 = PhotoImage(file =img_resource_path("exit.png"))
        ext= Button(cmw,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = Close,
            relief = "flat")

        ext.place(
            x = 1174, y = 627,
            width = 88,
            height = 69)
        global winner, matches
        winner = 0
        matches=0

        wether=['❄','❄','⚡','⚡','🔥','🔥','💧','💧','🌪','🌪','🌫','🌫']
        animals=['🐵','🐵','🐷','🐷','🐳','🐳','🐔','🐔','🦆','🦆','🐙','🐙']
        mood=['🙂','🙂','😑','😑','😮','😮','😎','😎','🙁','🙁','😶','😶']
        hell=['😈','😈','☠','☠','👻','👻','🎃','🎃','🏮','🏮','👹','👹']
        games=['🕹','🕹','🎱','🎱','🎲','🎲','🎮','🎮','⚽','⚽','🏈','🏈']
        asc=random.randint(1,5)
        if asc==1:
                matches=wether
        if asc==2:
                matches=animals
        if asc==3:
                matches=mood
        if asc==4:
                matches=hell
        if asc==5:
                matches=games
        random.shuffle(matches)

        def win():
                gist_list = gist_api.get_gists()
                jm=gist_list[5]['files']['dbase.csv']['raw_url']
                kl=pd.read_csv(jm)
                d=kl[kl['user']==ny].index.values
                kl.loc[d,'Offline WINs']+=1
                kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                kl.to_csv('dbase.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dbase.csv')
                os.rename('dbase.csv','cache')
                os.remove('cache')
                messagebox.showinfo(parent=cmw,title='Yeah,you won!',message="You got one point")
                Close()
        def xm(b, nb):
                global count,ansl,ansd,winner
                if b["text"] == ' ' and count < 2:
                        b["text"] = matches[nb]
                        # Add nb to answer list
                        ansl.append(nb)
                        # Add button and nb to Answer Dictionary
                        ansd[b] = matches[nb]
                        # Increment our Counter
                        count += 1
                if len(ansl) == 2:
                        if matches[ansl[0]] == matches[ansl[1]]:
                                for key in ansd:
                                        key["state"] = "disabled"
                                count = 0
                                ansl = []
                                ansd = {}
                                # Increment our winner counter
                                winner += 1
                                if winner == 6:
                                        win()
                        else:
                                count = 0
                                ansl = []
                                # pop up box
                                messagebox.showinfo(parent=cmw,title="Incorrect!",message="Incorrect")

                                # Reset the buttons
                                for key in ansd:
                                        key["text"] = " "

                                ansd = {}

        global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11 
        b0 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b0, 0), relief="groove")
        b1 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b1, 1), relief="groove")
        b2 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b2, 2), relief="groove")
        b3 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b3, 3), relief="groove")
        b4 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b4, 4), relief="groove")
        b5 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b5, 5), relief="groove")
        b6 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b6, 6), relief="groove")
        b7 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b7, 7), relief="groove")
        b8 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b8, 8), relief="groove")
        b9 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b9, 9), relief="groove")
        b10 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b10, 10), relief="groove")
        b11 = Button(cmw, text=' ', font=("Teko", 31), height=3,bg='black',disabledforeground="#0059ff",fg='#09ff00', width=6, command=lambda: xm(b11, 11), relief="groove")


        b0.place(x=350, y=101)
        b1.place(x=510, y=101)
        b2.place(x=670, y=101)
        b3.place(x=830, y=101)

        b4.place(x=350, y=290)
        b5.place(x=510, y=290)
        b6.place(x=670, y=290)
        b7.place(x=830, y=290)

        b8.place(x=350, y=479)
        b9.place(x=510, y=479)
        b10.place(x=670, y=479)
        b11.place(x=830, y=479)
        cmw.grab_set()
        cmw.resizable(False, False)
        cmw.mainloop()
