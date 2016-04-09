# pgexec
Pygraphics is a family of tools to work with color hexcodes. The main tool, pgexec, is a simple command line script to output arrays of color hexcodes as images. Written in Python.





From the pgexec readme:

Thanks for downloading my code! I really appreciate that someone actually wants to run something I made :P. If you realy like it, you could consider sending a small loan of a million dollars mabye?

Pygraphics v1.0
4/9/16

#1. Modification
This is open source. Anyone can modify this code without my permission, as long as they tell me that they’ve modified it, and I receive credit wherever they post their version of the code.

#2. Requirements/Dependencies
Some version of Python 3 should be fine. This is incompatible with Python 2. If you are using Python 3 and experience errors or problems, try running the code on Python 3.5, that’s what this was made with. Also note that this requires a lot of the built-in libraries that come with the standard Python 3.5 installation, such as tkinter.

Other than that, there are no dependencies

#3.IMPORTANT!!!!RAAAAHHH!!!INCOMPATIBILITIES!!!!!!RAAAAA!!!
This code was made on a mac!(for Python programming, linux > mac > windows imo). I couldn’t test (aka was too lazy) the system commands on other oses! This should work with linux but not windows, however there is good news! The only parts that should be incompatible are the the os.system(‘clear’) things. These should be fairly easy to change.

#4. How to Make Images/Program Description
This program is designed to open files containing python scripts that look like this:

(This won't render, it's for error testing)

w = 5
pix = ["#004356","#004356","#004356","#000000","#ffffff","#000000","#000000","#ffffff","#000000","#ffffff","#000000","#000000","#ffffff","#000000","#ffffff","#000000","#000000","#ffffff”]

The program reads through a list of hex values and draws them left to right, line by line. It ends the line and goes to the next when it detects that it has drawn the number of pixels specified with the variable w, which means width. If w=5, each line is drawn 5 pixels long. This method avoids assigning coordinates to the hex values. As of right now, the first version, it cannot render rectangles. It can only render 1:1 squares. Because of this, you must make sure that your image is 1:1, or it will not render. To do this, you must have a list of hex values with a len(pix) length that when divided by w, equals w. Or more simply:

if w==len(pix)/w:
	print(“You have a valid 1:1 square image”)
else:
	print(“You dun diddly did the wrong number of pixels, boy”)

(pix is your list of hex values)

Remember, your hex array must be defined as pix, and you must define your image width as w

#5. Installation and Use
finally, we’re here at the last part. pgexec.py is the source code, not meant to be run. To use pgexec, you want to run the extension-less ‘pgexec’ from the command line/cmd/terminal. Drag and drop pgexec (which is just the source code without the extension) into your PATH folder. Or you can add it to your path however you like.

To use it, just type without quotes: pgexec ‘relative filename/directory of image’

You can also add a space and a ‘v’ after the directory to see more verbose errors.

#6. Extras
The code is heavily commented if you want to read through it. It’s a really simple and probably poorly written program :P. I tried to do my best to explain everything, though there’s not a whole lot of code to explain, and anyone even slightly above my skill level (probably 99% of Python users) should understand. Also, I threw in an extra crappy chef surprise in the form of ranhenx.py. It’s a poorly made script for generating hex values to put in my ‘.pgf’ format, to be read by pgexec. 

#7. Vape Naysh yall
