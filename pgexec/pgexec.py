#!/usr/bin/env python3

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

try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    print('Missing tkinter, downloading...')
    os.system('sudo apt-get install python3-tk')

start = time.time()#start timer for debugging performance
#####################################
sys.argv
#cleanup sys args from command line
args = sys.argv
args.remove(args[0])#remove script path from sys args
print('Loading...')
#####################################


#Function Declarations. Beware, pretty long
################################################################################
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#attempt to open file/deal with cmds.
try:
    file = open(args[0])
except FileNotFoundError:
    clear()
    print('PGexec Error 10;file not found: \nNo such file or directory','["',args[0],'"]')
    try:
        if args[1]=="v":
            raise
    except IndexError:
        quit()
    quit()
except IndexError:
    clear()
    print("PGexec Error 30;no command given: \nYou must use a command. \nSyntax, type without quotes: \npgexec 'relative directory of .pgf file' 'v'(optional error verbosity)")
    quit()
#attempt to read files
try:
    f = file.read()
    exec(f) #what actually 'reads the vars'
except UnicodeDecodeError:
    clear()
    print("PGexec Error 20;invalid image file: \nimage is not decodeable by UTF-8\nplease use images in .pgf format only")
    try:
        if args[1]=="v":
            raise
    except IndexError:
        quit()
    quit()
except SyntaxError:
    clear()
    print("PGexec Error 22;invalid image file: \ninvalid Python syntax\nplease use images in .pgf format only")
    try:
        if args[1]=="v":
            raise
    except IndexError:
        quit()
    quit()

def vout():#live draw count and stats for 'v'
    try:
        if args[1]=='v':
            clear()

            #give progress and size info
            print("Drawing from array...")
            print("Progress:",line,"/",dpl)
            print("Image size:",os.path.getsize(args[0]),"bytes")
    except IndexError:
        pass

################################################################################

#Draw pixels, define placement and counter vars.
#Also output stats and launch tk

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
            c.create_line(x, y, x+1, y, fill=clr, width=1)
            x=x+1
            steps=steps+1#used to keep track of when to end the line
            clr=next(ipix)
        except StopIteration:#if the image is nonsquare, the iterator runs out of values and errors
            clear()
            print("PGexec Error 21;invalid image file: \ndimesions given would describe an image with pixel height less than 1")
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
    if len(args) > 0:
        vout()


#when finished drawing, show some stats while tk loads
clear()
print("Finished! Wait for tk to load.")
print('Dimensions:',w,'x',line)
print("Total # of pixels drawn:",w*line)
print("Image size:",os.path.getsize(args[0]),"bytes")
end = time.time()
time = end - start
print('Time:',time,'seconds')

url = 'http://tacolizard.github.io/HexPy/'

cmdv='python3 pgexec '+args[0]+' v'
cmd='python3 pgexec '+args[0]

def OpenUrl(url):
    webbrowser.open_new(url)
def verb():
    os.system(cmdv)
    quit()
def nverb():
    os.system(cmd)
    quit()

menubar = Menu(master)
submenu = Menu(menubar)
reopnmenu = Menu(submenu)
reopnmenu.add_command(label='Verbosity', command=verb)
reopnmenu.add_command(label='Non-Verbosity', command=nverb)
submenu.add_command(label='Visit Website', command=lambda aurl=url:OpenUrl(aurl))
submenu.add_command(label='Exit',command=master.quit)
submenu.add_cascade(label='Reopen With...', menu=reopnmenu)
menubar.add_cascade(label='Menu', menu=submenu)

master.minsize(width=200,height=150)
master.resizable(width=FALSE,height=FALSE)
master.wm_title(args[0])
master.config(menu=menubar)


master.mainloop()
