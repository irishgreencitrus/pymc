import os
try:
    from . import handler
except:
    print("Import pymc into your project using import pymc \n")
    print("Main script shown below \n")
    print(open("handler.py").read() + "\n\n\n\n")
    print("PYMC MINECRAFT PYTHON LAUNCHER vA0.0.1")
    print("CREDITS SHOWN BELOW, ADD YOUR NAME TO THE LIST IF YOU EDIT THE MODULE ON GITHUB\n")
    credits = ["Dr Pickens"]
    for c in credits:
        print(c)
        print("\n")
    print("FIND THIS ON GITHUB https://github.com/DrPickens/pymc")
    os.system("start chrome.exe https://github.com/DrPickens/pymc")
