from asyncio import exceptions
import os
import random as r
import time as t
from tkinter import *
from tkinter import messagebox
import gistyc
import sys
import yt
gist_api = gistyc.GISTyc(auth_token='<auth_token_here>')
import pandas as pd
zap=0

def icno():
    yt.spyt()
    
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def tttmp():
    try:
        gz=pd.read_csv("gen.csv")
        ny=str(gz.loc[0,'0'])
        gist_list = gist_api.get_gists()
        jm=gist_list[5]['files']['dbase.csv']['raw_url']
        kl=pd.read_csv(jm)
        d=kl[kl['user']==ny].index.values
        you=int(d)+1
        os.rename('gen.csv','userdata')
    except:
        try:
            os.rename('userdata','gen.csv')
            gz=pd.read_csv("gen.csv")
            ny=str(gz.loc[0,'0'])
            gist_list = gist_api.get_gists()
            jm=gist_list[5]['files']['dbase.csv']['raw_url']
            kl=pd.read_csv(jm)
            d=kl[kl['user']==ny].index.values
            you=int(d)+1
            os.rename('gen.csv','userdata')
        except:
            pass

    def res():
        guno=pd.DataFrame(data=[[1,2,3,0,0,0,0],[4,5,6,0,0,0,0],[7,8,9,0,0,0,0]])
        gist_list = gist_api.get_gists()
        jm=gist_list[n]['files']['dev.csv']['raw_url']
        ngen=pd.read_csv(jm)
        if tuple(guno.dtypes)==tuple(ngen.dtypes):
            pass
        if tuple(guno.dtypes)!=tuple(ngen.dtypes):
            guno.to_csv('dev.csv',index=False)
            response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
            os.rename('dev.csv','cache')
            os.remove('cache')
    n=0
    try:
        while n<=5:
            gist_list = gist_api.get_gists()
            jm=gist_list[n]['files']['dev.csv']['raw_url']
            rept=pd.read_csv(jm)
            if int(rept.loc[0,'4'])==0 or int(rept.loc[0,'4'])==1 :
                print(n)
                break
            else:
                n+=1
    except:
        n=6
    def Close():
        try:
            res()
            xaim.destroy()
            
        except:
            print()
        1/0
    try:
        xaim = Toplevel()
        xaim.overrideredirect(True)
        xaim.geometry("1280x720")
        xaim.configure(bg = "#000000")
        xaim.grab_set()
        def center_screen():
            global screen_height, screen_width, x_cordinate, y_cordinate
            screen_width = xaim.winfo_screenwidth()
            screen_height = xaim.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (1280/2))
            y_cordinate = int((screen_height/2) - (720/2))
            xaim.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))
        
        center_screen()
        canvas = Canvas(
            xaim,
            bg = "#000000",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        background_img = PhotoImage(file =img_resource_path("gbg.png"))
        background = canvas.create_image(
            640.0, 361.5,
            image=background_img)
        imgi = PhotoImage(file = img_resource_path("ino.png"))
        ino = Button(xaim,
            image = imgi,
            borderwidth = 0,
            highlightthickness = 0,
            command = icno,
            relief = "flat")
        ino.place(
            x = 317, y = 654,
            width = 59,
            height = 59)
        img0 = PhotoImage(file =img_resource_path("exit.png"))
        ext = Button(xaim,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Close,
            relief = "flat")
        ext.place(
            x = 1174, y = 610,
            width = 88,
            height = 69)
        if n==6:
            messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe status",message="Server is full plz try after sometime")
            1/0

        gist_list = gist_api.get_gists()
        jm=gist_list[n]['files']['dev.csv']['raw_url']
        edg=pd.read_csv(jm)
        edg.loc[0,'5']+=1
        edg.loc[0,'4']+=1
        edg.to_csv('dev.csv',index=False)
        response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
        danc=edg.loc[0,'5']
        tt=11
        pk="null"
        pun=0
        if danc==1:
            tt=0
            messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe status",message="Wait for another player to connect !..")
            while True:
                gist_list = gist_api.get_gists()
                jm=gist_list[n]['files']['dev.csv']['raw_url']
                edg=pd.read_csv(jm)
                danc=edg.loc[0,'5']
                if pun==0:
                    edg.to_csv('dev.csv',index=False)
                    response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                    os.rename('dev.csv','cache')
                    os.remove('cache')
                    pun=9
                if danc==1:
                    pass
                if danc==2:
                    messagebox.showwarning(parent=xaim,title="Tic-Tac-Toe status",message="Be ready! another player connected..")
                    danc=2
                    break
        gen=0
        if danc==2:
            t.sleep(tt)
            gist_list = gist_api.get_gists()
            jm=gist_list[n]['files']['dev.csv']['raw_url']
            try:
                os.rename('userdata','gen.csv')
            except:
                pass
            gz=pd.read_csv("gen.csv")
            edg=pd.read_csv(jm)
            pk=edg.loc[0,'3']
            if pk==0:                
                asi=r.randint(1,100)
                if asi%2==0:
                    print('1st')
                    edg.loc[0,'3']=1
                    edg.loc[0,'4']=1
                    edg.loc[0,'5']=1
                    edg.loc[0,'6']=str(gz.loc[0,'0'])
                    edg.loc[1,'6']=gz.loc[0,'3']
                    edg.to_csv('dev.csv',index=False)
                    response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                    if edg.loc[2,'6']==0:
                        t.sleep(7)
                    try:
                        os.rename('gen.csv','userdata')
                    except:
                        pass
                    os.rename('dev.csv','cache')
                    os.remove('cache')
                    gen=1
                    messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe status",message='You have been randomly assigned "X"')

                else:
                    edg.loc[0,'3']=2
                    edg.loc[0,'4']=1
                    edg.loc[0,'5']=1
                    edg.loc[1,'4']=str(gz.loc[0,'0'])
                    edg.loc[2,'6']=gz.loc[0,'3']
                    edg.to_csv('dev.csv',index=False)
                    response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                    if edg.loc[1,'6']==0:
                        t.sleep(7)
                    try:
                        os.rename('gen.csv','userdata')
                    except:
                        pass
                    os.rename('dev.csv','cache')
                    os.remove('cache')
                    gen=2
                    messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe status",message='You have been randomly assigned "O"')
            if pk==1:
                gen=2
                edg.loc[1,'4']=str(gz.loc[0,'0'])
                edg.loc[2,'6']=you
                edg.loc[0,'4']=2
                edg.loc[0,'5']=2
                edg.to_csv('dev.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                try:
                    os.rename('gen.csv','userdata')
                except:
                    pass
                os.rename('dev.csv','cache')
                os.remove('cache')
                messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe status",message='You have been randomly assigned "O"')
            if pk==2:
                gen=1
                edg.loc[0,'6']=str(gz.loc[0,'0'])
                edg.loc[1,'6']=you
                edg.loc[0,'4']=2
                edg.loc[0,'5']=2
                edg.to_csv('dev.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                try:
                    os.rename('gen.csv','userdata')
                except:
                    pass
                os.rename('dev.csv','cache')
                os.remove('cache')
                messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe status",message='You have been randomly assigned "X"')

        fk=['1','2','3','4','5','6','7','8','9',]
        #for win check
        def cat(fk,zenc):
            print()
            gist_list = gist_api.get_gists()
            jm=gist_list[n]['files']['dev.csv']['raw_url']
            kt=pd.read_csv(jm)
            #win prompt
            if int(kt.loc[2,'4'])==1:
                if zap=="X"and zenc==0:
                    if ny!=opponent:
                        gist_list = gist_api.get_gists()
                        jm=gist_list[5]['files']['dbase.csv']['raw_url']
                        kl=pd.read_csv(jm)
                        d=kl[kl['user']==ny].index.values
                        kl.loc[d,'Online WINs']+=1
                        kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                        kl.to_csv('dbase.csv',index=False)
                        response_update_data = gist_api.update_gist(file_name='dbase.csv')
                        zenc+=1
                        os.rename('dbase.csv','cache')
                        os.remove('cache')
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='X won!')
                        Close()
                    if ny==opponent:
                        gist_list = gist_api.get_gists()
                        jm=gist_list[5]['files']['dbase.csv']['raw_url']
                        kl=pd.read_csv(jm)
                        d=kl[kl['user']==ny].index.values
                        kl.loc[d,'Online WINs']-=1
                        kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                        kl.to_csv('dbase.csv',index=False)
                        response_update_data = gist_api.update_gist(file_name='dbase.csv')
                        zenc+=1
                        os.rename('dbase.csv','cache')
                        os.remove('cache')
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Nice try kido ( ͡° ͜ʖ ͡°) dont play against urself (u got -1)!')
                        Close()
                if zap=="O":
                    if ny!=opponent:
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='X won!')
                        try:
                            xaim.destroy()
                            
                        except:
                            print()
                        pass
                    if ny==opponent:
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Nice try kido ( ͡° ͜ʖ ͡°) dont play against urself (u got -1)!')
                        try:
                            xaim.destroy()
                            
                        except:
                            print()
                        pass
                print('1 cat')

            if int(kt.loc[2,'4'])==2:
                if zap=="O"and zenc==0:
                    if ny!=opponent:
                        gist_list = gist_api.get_gists()
                        jm=gist_list[5]['files']['dbase.csv']['raw_url']
                        kl=pd.read_csv(jm)
                        d=kl[kl['user']==ny].index.values
                        kl.loc[d,'Online WINs']+=1
                        kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                        kl.to_csv('dbase.csv',index=False)
                        response_update_data = gist_api.update_gist(file_name='dbase.csv')
                        zenc+=1
                        os.rename('dbase.csv','cache')
                        os.remove('cache')
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='O won!')
                        Close()
                    if ny==opponent:
                        gist_list = gist_api.get_gists()
                        jm=gist_list[5]['files']['dbase.csv']['raw_url']
                        kl=pd.read_csv(jm)
                        d=kl[kl['user']==ny].index.values
                        kl.loc[d,'Online WINs']-=1
                        kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                        kl.to_csv('dbase.csv',index=False)
                        response_update_data = gist_api.update_gist(file_name='dbase.csv')
                        zenc+=1
                        os.rename('dbase.csv','cache')
                        os.remove('cache')
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Nice try kido ( ͡° ͜ʖ ͡°) dont play against urself (u got -1)!')
                        Close()                           
                if zap=="X":
                    if ny!=opponent:
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='O won!')
                        try:
                            xaim.destroy()
                            
                        except:
                            print()
                        pass
                    if ny==opponent:
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Nice try kido ( ͡° ͜ʖ ͡°) dont play against urself (u got -1)!')
                        try:
                            xaim.destroy()
                            
                        except:
                            print()
                        pass                           
            if int(kt.loc[2,'4'])==3:
                messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Game Tie!')
                Close()
            zeo=kt.drop('3',axis=1)
            zeo=zeo.drop('4',axis=1)
            zeo=zeo.drop('5',axis=1)
            zeo=zeo.drop('6',axis=1)
            eon=zeo.values
            r1=tuple(eon[0])
            n1=[]
            for x in r1:
                if x in fk :
                    n1.append(int(x))
                else:
                    n1.append(x)
            r1=tuple(n1)
            r2=tuple(eon[1])
            n2=[]
            for x in r2:
                if x in fk :
                    n2.append(int(x))
                else:
                    n2.append(x)
            r2=tuple(n2)
            r3=tuple(eon[2])
            n3=[]
            for x in r3:
                if x in fk :
                    n3.append(int(x))
                else:
                    n3.append(x)
            r3=tuple(n3)
            gym=(r1,r2,r3)
            gist_list = gist_api.get_gists()
            jm=gist_list[n]['files']['dev.csv']['raw_url']
            kt=pd.read_csv(jm)
            def all_same(l):
                if l.count(l[0]) == len(l) and l[0] != 0:
                    return True
                else:
                    return False

            ## horizontal
            for row in gym:
                if all_same(row) :
                    if row[0]=="X":
                        kt.loc[2,'4']=1
                    if row[0]=="O":
                        kt.loc[2,'4']=2
                    kt.to_csv('dev.csv',index=False)
                    response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                    os.rename('dev.csv','cache')
                    os.remove('cache')
                    return True

            ## vertical
            for col in range(len(gym[0])):
                check = []
                for row in gym:
                    check.append(row[col])
                if all_same(check):
                    if check[0]=="X":
                        kt.loc[2,'4']=1
                    if check[0]=="O":
                        kt.loc[2,'4']=2
                                
                    kt.to_csv('dev.csv',index=False)
                    response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                    os.rename('dev.csv','cache')
                    os.remove('cache')
                    return True

            ## / diagonal
            diags = []
            for idx, reverse_idx in enumerate(reversed(range(len(gym)))):
                diags.append(gym[idx][reverse_idx])

            if all_same(diags):
                if diags[0]=="X":
                    kt.loc[2,'4']=1
                if diags[0]=="O":
                    kt.loc[2,'4']=2
                kt.to_csv('dev.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                os.rename('dev.csv','cache')
                os.remove('cache')
            
            # \ diagonal
            diags = []
            for ix in range(len(gym)):
                diags.append(gym[ix][ix])

            if all_same(diags):
                if diags[0]=="X":
                    kt.loc[2,'4']=1
                if diags[0]=="O":
                    kt.loc[2,'4']=2
                            
                kt.to_csv('dev.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                return True
            #win prompt
            if int(kt.loc[2,'4'])==1:
                if zap=="X"and zenc==0:
                    print(opponent,ny)
                    if opponent!=ny:
                        gist_list = gist_api.get_gists()
                        jm=gist_list[5]['files']['dbase.csv']['raw_url']
                        kl=pd.read_csv(jm)
                        d=kl[kl['user']==ny].index.values
                        kl.loc[d,'Online WINs']+=1
                        kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                        kl.to_csv('dbase.csv',index=False)
                        response_update_data = gist_api.update_gist(file_name='dbase.csv')
                        zenc+=1
                        os.rename('dbase.csv','cache')
                        os.remove('cache')
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='X won!')
                        Close()
                    if opponent==ny:
                        gist_list = gist_api.get_gists()
                        jm=gist_list[5]['files']['dbase.csv']['raw_url']
                        kl=pd.read_csv(jm)
                        d=kl[kl['user']==ny].index.values
                        kl.loc[d,'Online WINs']-=1
                        kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                        kl.to_csv('dbase.csv',index=False)
                        response_update_data = gist_api.update_gist(file_name='dbase.csv')
                        zenc+=1
                        os.rename('dbase.csv','cache')
                        os.remove('cache')
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Nice try kido ( ͡° ͜ʖ ͡°) dont play against urself (u got -1)!')
                        Close()
                if zap=="O":
                    if opponent!=ny:
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='X won!')
                        try:
                            xaim.destroy()
                            
                        except:
                            print()
                        pass
                    if opponent==ny:
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Nice try kido ( ͡° ͜ʖ ͡°) dont play against urself (u got -1)!')
                        try:
                            xaim.destroy()
                            
                        except:
                            print()
                        pass
                print('2 cat')

            if int(kt.loc[2,'4'])==2:
                if zap=="O"and zenc==0:
                    if opponent!=ny:
                        gist_list = gist_api.get_gists()
                        jm=gist_list[5]['files']['dbase.csv']['raw_url']
                        kl=pd.read_csv(jm)
                        d=kl[kl['user']==ny].index.values
                        kl.loc[d,'Online WINs']+=1
                        kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                        kl.to_csv('dbase.csv',index=False)
                        response_update_data = gist_api.update_gist(file_name='dbase.csv')
                        zenc+=1
                        os.rename('dbase.csv','cache')
                        os.remove('cache')
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='O won!')
                        Close()
                    if opponent==ny:
                        gist_list = gist_api.get_gists()
                        jm=gist_list[5]['files']['dbase.csv']['raw_url']
                        kl=pd.read_csv(jm)
                        d=kl[kl['user']==ny].index.values
                        kl.loc[d,'Online WINs']-=1
                        kl.loc[d,'TOTAL WINs']=kl.loc[d,'Online WINs']+kl.loc[d,'Offline WINs']
                        kl.to_csv('dbase.csv',index=False)
                        response_update_data = gist_api.update_gist(file_name='dbase.csv')
                        zenc+=1
                        os.rename('dbase.csv','cache')
                        os.remove('cache')
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Nice try kido ( ͡° ͜ʖ ͡°) dont play against urself (u got -1)!')
                        Close()
                if zap=="X":
                    if opponent!=ny:
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='O won!')
                        try:
                            xaim.destroy()
                            
                        except:
                            print()
                        pass
                    if opponent==ny:
                        messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Nice try kido ( ͡° ͜ʖ ͡°) dont play against urself (u got -1)!')
                        try:
                            xaim.destroy()
                            
                        except:
                            print()
                        pass
            if int(kt.loc[2,'4'])==3:
                messagebox.showinfo(parent=xaim,title="Tic-Tac-Toe results",message='Game Tie!')
                Close()
            return False
        #allotment x
        def insx(zenc):
            gist_list = gist_api.get_gists()
            jm=gist_list[n]['files']['dev.csv']['raw_url']
            kt=pd.read_csv(jm)
            zo=kt.loc[1,'3'] 
            jn=kt.loc[2,'3']
            while jn<9:
                    while zo==1 and jn<9:				
                        pin=1
                        while pin==1:
                            cat(fk,zenc)
                            gist_list = gist_api.get_gists()
                            jm=gist_list[n]['files']['dev.csv']['raw_url']
                            kt=pd.read_csv(jm)    
                            zo=kt.loc[1,'3']
                            jn=kt.loc[2,'3']
                            d=kt.loc[2,'5']
                            cat(fk,zenc)
                            if zo==1:pass
                            if zo==0:
                                    pin=0
                                    if d==1:
                                            b1["text"] = "O"
                                            b1["fg"]="#260857"
                                            b1["disabledforeground"]="#260857"
                                            b1['state'] = DISABLED
                                    if d==2:
                                            b2["text"] = "O"
                                            b2["fg"]="#260857"
                                            b2["disabledforeground"]="#260857"
                                            b2['state'] = DISABLED
                                    if d==3:
                                            b3["text"] = "O"
                                            b3["fg"]="#260857"
                                            b3["disabledforeground"]="#260857"
                                            b3['state'] = DISABLED
                                    if d==4:
                                            b4["text"] = "O"
                                            b4["fg"]="#260857"
                                            b4["disabledforeground"]="#260857"
                                            b4['state'] = DISABLED
                                    if d==5:
                                            b5["text"] = "O"
                                            b5["fg"]="#260857"
                                            b5["disabledforeground"]="#260857"
                                            b5['state'] = DISABLED
                                    if d==6:
                                            b6["text"] = "O"
                                            b6["fg"]="#260857"
                                            b6["disabledforeground"]="#260857"
                                            b6['state'] = DISABLED
                                    if d==7:
                                            b7["text"] = "O"
                                            b7["fg"]="#260857"
                                            b7["disabledforeground"]="#260857"
                                            b7['state'] = DISABLED
                                    if d==8:
                                            b8["text"] = "O"
                                            b8["fg"]="#260857"
                                            b8["disabledforeground"]="#260857"
                                            b8['state'] = DISABLED
                                    if d==9:
                                            b9["text"] = "O"
                                            b9["fg"]="#260857"
                                            b9["disabledforeground"]="#260857"
                                            b9['state'] = DISABLED
                                    break
                    if zo==0:
                        cat(fk,zenc)
                        break
        #allotment o
        def inso(zenc):
            gist_list = gist_api.get_gists()
            jm=gist_list[n]['files']['dev.csv']['raw_url']
            kt=pd.read_csv(jm)
            zo=kt.loc[1,'3'] 
            jn=kt.loc[2,'3']
            ifg=2
            while jn<9:
                while zo==0 and jn<9 and ifg==2:
                        pin=1
                        while pin==1:
                            gist_list = gist_api.get_gists()
                            jm=gist_list[n]['files']['dev.csv']['raw_url']
                            kt=pd.read_csv(jm)    
                            zo=kt.loc[1,'3']
                            jn=kt.loc[2,'3']
                            d=kt.loc[1,'5']
                            cat(fk,zenc)
                            if zo==0:
                                pass                       
                            if zo==1:
                                cat(fk,zenc)						
                                if d==1:
                                        b1["text"] = "X"
                                        b1["fg"]="#5C2670"
                                        b1["disabledforeground"]="#5C2670"
                                        b1['state'] = DISABLED
                                if d==2:
                                        b2["text"] = "X"
                                        b2["fg"]="#5C2670"
                                        b2["disabledforeground"]="#5C2670"
                                        b2['state'] = DISABLED
                                if d==3:
                                        b3["text"] = "X"
                                        b3["fg"]="#5C2670"
                                        b3["disabledforeground"]="#5C2670"
                                        b3['state'] = DISABLED
                                if d==4:
                                        b4["text"] = "X"
                                        b4["fg"]="#5C2670"
                                        b4["disabledforeground"]="#5C2670"
                                        b4['state'] = DISABLED
                                if d==5:
                                        b5["text"] = "X"
                                        b5["fg"]="#5C2670"
                                        b5["disabledforeground"]="#5C2670"
                                        b5['state'] = DISABLED
                                if d==6:
                                        b6["text"] = "X"
                                        b6["fg"]="#5C2670"
                                        b6["disabledforeground"]="#5C2670"
                                        b6['state'] = DISABLED
                                if d==7:
                                        b7["text"] = "X"
                                        b7["fg"]="#5C2670"
                                        b7["disabledforeground"]="#5C2670"
                                        b7['state'] = DISABLED
                                if d==8:
                                        b8["text"] = "X"
                                        b8["fg"]="#5C2670"
                                        b8["disabledforeground"]="#5C2670"
                                        b8['state'] = DISABLED
                                if d==9:
                                        b9["text"] = "X"
                                        b9["fg"]="#5C2670"
                                        b9["disabledforeground"]="#5C2670"
                                        b9['state'] = DISABLED
                                pin=0										
                                break
                if zo==1:
                        cat(fk,zenc)
                        break
        def erm():
            return messagebox.showerror(parent=xaim,title="Tic Tac Toe",message="Hey! That box has already been selected\nPick Another Box..." )



        def forex(zenc):
            def xm(a,vp):
                insx(zenc)
                gist_list = gist_api.get_gists()
                jm=gist_list[n]['files']['dev.csv']['raw_url']
                edg=pd.read_csv(jm)
                jn=edg.loc[2,'3']
                try:
                    if vp=='b1':
                        if int(edg.loc[0,'0'])==1:
                            edg.loc[0,'0']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=1

                    if vp=='b2':
                        if int(edg.loc[0,'1'])==2:
                            edg.loc[0,'1']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=2
                    if vp=='b3':
                        if int(edg.loc[0,'2'])==3:
                            edg.loc[0,'2']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=3
                    if vp=='b4':
                        if int(edg.loc[1,'0'])==4:
                            edg.loc[1,'0']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=4
                    if vp=='b5':
                        if int(edg.loc[1,'1'])==5:
                            edg.loc[1,'1']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=5
                    if vp=='b6':
                        if int(edg.loc[1,'2'])==6:
                            edg.loc[1,'2']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=6

                    if vp=='b7':
                        if int(edg.loc[2,'0'])==7:
                            edg.loc[2,'0']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=7
                    if vp=='b8':
                        if int(edg.loc[2,'1'])==8:
                            edg.loc[2,'1']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=8
                    if vp=='b9':
                        if int(edg.loc[2,'2'])==9:
                            edg.loc[2,'2']='X'
                            a["text"] = "X"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=1
                            edg.loc[1,'5']=9
                except:
                    erm()
                edg.to_csv('dev.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                os.rename('dev.csv','cache')
                os.remove('cache')
                insx(zenc)
            
            global b1,b2,b3,b4,b5,b6,b7,b8,b9
            b1 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b1,'b1'))
            b2 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b2,'b2'))
            b3 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b3,'b3'))

            b4 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b4,'b4'))
            b5 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b5,'b5'))
            b6 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b6,'b6'))

            b7 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b7,'b7'))
            b8 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b8,'b8'))
            b9 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#5C2670", command=lambda: xm(b9,'b9'))

            # Grid our buttons to the screen
            b1.place(x=170,y=184)
            b2.place(x=294,y=184)
            b3.place(x=418,y=184)

            b4.place(x=170,y=327)
            b5.place(x=294,y=327)
            b6.place(x=418,y=327)

            b7.place(x=170,y=470)
            b8.place(x=294,y=470)
            b9.place(x=418,y=470)
            entry0 = Button(xaim, text="X", font=("Teko", 25), height=3, width=6, bg="Black",fg="white")

            entry0.place(
                x = 1116, y = 265,
                width = 70,
                height = 50)

            entry1 =Button(xaim, text=you, font=("Teko", 25), height=3, width=6, bg="Black",fg="white")

            entry1.place(
                x = 1096, y = 342,
                width = 108,
                height = 50)
            if opponent==0:
                messagebox.showwarning(parent=xaim,title="status",message="Someting Ain't gone right,plz restart the game or contact us")
                Close()
            entry2 =Button(xaim, text=opponent, font=("Teko", 25), height=3, width=6, bg="Black",fg="white")

            entry2.place(
                x = 1068, y = 412,
                width = 164,
                height = 50)

            entry3 =Button(xaim, text=rank, font=("Teko", 25), height=3, width=6, bg="Black",fg="white")

            entry3.place(
                x = 1096, y = 489,
                width = 108,
                height = 50)


        def foreo(zenc):
            def xm(a,vp):
                inso(zenc)
                gist_list = gist_api.get_gists()
                jm=gist_list[n]['files']['dev.csv']['raw_url']
                edg=pd.read_csv(jm)
                try:
                    if vp=='b1':
                        if int(edg.loc[0,'0'])==1:
                            edg.loc[0,'0']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=1


                    if vp=='b2':
                        if int(edg.loc[0,'1'])==2:
                            edg.loc[0,'1']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=2

                    if vp=='b3':
                        if int(edg.loc[0,'2'])==3:
                            edg.loc[0,'2']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=3

                    if vp=='b4':
                        if int(edg.loc[1,'0'])==4:
                            edg.loc[1,'0']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=4

                    if vp=='b5':
                        if int(edg.loc[1,'1'])==5:
                            edg.loc[1,'1']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=5

                    if vp=='b6':
                        if int(edg.loc[1,'2'])==6:
                            edg.loc[1,'2']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=6

                    if vp=='b7':
                        if int(edg.loc[2,'0'])==7:
                            edg.loc[2,'0']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=7
                    if vp=='b8':
                        if int(edg.loc[2,'1'])==8:
                            edg.loc[2,'1']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=8

                    if vp=='b9':
                        if int(edg.loc[2,'2'])==9:
                            edg.loc[2,'2']='O'
                            a["text"] = "O"
                            a['state'] = DISABLED
                            edg.loc[2,'3']+=1
                            edg.loc[1,'3']=0
                            edg.loc[2,'5']=9
                except:
                    erm()
                edg.to_csv('dev.csv',index=False)
                response_update_data = gist_api.update_gist(file_name='dev.csv',gist_id=gist_list[n]['id'])
                os.rename('dev.csv','cache')
                os.remove('cache')
                inso(zenc)
            
            global b1,b2,b3,b4,b5,b6,b7,b8,b9
            b1 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b1,'b1'))
            b2 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b2,'b2'))
            b3 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b3,'b3'))

            b4 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b4,'b4'))
            b5 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b5,'b5'))
            b6 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b6,'b6'))

            b7 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b7,'b7'))
            b8 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b8,'b8'))
            b9 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="black",activebackground="#c25106",disabledforeground="#260857", command=lambda: xm(b9,'b9'))
            # Grid our buttons to the screen
            b1.place(x=170,y=184)
            b2.place(x=294,y=184)
            b3.place(x=418,y=184)

            b4.place(x=170,y=327)
            b5.place(x=294,y=327)
            b6.place(x=418,y=327)

            b7.place(x=170,y=470)
            b8.place(x=294,y=470)
            b9.place(x=418,y=470)

            entry0 = Button(xaim, text="O", font=("Teko", 25), height=3, width=6, bg="Black",fg="white")

            entry0.place(
                x = 1116, y = 265,
                width = 70,
                height = 50)

            entry1 =Button(xaim, text=you, font=("Teko", 25), height=3, width=6, bg="Black",fg="white")

            entry1.place(
                x = 1096, y = 342,
                width = 108,
                height = 50)
            if opponent==0:
                messagebox.showwarning(parent=xaim,title="status",message="Someting Ain't gone right,plz restart the game or contact us")
                Close()
            entry2 =Button(xaim, text=opponent, font=("Teko", 25), height=3, width=6, bg="Black",fg="white")

            entry2.place(
                x = 1068, y = 412,
                width = 164,
                height = 50)

            entry3 =Button(xaim, text=rank, font=("Teko", 25), height=3, width=6, bg="Black",fg="white")

            entry3.place(
                x = 1096, y = 489,
                width = 108,
                height = 50)

            inso(zenc)
        
        #final alotation
        global zenc
        zenc=0
        if gen==1:
            t.sleep(4)
        else:
            t.sleep(2.3)
        gist_list = gist_api.get_gists()
        jm=gist_list[n]['files']['dev.csv']['raw_url']
        dog=pd.read_csv(jm)
        global rank,opponent
        if gen==1:
            zap="X"
            opponent=dog.loc[1,'4']
            rank=dog.loc[2,'6']
            print(dog.loc[1,'4'])
            print(opponent)
            forex(zenc)
        if gen==2:
            zap="O"
            opponent=dog.loc[0,'6']
            rank=dog.loc[1,'6']
            print(dog.loc[0,'6'])
            print(opponent)
            foreo(zenc)

        xaim.grab_set()
        xaim.resizable(False, False)
        xaim.mainloop()
    except:
        res()
        Close()
