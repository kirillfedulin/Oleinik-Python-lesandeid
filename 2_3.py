print("Tere! Olen sinu uus sõber - Python!")
name = input("Mis on sinu nimi? ")
print(f"{name}, oi kui ilus nimi")
try:
    ask = int(input(f"{name}, kas leian Sinu keha indeksi? 0-ei, 1-jah"))
    if ask == 1:
        print("Indski leidmine algab!")
        while True:
            try:
                pikkus = int(input("Mis on sinu pikkus cm? "))
                if 0 < pikkus <= 250:
                    break
                else:
                    print("Pikkus peab olema vahemikus 1 kuni 250 cm")
            except:
                print("Value andmed! Proovi uuesti.")
        while True:
                mass = int(input("Mis on sinu mass kg? "))
                if 0 < pikkus <= 350:
                    break
                else:
                    print("Mass peab olema vahemikus 1 kuni 350 kg")
        KMI = mass / (0.01 * pikkus) ** 2
        print(f"{name}, sinu kehamassiindeks on {KMI:.2f}")
        if KMI 	< 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= KMI < 19:
            print("Alakaal")
        elif 20 <= KMI < 25:
            print("Normaalkaal")
        elif 26 <= KMI < 30:
            print("Ülekaal")
        elif 31 <= KMI < 35:
            print("Rasvumine")
        elif 36 <= KMI < 40:
            print("Tugev rasvumine")
        elif KMI > 40:
            print("Tervisele ohtlik rasvumine")
except:
        print("Value andmed! Proovi uuesti.")



