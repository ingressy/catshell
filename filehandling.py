import os

def file_ls():
    files = os.listdir('D:\catshell\sysfile')
    print(files)

def file_nano():
    filename = input("ingressy ~ filename -> ")
    if filename != "exit":
        os.system('notepad "D:\catshell\sysfile\\' + filename + '"')
