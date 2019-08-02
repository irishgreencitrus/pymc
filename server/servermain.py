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
    global servers
    servers = fil.read().split(";")
    fil.close()
def servchoose():
    numserv = []
    num = 0
    for s in servers:
        num += 1
        if s != "":
            stro = "["+str(num)+"]" + s
            print(stro)
def getserv(num):
    return servers[int(num)-1]
def runopt():
    global ram
    global gui
    ram = int(input("How many GB of ram?")) * 1024
    gui = input("-nogui [y/n]").lower()
    if gui.lower().startswith("y"):
        gui = "-nogui"
    else:
        gui = ""
def runserv(path):
    cmd = "java -Xms" + str(ram) +"M -Xmx" + str(ram) + "M -jar" + str(path)
    subprocess.call([cmd])
def testscript():
    if input("Add new server to list? (y/n)").lower().startswith("y"):
        add2data(".jar")
    print("\n")
    print("Which server would you like to run?")
    servchoose()
    pth = getserv(input())
    print("\n")
    runopt()
    runserv(pth)
testscript()
