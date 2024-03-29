import os
import tkinter as tk
from tkinter import filedialog
import pathlib
import platform
#Define Variables
syst = platform.system()
if os.path.isfile("server.list") != True:
    open("server.list","a").close()
with open("server.list", "r") as servfile:
    servers = servfile.read().split(";")
#Define Functions
def listserv():
    """List all servers in server.list"""
    for s in servers:
        print(s)
def askfornew(prefixreq):
    """Open a file prompt to return path it gave"""
    #SideNote# if prefix req ends with a file ending you don't have in your file system while true will destroy you
    root = tk.Tk()
    root.withdraw()
    while True:
        new = filedialog.askopenfilename()
        if syst == "'Windows'":
            new = new.replace("/","\\")
        if new.endswith(prefixreq):
            return new
        else:
            continue
def add2data(pr):
    """Add path to server.list"""
    #SideNote# calls askfornew
    fil = open("server.list","a")
    fil.write("\"" + askfornew(pr) + "\"" + ";")
    fil.close()
    fil = open("server.list","r")
    global servers
    servers = fil.read().split(";")
    fil.close()
def servchoose():
    """Just a simple display of server.list"""
    numserv = []
    for num, s in enumerate(servers, start=1):
        if s != "":
            stro = "["+str(num)+"]" + s.replace("\"","")
            print(stro)
def getserv(num):
    """Simple function, one line long"""
    return servers[int(num)-1]
def runopt():
    """Options, probably something will break here"""
    global ram
    global gui
    ram = int(input("How many GB of ram?")) * 1024
    gui = input("-nogui [y/n]").lower()
    gui = "-nogui" if gui.lower().startswith("y") else ""
def runserv(path):
    """ISSUE: If there are spaces in the path, os.system freaks out #fixed!"""
    """Anyway, runs the flipping thing"""
    os.chdir(str(os.path.dirname(path)).replace("\"",""))
    cmd = "java -Xms" + str(ram) +"M -Xmx" + str(ram) + "M -jar " + str(path)
    os.system(cmd)
def testscript():
    """Just a quick testscript() {sorry i know that was horrible}"""
    if input("Add new server to list? (y/n)").lower().startswith("y"):
        add2data(".jar")
    print("\n")
    print("Which server would you like to run?")
    servchoose()
    pth = getserv(input())
    print("\n")
    runopt()
    runserv(pth)
testscript(

)
