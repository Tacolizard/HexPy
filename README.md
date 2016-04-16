#HexPy

HexPy is a project focused on using arrays of 8-byte color hexcodes. 

####To see the latest version of HexPy, [click here](https://github.com/Tacolizard/HexPy/releases/latest)

###Installation is easy:
1. Have Python 3.4 or later installed. 
**<strike>Note: on most Linux distros, you must install `python3-tk` as well</strike>**
**v2.0-release: `pgexec` now automatically downloads dependencies**
2. Download and decompress the `.zip` or `.tar` from Github
3. `cd` to the uncompressed directory
4. Do `chmod 777 pgexec`
5. Either add it to your PATH or run it with `./pgexec`

###To test HexPy:
1. Use a pre-made image or run the `ranhex.py` script to generate a test image.
2. From a terminal do `pgexec myimage.pgf`
You can also add a `v` at the end if you want to see live stats and errors raised directly from Python.
However, `v` tends to impact performance pretty heavily.
