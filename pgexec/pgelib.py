#!/usr/bin/env python3
#encoding=utf-8

#██╗  ██╗███████╗██╗  ██╗██████╗ ██╗   ██╗     ██████╗  ██████╗ ███████╗██╗  ██╗███████╗ ██████╗
#██║  ██║██╔════╝╚██╗██╔╝██╔══██╗╚██╗ ██╔╝     ██╔══██╗██╔════╝ ██╔════╝╚██╗██╔╝██╔════╝██╔════╝
#███████║█████╗   ╚███╔╝ ██████╔╝ ╚████╔╝█████╗██████╔╝██║  ███╗█████╗   ╚███╔╝ █████╗  ██║
#██╔══██║██╔══╝   ██╔██╗ ██╔═══╝   ╚██╔╝ ╚════╝██╔═══╝ ██║   ██║██╔══╝   ██╔██╗ ██╔══╝  ██║
#██║  ██║███████╗██╔╝ ██╗██║        ██║        ██║     ╚██████╔╝███████╗██╔╝ ██╗███████╗╚██████╗
#╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝        ╚═╝        ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝
#Beta version
#args: path, v, c
###############################################################################

import sys
import os
import time
import platform
import webbrowser
import subprocess
import string

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear()

if sys.version_info < (3,0):
    print('This script must be run with Python 3. Detected version:\n')
    print(sys.version_info)
    quit()

try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    print('Missing tkinter, downloading...')
    os.system('sudo apt-get install python3-tk')



################################################################################


#####################################
def trun():
    global tfile
    tfile = tfilen.get()
    tp.quit()
    tf=open(tfile)
    global texec
    texec = tf.read()
tp = Tk()
tp.minsize(width=100,height=70)
tp.wm_title('Open file')
tmsg = Message(tp,text='Enter file:')
tmsg.pack()

tfilen = Entry(tp)
tfilen.pack()

tbtn = Button(tp,text='Enter',command=trun)
tbtn.pack()

tp.mainloop()
#####################################


#Function Declarations. Beware, pretty long
################################################################################
exec(texec)
#Draw pixels, define placement and counter vars.
#Also output stats and launch tk
start = time.time()#start timer for debugging performance
master = Tk()

c = Canvas(master, width=w, height=len(pix) / w)
c.pack()

#define draw placement variables, set up hex array to be accessed
x=0
y=0
steps = 0
clr=pix[0]
ipix=iter(pix)
line = 0
pl = len(pix)
dpl = pl / w

#fuction to draw a single line, receives y pos from while loop on line 98
def drawline(x,y,steps,clr,pix,ipix,w):
    while steps < w:#check if the line is done drawing
        try:
            c.create_line(x, y, x, y, fill=clr, width=1)
            x=x+1
            steps=steps+1#used to keep track of when to end the line
            clr=next(ipix)
        except StopIteration:#if the image is nonsquare, the iterator runs out of values and errors
            clear()
            print("PGexec Error 21;invalid image file: \nNumber of values can't be evenly divided by width")
            try:
                if args[1]=="v":
                    raise
            except IndexError:
                quit()
            quit()

#move the line being drawn 1 pixel down, after the previous line is complete
while line < dpl:
    drawline(x,y,steps,clr,pix,ipix,w)#draw line with the new vars

    #refresh vars for next line and clear terminal
    line = line + 1
    y=y+1#this is the var that actually moves the line. all others are display and stuff
    steps=0
    #if len(args) > 0:
    #    vout()


#when finished drawing, show some stats while tk loads
clear()
print("Finished! Wait for tk to load.")
print('Dimensions:',w,'x',line)
print("Total # of pixels drawn:",w*line)
#print("Image size:",os.path.getsize(tfile),"bytes")
end = time.time()
time = end - start
print('Time:',time,'seconds')

url = 'http://tacolizard.github.io/HexPy/'

#cmdv='python3 pgexec '+args[0]+' v'
#cmd='python3 pgexec '+args[0]

#welcome to the land of shoddy tkinter code
#it really sucks, but I hate using classes
def OpenUrl(url):
    webbrowser.open_new(url)
def verb():
    os.system(cmdv)
def nverb():
    os.system(cmd)
def close():
    c.delete('all')
def opn():

    def runf():
        openf='python3 pgexec '+filen.get()
        os.system(openf)

    top = Toplevel()
    top.minsize(width=100,height=70)
    top.wm_title('Open file')
    msg = Message(top,text='Enter file:')
    msg.pack()

    filen = Entry(top)
    filen.pack()

    btn = Button(top,text='Enter',command=runf)
    btn.pack()





menubar = Menu(master)
submenu = Menu(menubar)
filemenu = Menu(master)
reopnmenu = Menu(filemenu)
reopnmenu.add_command(label='Verbosity', command=verb)
reopnmenu.add_command(label='Non-Verbosity', command=nverb)
submenu.add_command(label='Visit Website', command=lambda aurl=url:OpenUrl(aurl))
filemenu.add_cascade(label='Reopen With...', menu=reopnmenu)
filemenu.add_command(label='Open',command=opn)

submenu.add_command(label='Exit',command=master.quit)
filemenu.add_command(label='Close File',command=close)
menubar.add_cascade(label='pgexec', menu=submenu)
menubar.add_cascade(label='File',menu=filemenu)

master.minsize(width=200,height=150)
master.resizable(width=FALSE,height=FALSE)
master.wm_title(tfile)
master.config(menu=menubar)


master.mainloop()
