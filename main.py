# 2.alkalom
import random
from importlib.metadata import pass_none
from types import new_class

'''szam = input("Kérek egy számot: ")
if szam.isdigit():
    szam = int(szam)
    if szam > 0:
        print("Pozitív")
    elif szam < 0:
        print("Negatív")
    else:
        print("Nulla")
else:
    print("Nem számot adtál meg.")'''

'''jegy = int(input("Kérek egy érdemjegyet: "))
while jegy == 1 or jegy > 5 or jegy < 1:
    jegy = int(input("Kérek egy érdemjegyet: "))
    if jegy == 10:
        print ("Csillagos ötös!")
        break
else:
    print("Jól teljesített.")
print ("Gratulálunk")'''

'''kocka = random.randint(1,6)
while True:
    tipp = int(input("Kérek egy tippet: "))
    if tipp == kocka:
        break
print ("Sikerült eltalálnod a számot!")'''

'''uzenet = "Jó reggelt"
for betu in uzenet:
    print(betu)
    if betu == " ":
        break'''

'''for _ in range(5):
    print("Nem leszek többet rossz.")
for elem in range(1, 4):
    print(elem, "Soha nem leszek többet rossz.")'''

'''try:
    print(10/0)
except ZeroDivisionError:
    print("HIBA! Nullával osztás.")
except NameError:
    print("HIBA! Névhiba.")
print("OK")'''

while True:
    try:
        szam = int(input("Kérek egy egész számot: "))
    except:
        print("Nem egész számot adott meg!")
    else:
        break