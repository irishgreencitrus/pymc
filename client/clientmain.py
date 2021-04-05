import os
import subprocess
mcwd = os.path.expanduser("~") + "\\AppData\\Roaming\\.minecraft"
mcver = mcwd + "\\versions"
os.chdir(mcwd)
def listmc():
    mcls = os.listdir()
    for i in mcls:
        print(i)
def listver():
    os.chdir(mcver)
    mclsv = os.listdir()
    for i in mcls:
        print(i)
    os.chdir(mcwd)
def getallfile(dir, ext, mode):
    if mode == "p":
        for r, d, f in os.walk(dir):
            for file in f:
                if ext in file:
                    print(file)
    elif mode == "r":
        ret = []
        for r, d, f in os.walk(dir):
            for file in f:
                if ext in file:
                    ret.append(file)
        return ret
def launch():
    print("Which version would you like to launch?")
    ls = getallfile(mcver, ".jar", "r")
    for n, a in enumerate(ls, start=1):
        print("["+str(n)+"] "+ a)
    try:
        ch = int(input())
    except:
        print("That's not a Number! Exiting...")
        exit()
    try:
        pth = mcver + "\\" + ls[ch].replace(".jar","") + "\\" + ls[ch]
    except:
        print("Version not found! Exiting...")
        exit()
    run = "java -jar "+ pth + ""
    try:
        subprocess.call([run])
    except OSError:
        print(open(__file__).read() + "\n")
        print("There is an error with subprocess.call(), If anyone was willing to fix it I'd be grateful")
