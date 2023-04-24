from tkinter import *
import os
from tkinter import *
from tkinter import messagebox
import gistyc
import sys
# X starts so true
clicked = True
count = 0
def ofaim():
	def Close():
			ofwin.destroy()
	def img_resource_path(relative_path):
		""" Get absolute path to resource, works for dev and for PyInstaller """
		try:
			# PyInstaller creates a temp folder and stores path in _MEIPASS
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")

		return os.path.join(base_path, relative_path)
	gist_api = gistyc.GISTyc(auth_token='<auth_token_here>')
	ofwin = Toplevel()
	ofwin.overrideredirect(True)
	ofwin.geometry("1280x720")
	def center_screen():
		global screen_height, screen_width, x_cordinate, y_cordinate
		screen_width = ofwin.winfo_screenwidth()
		screen_height = ofwin.winfo_screenheight()
		x_cordinate = int((screen_width/2) - (1280/2))
		y_cordinate = int((screen_height/2) - (720/2))
		ofwin.geometry("{}x{}+{}+{}".format(1280,720, x_cordinate, y_cordinate))

	center_screen()
	ofwin.configure(bg = "#000000")
	canvas = Canvas(
		ofwin,
		bg = "#000000",
		height = 720,
		width = 1280,
		bd = 0,
		highlightthickness = 0,
		relief = "ridge")
	canvas.place(x = 0, y = 0)

	background_img = PhotoImage(file =img_resource_path("ofbg.png"))
	background = canvas.create_image(
		640.0, 361.5,
		image=background_img)
	img1 = PhotoImage(file =img_resource_path("exit.png"))
	ext = Button(ofwin,
		image = img1,
		borderwidth = 0,
		highlightthickness = 0,
		command = Close,
		relief = "flat")

	ext.place(
		x = 1174, y = 627,
		width = 88,
		height = 69)
	def ccn(fgc,b):
		if b["text"] == "X":
			b.config(fg='#260857')
		if b["text"] == "O":
			b.config(fg='#5C2670')
	# Check to see if someone won
	def checkifwon():
		global winner
		winner = False
		if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" X Won!!")
			Close()
		elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" X Won!!")
			Close()

		elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" X Won!!")
			Close()

		elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" X Won!!")
			Close()

		elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" X Won!!")
			Close()

		elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" X Won!!")
			Close()

		elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" X Won!!")
			Close()

		elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" X Won!!")
			Close()

		#### CHECK FOR O's Win
		elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" O Won!!")
			Close()
		elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" O Won!!")
			Close()

		elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" O Won!!")
			Close()

		elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" O Won!!")
			Close()

		elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" O Won!!")
			Close()

		elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" O Won!!")
			Close()

		elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" O Won!!")
			Close()

		elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
			winner = True
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message=" O Won!!")
			Close()

		# Check if tie
		if count == 9 and winner == False:
			messagebox.showinfo(parent=ofwin,title="Tic Tac Toe", message="It's A Tie!\n No One Won!")
			Close()
					
	# Button clicked function
	def xm(b):
		global clicked, count,fgc

		if b["text"] == " " and clicked == True:
			b["text"] = "X"
			ccn("#260857",b)
			clicked = False
			count += 1
			checkifwon()
		elif b["text"] == " " and clicked == False:
			b["text"] = "O"
			ccn("#5C2670",b)
			clicked = True
			count += 1
			checkifwon()
		else:
			messagebox.showerror(parent=ofwin,title="Tic Tac Toe", message="Hey! That box has already been selected\nPick Another Box..." )

	# Start the game over!
	def pmt():
		
		global b1, b2, b3, b4, b5, b6, b7, b8, b9
		global clicked, count,fgc
		clicked = True
		count = 0
		fgc="#5C2670"
		
		# Build our buttons
		b1 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b1))
		b2 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b2))
		b3 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b3))

		b4 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b4))
		b5 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b5))
		b6 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b6))

		b7 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b7))
		b8 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b8))
		b9 = Button(ofwin, text=" ", font=("Teko", 25), height=3, width=6, bg="Black",fg=fgc, command=lambda: xm(b9))


		b1.place(x=472,y=172)
		b2.place(x=596,y=172)
		b3.place(x=720,y=172)

		b4.place(x=472,y=315)
		b5.place(x=596,y=315)
		b6.place(x=720,y=315)

		b7.place(x=472,y=458)
		b8.place(x=596,y=458)
		b9.place(x=720,y=458)
	pmt()
	ofwin.grab_set()
	ofwin.resizable(False, False)
	ofwin.mainloop()
