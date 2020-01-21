from tkinter import *
#import tkinter as tkk

from pathlib import Path

#if Path('a.out').is_file():
 #   print ("File exists")
#else:
 #   TS = "First Name, Last Name, Title, Location, Email, Phone Number, Carrier \n"
  #  print ("File not exists")
   # TheFile = open('a.out', 'w+')
 #   print(TS)
 #  TheFile.write(TS)
 #  TheFile.close

master = Tk()


Label(master, text='First Name').grid(row=0)
Fname = Entry(master)
Fname.grid(row=0, column=1)
Label(master, text='Last Name').grid(row=0, column=2)
Lname = Entry(master)
Lname.grid(row=0, column=3)
Label(master, text='Title').grid(row=1)
TheTitle = Entry(master)
TheTitle.grid(row=1, column=1)
Label(master, text='Location').grid(row=1, column=2)
TheLoco = Entry(master)
TheLoco.grid(row=1, column=3)
Label(master, text='Email').grid(row=2)
TheEmail = Entry(master)
TheEmail.grid(row=2, column=1)
Label(master, text='Phone').grid(row=3)
ThePhone = Entry(master)
ThePhone.grid(row=3, column=1)
TheString = StringVar(master)
choices = { 'Select Carrier', 'AT&T', 'Sprint', 'T-Mobile', 'Verizon'}
TheString.set('Select Carrier')
popupMenu = OptionMenu(master, TheString, *choices)
Label(master, text="Carrier").grid(row=3, column=2)
popupMenu.grid(row=3, column=3)
Fname.focus_set()
def change_dropdown(*args):
	    print( TheString.get() )
TheString.trace('w', change_dropdown)
S1 = TheString.get()
print(S1)
def TheWork():
    f = Fname.get()
    L = Lname.get()
    T = TheTitle.get()
    l = TheLoco.get()
    e = TheEmail.get()
    p = ThePhone.get()
    C = ","
    c = TheString.get()
    BS = "%s %s %s %s %s %s %s %s %s %s %s %s %s \n" % (f,C, L, C, T, C, l, C, e, C, p, C, c)
    print(BS)
    saveFile = open('a.out', "a+")
    saveFile.write(BS)
    saveFile.close

def ClearThings():
    Fname.delete(0, END)
    Lname.delete(0, END)
    TheTitle.delete(0, END)
    TheLoco.delete(0, END)
    TheEmail.delete(0, END)
    ThePhone.delete(0, END)
    TheString.set('Select Carrier')
    Fname.focus_set()

Button(master, text = "Submit", command = TheWork).grid(row=4, column = 3)
Button(master, text = "Clear" , command = ClearThings).grid(row=4, column=4)
Tk.mainloop