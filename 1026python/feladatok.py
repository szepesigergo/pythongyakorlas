import math


def egy():
    i = 0
    while i < 150:
        if i % 2 == 0:
            print(i, end=", ")
        i += 1
    print(150, end="")


def ketto():
    osztharom = 0
    sorszam = 1

    while sorszam <= 10:
        szam = int(input("Kérem adjon meg "+str(sorszam)+". számot:"))
        if szam % 3 == 0:
            osztharom += 1
        sorszam += 1
    print("A bekért számok alapján "+str(osztharom)+" olyan szám található, amely 3-mal osztható.")


def harom():
    szam = int(input("Kérem adjon meg számokat: "))
    while not (szam % 10 == 0):
        szam = int(input("Kérem adjon meg számokat: "))
    print("10-el osztható")


def negy():

    szam = int(input("Kérem adjon meg egy számot: "))

    while not ((((szam >= 10) and (szam <= 99)) or ((szam >= -99) and (szam <= -10))) and (szam % 2 == 0)):
        szam = int(input("Kérem adjon meg egy számot: "))


def ot():

    szam = int(input("Kérem adjon meg egy számot: "))

    while not ((szam > 0) and (szam % 2 == 1)):
        szam = int(input("Kérem adjon meg egy számot: "))


def hat():

    szam = int(input("Kérem adjon meg egy számot: "))

    while not ((szam % 3 == 0) and (int(math.sqrt(szam)))):
        szam = int(input("Kérem adjon meg egy számot: "))


def het():
    a = float(input("Kérem adjon meg egy valós számot: "))
    b = float(input("Kérem adjon meg egy másik valós számot: "))
    c = float(input("Kérem adjon meg egy harmadik valós számot: "))
    while not ((a > b+c) and (b < a+c) and (c < a+b)):
        print("A háromszög nem szerkeszhető!")
        a = float(input("Kérem adjon meg egy valós számot: "))
        b = float(input("Kérem adjon meg egy másik valós számot: "))
        c = float(input("Kérem adjon meg egy harmadik valós számot: "))
    print("A háromszög szerkeszthető!")
