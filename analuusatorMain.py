import analüüsatorMoodle
import os

# Kuvab praeguse töökataloogi
print(os.getcwd())

# Loeb kõik failid praegusest kataloogist
failid = os.listdir()

# Kogub unikaalsed faililaiendid
laiendid = set()
for f in failid:
    if '.' in f:
        laiendid.add(f.split('.')[-1])

# List, kuhu salvestatakse tegevuste tulemused
stat = []        

# Peamenüü tsükkel
while True:
    valik = input(
        "Vali tegevus:\n"
        "1. Leia projektifailid\n"
        "2. Analüüsi faili sisu\n"
        "3. Loo raporti kataloog\n"
        "4. Leia failid algustähega\n"
        "5. Välju\n"
        "Sisesta valik (1-5): "
    )

    # Kontrollib, kas valik on korrektne
    if valik not in ['1', '2', '3', '4', '5']:
        print("Vigane valik, proovi uuesti.")
        continue

    try:
        # Otsib projektifailid kindla laiendiga
        if valik == '1':
            faililaiend = analüüsatorMoodle.leia_projektifailid()
            stat.append(faililaiend)

        # Analüüsib faili sisu (sõnade arv, pikkus jne)
        elif valik == '2':
            analuus = analüüsatorMoodle.analuusi_faili_sisu()
            stat.append(analuus)

        # Loob, kustutab või otsib raporti kataloogi
        elif valik == '3':
            raport = analüüsatorMoodle.loo_raporti_kataloog()
            stat.append(raport)

        # Leiab failid kindla algustähega
        elif valik == '4':
            algustahed = analüüsatorMoodle.leia_failid_algustahega()
            stat.append(algustahed)

        # Väljub programmist
        elif valik == '5':
            print("Väljutamine...")
            break

    except:
        # Püüab kinni võimalikud vead
        print("Ilmnes viga, proovi uuesti.")

# Kui statistika fail juba eksisteerib, kustutatakse see
if os.path.isfile('statistika.txt'):
    os.remove("statistika.txt")

# Salvestab kogutud statistika faili
with open("statistika.txt", 'w', encoding='utf-8') as f:
    for rida in stat:
        f.write(str(rida) + "\n")

print("Statistika on salvestatud faili 'statistika.txt'.")
