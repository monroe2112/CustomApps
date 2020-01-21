from tkinter import *
#import tkinter as tkk

master = Tk()

TheString = StringVar(master)
choices = { 'AT&T', 'Sprint', 'T-Mobile', 'Verizon'}
TheString.set('AT&T')
popupMenu = OptionMenu(master, TheString, *choices)
Label(master, text="Carrier").grid(row=3, column=2)
popupMenu.grid(row=3, column=3)
def change_dropdown(*args):
	    print( TheString.get() )

#def TheWork():
 #   f = Fname.get()
 #   L = Lname.get()
 #   T = TheTitle.get()
 #   l = TheLoco.get()
 #   e = TheEmail.get()
 #   p = ThePhone.get()
 #   C = ","
 #   c = TheString.trace('w', change_dropdown)
 #   print(f, C, L, C, T, C, l, C, e, C, p, C, c)
 #TheString.trace('w', change_dropdown)

TheString.trace('w', change_dropdown)

#Button(master, text = "Submit", command = TheWork).grid(row=4, column = 3)
Tk.mainloop