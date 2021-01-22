# %%

from functools import partial
import tkinter as tk
import tkinter.font as TkFont
import tkinter.messagebox
import random
from tkinter import *

interface = Tk()
interface.title("Play The Game")
interface.geometry("1050x750")
changingnum = 1
PLUS = 1
MINUS = 0
start = 11
oway = 1
button_identities = []
attempts = 0
helpme = 0
radiobutt = IntVar()
radiobutt.set(1)


def forget(widget):
    """
    This will remove the widget from toplevel
    widget will become invisible and loses its position
    """
    
    widget.grid_forget()


def change(n):
    """
    function to get the index and the identity (bname)
    """
    global changingnum
    global attempts
    global listpre
    global listfin
    
    bname = (button_identities[n])
    
    bname["text"] = str(changingnum)
    attempts += 1
    labellevel["text"] = "No Attemps " + str(attempts)

    listpre[n] = changingnum
    print(listpre[n])
    if listpre == listfin:
        tkinter.messagebox.showinfo("You Won the Game!")
    else:
        attempts += 1
    bname["fg"] = '#11670a'

    
def retrieve(widget, wid):
    global oway
    if wid == '1':
        widget.grid(row=oway, column=0)
        oway += 1
    elif wid == 'buttonlevel':
        widget.grid(row=4, column=15)
    elif wid == 'labellevel':
        widget.grid(row=2, column=14)
    elif wid == 'buttonlevelnew':
        widget.grid(row=5, column=15)
    elif wid == 'label':
        widget['text'] = "Select a value to  Change"
        widget.grid(row=0, column=0)
    if oway > 5:
        oway = 1

    
def changnum():
    global changingnum
    changingnum = radiobutt.get()

    
def changlevel(m):
    """
    for changing the level
    """
    global listfin
    global listpre
    global button_identities
    global attempts
    global helpme
    if m == 0:
        if helpme == 0:
            tkinter.messagebox.showinfo("Game Rule", "Every help will increase your attempts by 50")
        if helpme > 0:
            attempts += 50
            labellevel["text"] = "No Attemps " + str(attempts)
        else:
            labellevel["text"] = "No Attemps " + str(attempts)
            helpme += 1
        rand13 = list(range(0, 80))
        indexes = random.sample(rand13, k=13)
        for i in indexes:
            listpre[i] = listfin[i]
        for i in range(len(listpre)):
            e = listpre[i]
            but = button_identities[i]
            if e > 0:
                but['text'] = listpre[i]
            elif e == 0:
                but['text'] = ""
    if m == 11:
        attempts = 0
        labellevel["text"] = "No Attemps " + str(attempts)
        retrieve(Rd1, "1")
        retrieve(Rd2, '1')
        retrieve(Rd3, '1')
        retrieve(Rd4, '1')
        retrieve(Rd5, '1')
        retrieve(labellevel, 'labellevel')
        retrieve(label, 'label')
        retrieve(buttonlevelnew, 'buttonlevelnew')
     
        for i in range(len(listpre)):  
            but = button_identities[i]
            listpre[i] = 0
            but['text'] = ""
        attempts = 0
        rand13 = list(range(0, 80))
        indexes = random.sample(rand13, k=13)
        for i in indexes:
            listpre[i] = listfin[i]
        for i in range(len(listpre)):
            e = listpre[i]
            but = button_identities[i]
            if e > 0:
                but['text'] = listpre[i]
            elif e == 0:
                but['text'] = ""

    if m == 1:
      
        for i in range(81):
            a = button_identities[i]
            b = listfin[i]
            a['text'] = b
      
    
def exitb():
    """
    exit code button
    """
    interface.destroy()


labellevel = Label(interface, width=16, height=1, text="No Attemps ")
labellevel.grid(row=2, column=14)
buttonlevelpre = Button(interface, width=12, height=2, text=' New Game ', command=partial(changlevel, start))
buttonlevel = Button(interface, width=12, height=2, text=' check the result ', command=partial(changlevel, PLUS))
buttonlevelnew = Button(interface, width=12, height=2, text=' Help me', command=partial(changlevel, MINUS))
buttonlevelexit = Button(interface, width=12, height=2, text=' Exit ', command=exitb)
buttonlevelpre.grid(row=3, column=15)
buttonlevel.grid(row=4, column=15)
buttonlevelnew.grid(row=5, column=15)
buttonlevelexit.grid(row=6, column=15)

label = Label(interface, text="Press Start button", font=("Time New Roman", 10, ['bold']))
label.grid(row=0, column=0)
Rd1 = Radiobutton(interface, text='1', font=(['Bold']), variable=radiobutt, value=1, command=changnum)
Rd2 = Radiobutton(interface, text='2', font=(['Bold']), variable=radiobutt, value=2, command=changnum)
Rd3 = Radiobutton(interface, text='3', font=(['Bold']), variable=radiobutt, value=3, command=changnum)
Rd4 = Radiobutton(interface, text='4', font=(['Bold']), variable=radiobutt, value=4, command=changnum)
Rd5 = Radiobutton(interface, text='5', font=(['Bold']), variable=radiobutt, value=5, command=changnum)

Rd1.grid(row=1, column=0)
Rd2.grid(row=2, column=0)
Rd3.grid(row=3, column=0)
Rd4.grid(row=4, column=0)
Rd5.grid(row=5, column=0)

butt = ""
columnn = 2
roww = 3

list1 = [0, 1, 9, 10]
list2 = [2, 3, 11, 12, 13]
list3 = [4, 5, 6, 7, 8]
list4 = [16, 17, 25, 26]
list5 = [14, 15, 22, 23]
list6 = [18, 19, 20, 21]
list7 = [24, 33, 34]
list8 = [35, 43, 44, 52, 53]
list9 = [27, 36, 45, 46];
list10 = [28, 29, 30, 37, 38]
list11 = [31, 32, 39, 40, 41]
list12 = [42, 49, 50, 51, 58]
list13 = [47, 48, 56, 57]
list14 = [54, 55, 63, 72]
list15 = [64, 65, 66, 73, 74]
list16 = [75, 76]
list17 = [77, 78, 79, 80]
list18 = [61, 62, 70, 71]
list19 = [59, 60, 67, 68, 69]
listpre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, ]

listfin = [3, 1, 2, 4, 2, 1, 5, 4, 3, 2, 4, 3, 1, 5, 4, 3, 1, 2, 3, 1, 2, 4, 2, 1, 2, 4, 3, 2, 4, 3, 1, 3, 5, 3, 1, 2, 1,
          5, 2, 4, 2, 1, 2, 4, 3, 4, 3, 1, 3, 5, 4, 3, 5, 1, 1, 2, 4, 2, 1, 2, 1, 4, 3, 4, 5, 1, 3, 4, 5, 3, 2, 1, 3, 2,
          4, 2, 1, 2, 1, 4, 3]

for i in range(81):
    columnn += 1
    butt = "button" + str(i + 1)
    butt = Button(interface, height=3, width=6, text=i + 1, font=("Helvetica", 12, ['bold']),
                  command=partial(change, i))
    butt.grid(row=roww, column=columnn)
    button_identities.append(butt)
    if i in list1:
        butt['bg'] = '#FFFF10'
    elif i in list2:
        butt['bg'] = '#FF1010'
    elif i in list3:
        butt['bg'] = '#FF7070'
    elif i in list4:
        butt['bg'] = '#0F21F9'
    elif i in list5:
        butt['bg'] = '#F010FF'
    elif i in list6:
        butt['bg'] = '#9ac930'
    elif i in list7:
        butt['bg'] = '#b5ff10'
    elif i in list8:
        butt['bg'] = '#0FF1FF'
    elif i in list9:
        butt['bg'] = '#30c997'
    elif i in list10:
        butt['bg'] = '#ffad10'
    elif i in list11:
        butt['bg'] = '#ff10b9'
    elif i in list12:
        butt['bg'] = '#7a8d85'
    elif i in list13:
        butt['bg'] = '#ff6410'
    elif i in list14:
        butt['bg'] = '#86cbe5'
    elif i in list15:
        butt['bg'] =  '#dfbd8a'
    elif i in list16:
        butt['bg'] = '#b510ff'
    elif i in list17:
        butt['bg'] ='#3cff10'
    elif i in list18:
        butt['bg'] = '#e198da'
    elif i in list19:
        butt['bg'] = '#beb3bf'
    if (columnn == 11):
        columnn = 2
        roww += 1
        
# remove all the unnecessory wigdets from the

forget(Rd1)
forget(Rd2)
forget(Rd3)
forget(Rd4)
forget(Rd5)
forget(labellevel)
forget(buttonlevelnew)
forget(buttonlevel)

# this widget will automatically retrive but calling changelevel(11) function underneath

radiobutt.set(1)
interface.configure(background='AntiqueWhite1')
changlevel(11)
forget(buttonlevel) 
interface.mainloop()

# %%
