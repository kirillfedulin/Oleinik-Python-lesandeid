import random
import json

FAILI_NIMI = "riigid_pealinnad.json"


def lae_andmed():
    try:
        with open(FAILI_NIMI, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "Eesti": "Tallinn",
            "Soome": "Helsingi",
            "Rootsi": "Stockholm",
            "Norra": "Oslo",
            "Saksamaa": "Berliin",
            "Prantsusmaa": "Pariis"
        } 

def salvesta_andmed(sonastik):
    with open(FAILI_NIMI, "w", encoding="utf-8") as f:
        json.dump(sonastik, f, ensure_ascii=False, indent=4)

def otsi(sonastik):
    sisend = input("Sisesta riik või pealinn: ").strip()

    if sisend in sonastik:
        print(f"Pealinn: {sonastik[sisend]}")
    elif sisend in sonastik.values():
        for riik, pealinn in sonastik.items():
            if pealinn == sisend:
                print(f"Riik: {riik}")
                break
    else:
        print("Ei leitud.")
        lisa = input("Kas soovid selle lisada? (jah/ei): ").lower()
        if lisa == "jah":
            riik = input("Sisesta riik: ")
            pealinn = input("Sisesta pealinn: ")
            sonastik[riik] = pealinn
            salvesta_andmed(sonastik)
            print("Lisatud!")


def paranda(sonastik):
    riik = input("Sisesta riigi nimi, mida parandada: ")
    if riik in sonastik:
        uus = input(f"Sisesta õige pealinn ({sonastik[riik]} → ): ")
        sonastik[riik] = uus
        salvesta_andmed(sonastik)
        print("Parandatud!")
    else:
        print("Riiki ei leitud.")


def test(sonastik):
    kysimusi = min(5, len(sonastik))
    õiged = 0
    riigid = list(sonastik.keys())

    for _ in range(kysimusi):
        riik = random.choice(riigid)
        vastus = input(f"Mis on riigi {riik} pealinn? ")

        if vastus.lower() == sonastik[riik].lower():
            print("Õige!")
            õiged += 1
        else:
            print(f"Vale! Õige vastus on {sonastik[riik]}")

    tulemus = õiged / kysimusi * 100
    print(f"\nTulemus: {tulemus:.0f}%")

"""
def loe_ette(tekst):
    engine = pyttsx3.init()
    engine.say(tekst)
    engine.runAndWait()
"""

def menuu():
    sonastik = lae_andmed()

    while True:
        print("\n--- RIIGID JA PEALINNAD ---")
        print("1. Otsi riiki või pealinna")
        print("2. Paranda viga")
        print("3. Testi oma teadmisi")
        print("4. Välju")

        valik = input("Valik: ")

        if valik == "1":
            otsi(sonastik)
        elif valik == "2":
            paranda(sonastik)
        elif valik == "3":
            test(sonastik)
        elif valik == "4":
            print("Head õppimist!")
            break
        else:
            print("Vale valik!")


menuu()
