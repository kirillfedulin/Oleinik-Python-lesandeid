from MyModle import *


k = []
s = []


while True:
    valik = 0
    print("Menu")
    print("Sisseta palun mis te tahate: ")
    print("1 - regestreerimine")
    print("2 - Autoriserumine")
    print("3 - Nime muutmine")
    print("4 - Parooli taastamine")
    print("5 - Lõpetamine")
    ask = input(" ")
    
    if ask == "1":
        regestreerimine(k, s)
    elif ask == "2":
        autorimine(k, s)
    elif ask == "3":
        parolivahetus(k, s)
    elif ask == "4":
        paroolitaastamine(k, s)
    elif ask == "5":
        break
