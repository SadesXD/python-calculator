from os import system as sp
import math

# clear the console function
def cls():
    sp('cls')

# is not a number function
def nan(x):
    if type(x) != int:
        try:
            int(x)
        except:
            return False
    else:
        int(x)
        return True

# back to main menu function
def balek():
    teks = '\ntype [ BACK ] -> for back to main menu\ntype [ EXIT ] -> for stop the process\n\ntype your selection: '
    tes = input(teks)
    if tes.lower() == "back":
        cls()
        menu()
    elif tes.lower() == "exit":
        quit()
    else:
        cls()
        print("Can't found the options")
        balek()

# if wrong input will show the message function
def ada(x,kata):
    if not x or x == "":
        teks = "You are not giving anything\n"
    else:
        teks = f'[ {kata} ]\n"{x}" must be number\n'
    print(teks)

def tambah():
    cls()
    print("[ Add a number ]\n")
    k1 = input("Please give the first number: ")
    while nan(k1) == False:
        cls()
        ada(k1,"Add a number")
        k1 = input("Please give the first number: ")
    k2 = input("Please give the second number: ")
    while nan(k2) == False:
        cls()
        ada(k1,"Add a number")
        k2 = input("Please give the second number: ")
    hasil = int(k1) + int(k2)
    print(f'[ + ] = {k1} + {k2}\n      = {hasil}')
    balek()

def kurang():
    cls()
    print("[ Subtract a number ]\n")
    k1 = input("Please give the first number: ")
    while nan(k1) == False:
        cls()
        ada(k1,"Subtract a number")
        k1 = input("Please give the first number: ")
    k2 = input("Please give the second number: ")
    while nan(k2) == False:
        cls()
        ada(k1,"Subtract a number")
        k2 = input("Please give the second number: ")
    hasil = int(k1) - int(k2)
    print(f'[ - ] = {k1} - {k2}\n      = {hasil}')
    balek()

def kali():
    cls()
    print("[ Multiplying a number ]\n")
    k1 = input("Please give the first number: ")
    while nan(k1) == False:
        cls()
        ada(k1,"Multiplying a number")
        k1 = input("Please give the first number: ")
    k2 = input("Please give the second number: ")
    while nan(k2) == False:
        cls()
        ada(k1,"Multiplying a number")
        k2 = input("Please give the second number: ")
    hasil = int(k1) * int(k2)
    print(f'[ x ] = {k1} x {k2}\n      = {hasil}')
    balek()

def bagi():
    cls()
    print("[ Divide a number ]\n")
    k1 = input("Please give the first number: ")
    while nan(k1) == False:
        cls()
        ada(k1,"Divide a number")
        k1 = input("Please give the first number: ")
    k2 = input("Please give the second number: ")
    while nan(k2) == False:
        cls()
        ada(k1,"Divide a number")
        k2 = input("Please give the second number: ")
    hasil = int(k1) / int(k2)
    print(f'[ / ] = {k1} / {k2}\n      = {hasil}')
    balek()

def akarKuadrat():
    cls()
    print("[ Square root a number ]\n")
    k1 = input("Please give the number: ")
    while nan(k1) == False:
        cls()
        ada(k1,"Square root a number")
        k1 = input("Please give the number: ")
    hasil = math.sqrt(int(k1))
    print(f'[ \/ ] = \/{k1}\n      = {hasil}')
    balek()

def kuadrat():
    cls()
    print("[ Squares a number ]\n")
    k1 = input("Please give the first number: ")
    while nan(k1) == False:
        cls()
        ada(k1,"Squares a number")
        k1 = input("Please give the first number: ")
    k2 = input("How many number will you pow ??: ")
    while nan(k2) == False:
        cls()
        ada(k1,"Squares a number")
        k2 = input("How many number will you pow ??: ")
    hasil = math.pow(int(k1),int(k2))
    print(f'[ ^ ] = {k1}^{k2}\n      = {hasil}')
    balek()

def menu():
    teks = f'[ Simple python calculator ]\n\n1. [ + ] -> Add a number \n2. [ - ] -> subtract a number\n3. [ x ] -> multiplying a number\n4. [ / ] ->  divide a number\n5. [ \/ ] -> square root of a number\n6. [ ^ ] -> squares of a number\n\n- type [ EXIT ] -> for exit the calculator program\n\nSelect the number will you switch: '
    p = input(teks)
    if p.lower() == "exit":
        quit()
    elif p == "1":
        tambah()
    elif p == "2":
         kurang()
    elif p == "3":
        kali()
    elif p == "4":
        bagi()
    elif p == "5":
        akarKuadrat()
    elif p == "6":
        kuadrat()
    else:
        cls()
        print("Can't find your options\n")
        balek()
    
menu()  
