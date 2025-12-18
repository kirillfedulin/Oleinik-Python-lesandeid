from MyModle import *


s = ["Danya", "Artur", "Nikita"]  
k = ["2412", "1twet", "1f33"]  
praegune_kasutaja = None

while True:
        print("\n1 - Registreerimine")
        print("2 - Autoriseerimine")
        print("3 - Nime/parooli muutmine")
        print("4 - Unustatud parool")
        print("5 - Lõpetamine")

        valik = input("Valik: ")

        if valik == "1":
            ask = input("Kas te tahate teete sinu parool või random?")
            if ask == "random":
                rand(k)
                rand_nimi(s)
            elif ask == "minu":
                rand_nimi(s)
                no_rand_parool(k)
            else:
                print("Kirjuta palun minu või random")

        elif valik == "2":
            praegune_kasutaja = autoriseeri(s, k)

        elif valik == "3":
            if praegune_kasutaja is None:
                print("Pole sisse logitud!")
            else:
                praegune_kasutaja = muuda(s, k, praegune_kasutaja)

        elif valik == "4":
            unustatud_parool(s, k)

        elif valik == "5":
            print("Programmi lõpp.")
            break

        else:
            print("Vale valik!")

