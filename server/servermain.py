import os
import subprocess
import tkinter as tk
from tkinter import filedialog
#Define Variables
servfile = open("server.list", "r")
servers = servfile.read().split(";")
servfile.close()
#Define Functions
def listserv():
    for s in servers:
        print(s)
def askfornew(prefixreq):
    root = tk.Tk()
    root.withdraw()
    while True:
        new = filedialog.askopenfilename()
        new = new.replace("/","\\")
        if new.endswith(prefixreq):
            return new
        else:
            continue
def add2data(pr):
    fil = open("server.list","a")
    fil.write(askfornew(pr) + ";")
    fil.close()
    fil = open("server.list","r")
    servers = fil.read().split(";")
    fil.close()
print(servers)
add2data(".jar")
print(servers)
