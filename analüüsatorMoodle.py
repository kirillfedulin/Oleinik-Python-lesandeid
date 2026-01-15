import os
import glob

# Otsib praegusest kataloogist failid kasutaja antud laiendiga
def leia_projektifailid():
    fail = input("sisesta faililaiendi ilma punktita: ")
    failid = glob.glob(f'*.{fail}')  # leiab kõik vastava laiendiga failid
    print(f"Leitud failid: {failid}")
    return f"'.'+{fail} failid, {failid}"

# Loeb faili sisu ja otsib kindlat sõna
def analuusi_faili_sisu():
    while True:
        failitee = input("Sisesta faili tee: ")
        if not os.path.isfile(failitee):  # kontrollib, kas fail eksisteerib
            print("Faili ei leitud, proovi uuesti.")
        else:
            fail = open(failitee, 'r', encoding='utf-8')  # avab faili
            sisu = fail.read()  # loeb kogu faili sisu
            sõna = input("Sisesta sõna, mida otsida: ")
            sõna_count = sisu.lower().count(sõna.lower())  # loendab sõna esinemised
            length = len(sisu)  # faili pikkus märkides
        
            fail.close()  # sulgeb faili
            print(f"Sisu: {sisu}")
            print(f"Sõna '{sõna}' esinemiste arv: {sõna_count}")
            print(f"Faili pikkus: {length} tähemärki")
            break
    return f"{sõna_count}\nFaili pikkus: {length}\nSISU FAILIST:\n {sisu}\n"

# Loob, kustutab või otsib kataloogi
def loo_raporti_kataloog():
    while True:
        failitee = input("Sisesta raporti kataloogi tee: ")
        ask = input("Kas soovid lisada või kustutada või otsida kataloogi? (l/k/o)").lower()
        
        if ask == 'l':  # kataloogi loomine
            if not os.path.isdir(failitee):
                os.mkdir(failitee)
                return f"Kataloog {failitee} on loodud"
            else:
                print("Kataloog on juba olemas.")
                break

        elif ask == 'k':  # kataloogi kustutamine
            if not os.path.isdir(failitee):
                print("Kataloogi ei leitud. Palun proovi uuesti.")  
            else:
                ask2 = input("Kas soovid kataloogi kustutada? (jah/ei)")
                if ask2.lower() == 'jah':
                    os.rmdir(failitee)
                    return f"Kataloog {failitee} on kustutatud"
                else:
                    print("Kataloogi kustutamine katkestatud.")
                    break
                
        elif ask == 'o':  # kataloogi otsimine
            if not os.path.isdir(failitee):
                print("Kataloogi ei leitud.")
            else:
                print(f"Kataloog {failitee} on leitud.")
                break
      
    return f"{failitee} on leitud"

# Leiab failid, mis algavad kindla tähega
def leia_failid_algustahega():
    while True:
        algustaht = input("Sisesta algustäht: ")
        if not algustaht.isalpha() or len(algustaht) != 1:
            print("Palun sisesta üks täht.")
        else:
            break

    failid = glob.glob(f'{algustaht}*')  # leiab failid algustähe järgi
    print(f"Leitud failid: {failid}")
    return f"algustäht failid {algustaht}:\nFailid: {failid}\nKui palju: {len(failid)}"
