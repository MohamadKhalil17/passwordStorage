# -*- coding: utf-8 -*-
"""
@author: Mohamad Khalil
"""
#password storage

def decrypt(Word):
    string=""
    for i in range(len(Word)):
        string+=chr(ord(Word[i]) - 5)
    return string

def encrypt(Word):
    string=""
    for i in range(len(Word)):
        string+=chr(ord(Word[i]) + 5)
    return string 

def add():
    username=input("please enter the Username: ")
    password=input("please enter the Password: ")
    with open('password_storage.txt','a') as file:
        name=encrypt(username)
        passWord=encrypt(password)
        file.write(name+"|"+passWord+"\n")
    print("Username and password successfully added!")

def view():
    with open('password_storage.txt','r') as file:
        for line in file.readlines():
            data=line.rstrip()
            user, password=data.split("|")
            name=decrypt(user)
            passWord=decrypt(password)
            print(name+"|"+passWord+"\n")

def Quit():
    pass

def Operation(numberIncorrect2):
    operation=input("Do you want to add a new password or edit existing ones?(add,view,quit): ")
    if operation=="add":
        add()
    elif operation=="view":
        view()
    elif operation=="quit":
        Quit()
    else:
        print("Invalid input!")
        numberIncorrect2+=1
        if numberIncorrect2<5:
            Operation(numberIncorrect2)
        else:
            print("Many wrong attempts! Forced to quit!")
            


def checkMasterPassword(p,numberIncorrect1):
    if p==masterPass:
        Operation(numberIncorrect2)
    else:
        print("Invalid Password")
        numberIncorrect1+=1
        if numberIncorrect1<5:
            pa=input("please enter password to access items: ")
            checkMasterPassword(pa,numberIncorrect1)
        else:
            print("Many wrong attempts! Forced to quit!")
             


masterPassword=input("please enter password to access items: ")
masterPass="hello"
numberIncorrect1=0
numberIncorrect2=0
checkMasterPassword(masterPassword,numberIncorrect1)