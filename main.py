import os
from ctypes import *
import filehandling, help

print("catshell ~ {version v1.0}")
status = os.path.getsize('sysram.txt')
print(str(status) + "KB Speicher belegt")
print("(c) ingressy 2023\n")

while True:
    cli = input("ingressy ~ cs:\\home -> ")
    with open('sysram.txt', 'w') as f:
        f.write(cli)

    fcli = open('sysram.txt', 'r')
    rcli = fcli.read()
    if rcli.lower() == "stop":
        exit(1)
    elif rcli.lower() == "help":
        pass
    elif rcli.lower() == "ls":
        filehandling.file_ls()
    elif rcli.lower() == "nano":
        filehandling.file_nano()
    elif rcli.lower() == "info":
        user32 = WinDLL('user32.dll')

        window_handle = 0

        user32.MessageBoxA(
            window_handle,
            b'Version: v0.1\n'
            b'Coded by ingressy\n'
            b'(c) 2023-',
            b'catshell',
        )
    elif rcli.lower() == "status":
        status = os.path.getsize('sysram.txt')
        print(str(status) + "KB Speicher belegt")
    else:
        print("'" + cli + "' Mhm ... dieser Befehl existiert nicht. ^^")
