import random
# 1.feladat
sorozat = [-3, 5, 11, -2, 4]

def Masodikfeladat(a):
    print(*sorozat, sep=a)

def Masodikelsőfeladat():
    num = int(random.uniform(5, 12))
    sorozat[0] += num
    Masodikfeladat(";")

def Masodikmasodikfeladat():
    szam = int(input("+-al osztható nem páros kétjegyű szám: "))

    while not ((szam >= 10) and (szam <= 99) and (szam % 2 == 1) and (szam % 3 == 0)):
        szam = int(input("+-al osztható nem páros kétjegyű szám: "))

    print(szam)

def Masodikharmadikfeladat():
    Masodikfeladat(" ")

def Masodikotodikfeladat():
    prim = 0
    while not (())