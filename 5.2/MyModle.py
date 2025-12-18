def registreeri(s, k):
    nimi = input("Sisesta uus kasutajanimi: ")
    if nimi in s:
        print("Nimi juba võetud!")
        return

    parool = input("Sisesta parool: ")
    if len(parool) < 4:
        print("Parool liiga lühike!")
        return

    s.append(nimi)
    k.append(parool)
    print("Registreerimine õnnestus!")


def autoriseeri(s, k):
    nimi = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")

    if nimi not in s:
        print("Sellist kasutajat pole!")
        return None

    i = s.index(nimi)
    if k[i] != parool:
        print("Vale parool!")
        return None

    print("Sisselogimine õnnestus!")
    return nimi


def muuda(s, k, current_user):
    i = s.index(current_user)

    print("1 - Muuda nime")
    print("2 - Muuda parooli")
    valik = input("Valik: ")

    if valik == "1":
        uus_nimi = input("Uus nimi: ")
        if uus_nimi in s:
            print("Nimi juba võetud!")
        else:
            s[i] = uus_nimi
            print("Nimi muudetud!")
            return uus_nimi

    elif valik == "2":
        uus_parool = input("Uus parool: ")
        k[i] = uus_parool
        print("Parool muudetud!")

    return current_user


def unustatud_parool(s, k):
    nimi = input("Sisesta kasutajanimi: ")
    if nimi not in s:
        print("Sellist kasutajat pole!")
        return

    i = s.index(nimi)
    uus = input("Sisesta uus parool: ")
    k[i] = uus
    print("Parool taastatud!")
