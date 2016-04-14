#HexPy

HexPy is a lightweight family of tools for creating, modifying, and displaying 8-byte color hexcodes. By using arrays of colorhexes to output graphics, a programmer has simple yet powerful access to the exact pixels being displayed on the screen. 

Currently HexPy is in Beta, working towards Release 1. R1 will be achieved once all the issues with the "Release 1" milestone are closed. R1 is intended to be the first half of HexPy, a set of CLI scripts for creating and displaying colorhexes. The second half, Release 2, is planned to be an import-able Python 3 library containing all the existing R1 features and more.

The beta version of the main tool, pgexec, is available for download. pgexec is a CLI script for outputting colorhexes. More info below and in the pgexec README.


Excerpt from the pgexec library:

#1. Modification
This is open source. Anyone can modify this code without my permission, as long as they tell me that they’ve modified it, and I receive credit wherever they post their version of the code.

#2. Requirements/Dependencies
Any version of Python 3 should be fine. This is incompatible with Python 2. If you are using Python 3 and experience errors or problems, try running the code on Python 3.5, that’s what this was made with. Also note that this requires a lot of the built-in libraries that come with the standard Python 3.5 installation, such as tkinter.

Other than that, there are no dependencies

#3.Possible Incompatibilities
This code was made on a mac!(for Python programming, linux > mac > windows imo). I couldn’t test (aka was too lazy) the system commands on other oses! This should work with linux but not windows, however there is good news! The only parts that should be incompatible are the the os.system(‘clear’) things. These should be fairly easy to change.

#6. Extras
The code is heavily commented if you want to read through it. It’s a really simple and probably poorly written program :P. I tried to do my best to explain everything, though there’s not a whole lot of code to explain, and anyone even slightly above my skill level (probably 99% of Python users) should understand. Also, I threw in an extra crappy chef surprise in the form of ranhenx.py. It’s a poorly made script for generating hex values to put in my ‘.pgf’ format, to be read by pgexec. 
