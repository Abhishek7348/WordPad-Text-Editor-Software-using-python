import cz_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\ADARSH\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ADARSH\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("wordpad.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name="WordPad Editor",
    options={"build_exe": {"packages": ["tkinter", "os"], "include_files": [
        "icon.ico", 'tcl8.6t.dll', 'tk86t.dll', 'icons2']}},
    version="1.01",
    description="Tkinter Application",
    executables=executables
)
