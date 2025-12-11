

k = []
s = []

def regestreerimine(k: list, s: list)->any:
    while True:
        nimi = input("\nSisesta uus kasutajanimi: ")
        if nimi in k:
            print("Nimi juba võetud!")
            continue

        parool = input("Sisesta parool: ")
        if len(parool) < 4:
            print("\nNõrk parool!")
            continue

        k.append(nimi)
        s.append(parool)
        print("\nRegistreerimine õnnestus!\n")
        return


def autorimine(k: list, s: list)->any:
    while True:
        nimi = input("\nSisesta kasutajanimi: ")
        parool = input("Sisesta parool: ")

        if nimi not in k:
            print("\nSellist kasutajat pole!")
            continue

        i = s.index(nimi)
        if s[i] != parool:
            print("\nVale parool!")
            continue

        print("\nSisselogimine õnnestus!\n")
        return nimi


def parolivahetus(k: list, s: list, ks: list)->any:
    i = k.index(ks)
    print("\n1 - Muuda nime")
    print("2 - Muuda parooli\n")
    valik = input("Valik: ")

    if valik == "1":
        uus_nimi = input("\nUus nimi: ")
        if uus_nimi in k:
            print("\nNimi juba võetud!\n")
        else:
            k[i] = uus_nimi
            print("\nNimi muudetud!\n")
            return uus_nimi
    elif valik == "2":
        uus_parool = input("\nUus parool: ")
        s[i] = uus_parool
        print("\nParool muudetud!\n")

    return ks


def paroolitaastamine(k: list, s: list)->any:
    nimi = input("\nSisesta kasutajanimi: ")
    if nimi not in k:
        print("\nSellist kasutajat pole!\n")
        return

    i = k.index(nimi)
    uus = input("Sisesta uus parool: ")
    s[i] = uus
    print("Parool taastatud!")
