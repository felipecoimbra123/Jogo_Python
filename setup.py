from cx_Freeze import setup, Executable
import sys
 
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
 
executables = [Executable("jogo1.py", base=base)]
 
packages = ["tkinter"]
options = {
    'build_exe': {
        'packages':packages
    }, 
}
 
setup(
    name = "Luta de boxe",
    options = options,
    version = "1.0",
    description = 'Trabalho: Jogo em Python',
    executables = executables
)