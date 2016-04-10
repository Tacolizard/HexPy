#!/usr/bin/env python3

#Pygraphics image processor, a simple way to open images in the .pgf format
#basically opens arrays of color hex values, and draws them by guessing dimensions

#only works with square images. If you want anything else, like rectangular or anything irregular,
#you must add a square of alpha transparancy (or any color) around the image as a background.
#for this reason and others, I'm working on an image converter

#surprisingly, .pgf is about as efficient as an uncompressed jpeg image.
#also, I will potentially make an image compressor for .pgf


from tkinter import *
import sys
import os

sys.argv

#cleanup sys args from command line
args = sys.argv
args.remove("/usr/bin/pgexec")#change this if your script/path is in a different location. Also I don't know
#if this is required on Linux or Windows

#attempt to open file
try:
    file = open(args[0])
except FileNotFoundError:
    os.system('clear')
    print('PGexec Error 10;file not found: \nNo such file or directory','["',args[0],'"]')
    try:
        if args[1]=="v":
            raise
    except IndexError:
        quit()
    quit()
except IndexError:
    os.system('clear')
    print("PGexec Error 30;no command given: \nYou must use a command. \nSyntax, type without quotes: \npgexec 'relative directory of .pgf file' 'v'(optional error verbosity)")
    quit()
#attempt to read file
try:
    f = file.read()
    exec(f)
except UnicodeDecodeError:
    os.system('clear')
    print("PGexec Error 20;invalid image file: \nimage is not decodeable by UTF-8\nplease use images in .pgf format only")
    try:
        if args[1]=="v":
            raise
    except IndexError:
        quit()
    quit()
except SyntaxError:
    os.system('clear')
    print("PGexec Error 22;invalid image file: \ninvalid Python syntax\nplease use images in .pgf format only")
    try:
        if args[1]=="v":
            raise
    except IndexError:
        quit()
    quit()


#start tkinter;main part of the program
master = Tk()

c = Canvas(master, width=w, height=len(pix) / w)
c.pack()

#define draw placement variables, set up hex array to be accessed
x=2
y=2
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
            os.system('clear')
            print("PGexec Error 21;invalid image file: \ntotal number of pixels can't be evenly divided by image width")
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
    os.system("clear")

    #give progress and size info
    print("Drawing from array...")
    print("Progress:",line,"/",w)
    print("Image size:",os.path.getsize(args[0]),"bytes")
    if line > w:#invalidate file if it dosen't fit .pgf format. won't cause a python error,
        os.system('clear')#but will mess up stats and won't render correctly
        print("PGexec Error 23;invalid image file: \nimage is not square")
        try:
            if args[1]=="v":
                print("Not a Python error")
        except IndexError:
            quit()
        quit()

#when finished drawing, show some stats while tk loads
os.system('clear')
print("Finished! Wait for tk to load.")
print('Dimensions:',w,'x',line)
print("Total # of pixels drawn:",w*w)
print("Image size:",os.path.getsize(args[0]),"bytes")

mainloop()

#small loan of a million hidden memes army represent!!!
