from moodul import *

def main():
    s = []   
    k = [] 

    while True:
        print("\n1 - Registreerimine")
        print("2 - Autoriseerimine")
        print("3 - Nime/parooli muutmine")
        print("4 - Unustatud parool")
        print("5 - Lõpetamine")

        valik = input("Valik: ")

        if valik == "1":
            registreeri(s, k)

        elif valik == "2":
            current_user = autoriseeri(s, k)

        elif valik == "3":
            if current_user is None:
                print("Pole sisse logitud!")
            else:
                current_user = muuda(s, k, current_user)

        elif valik == "4":
            unustatud_parool(s, k)

        elif valik == "5":
            print("Programmi lõpp.")
            break

        else:
            print("Vale valik!")


if __name__ == "__main__":
    main()
