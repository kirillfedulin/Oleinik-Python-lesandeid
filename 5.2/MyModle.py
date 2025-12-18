import random

def rand (k):
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    print(psword)
    return psword
    k.append(psword)



def rand_nimi (s):
    nimi = input("Sisesta uus kasutajanimi: ")
    if nimi in s:
        print("Nimi juba võetud!")
        return
    s.append(nimi)



def no_rand_parool(k):
    print("Peab sisaldama numbrit")
    print("Peab sisaldama väikest tähte")
    print("Peab sisaldama suurt tähte")
    print("Peab sisaldama erimärki")
    print("Kui te ei tahtate tegi parool, sisetaja (ei)")

    while True:
        parool = input("Sisesta parool: ")

        if parool == "ei":
            print("Registreerimine katkestatud")
            break

        on_number = False
        on_lower = False
        on_upper = False
        on_special = False

        for t in parool:
            if t.isdigit():
                on_number = True
            elif t.islower():
                on_lower = True
            elif t.isupper():
                on_upper = True
            else:
                on_special = True

        if on_number and on_lower and on_upper and on_special:
            print("Parool on tugev")
            k.append(parool)
            print("Registreerimine õnnestus!")
            break
        else:
            print("Parool EI vasta nõuetele")
            if not on_number:
                print("- Puudub number")
            if not on_lower:
                print("- Puudub väike täht")
            if not on_upper:
                print("- Puudub suur täht")
            if not on_special:
                print("- Puudub erimärk")



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
