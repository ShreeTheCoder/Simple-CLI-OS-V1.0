import os
from termcolor import colored

global user

#write the username in a .txt file
with open("username.txt", "r") as file:
    file_text = file.read()
    user = file_text

#os logo colors
os_logo_first = colored("Simple", "light_red")
os_logo_second = colored("CLI", "light_green")
os_logo_third = colored("OS", "light_blue")

#user account colors
user_text = colored(user, "red")

print("-" * 20)
print(os_logo_first + " " + os_logo_second + " " +os_logo_third)
print("-" * 20)

print("Read \"Instructions.txt\" For Commands.")
print("-" * 20)

while True:
    if user != "mainuser":
        user = user

    command = input(user_text + ": ").lower()

    #exit command
    if command == "exit":
        verification = input("Are you sure that you want to exit? [y/n]: ").lower()
        if verification != "y":
            continue
        else:
            exit()

    #bios command
    if command == "bios":
        verification = input("Are you sure that you want to enter bios? [y/n]: ").lower()
        if verification != "y":
            continue
        else:
            os.startfile("Phantom BIOS.py")

    #ruser command
    if command == "ruser":
        with open("username.txt", "w") as file:
            file.write("root")

    #terminal command
    if command == "terminal":
        os.startfile("\\Applications\\terminal\\Terminal.py")