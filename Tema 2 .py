

#paev = input("Sisesta nädalapäev => ")
#if paev == "neljapäev":
#   print("täna on minu lemmik programmrimine!")
#else:
#    print("Ma tahan programerida teha!")
#
#if paev == "laupäev" or paev == "pühapäev":
#    print("Hurra")
#else:
#    print("Tuleb kooli minna")
#
# I-esmaspäev 2-teisipäev 3-kolmapäev 4-neljapäev 5-reede 
#paev_number = int(input("Siseta päeva number (1-7)"))
#if paev_number==1:
#    print("Esmaspäev")
#elif paev_number==2:
#    print("Teisipäev")
#elif paev_number==3:
#    print("Kolmapäev")
#elif paev_number==4:
#    print("Neljapäev")
#elif paev_number==5:
#    print("Reede")
#elif paev_number==6:
#    print("Laupäev")
#elif paev_number==7:
#    print("Pühapäev")
#else:
#    print("Vale number! Palun sisseta number vahemikus 1-7.")


#esimene ülesanne 
#nimi = input(print("Misugune sinu nimi on?"))
#if nimi == "JUKU":
#    print("Juku! lahme kino")
#    vana = int(input(print("Misugune sinu vanus?")))
#
#    if vana.isdigit():
#        vana = int(vana)
#        if vana <0 or vana>100:
#           print("Viga")
#        elif vana < 6:
#            print("Lastepilet")
#        elif vana <4:
#            print("laste pilet")
#        elif vana > 65:
#            print("sooduspilet")
#        else:
#            print("viga admetega")
#else:
#    print("Ma ei tea kes sa oled((()))")



#Teine ülesanne

#nimi1 = input("Sisseta nimi => ").capitalize()
#nimi2 = input("Sisseta nimi => ").capitalize()
#if nimi1.isalpha() and nimi2.isalpha():
#    if nimi1=="Yaroslav" and nimi2 =="Yarik" or nimi1=="Yarik" and nimi2=="Kirill":
#        print(f"{nimi1} ja {nimi2} on täna pinginaber")
#    else:
#        print(f"{nimi1} ja {nimi2} ei ole täna pinginaber")
#else:
#    print("Palun sissesta ainult täheb")




#ülesanne 3

#pikkus = int(input("Sisetage pikkus: "))
#laius = int(input("Sisetage laius: "))
#if pikkus>0 and laius>0:
#
#    pindala = pikkus * laius
#
#    print(f"Pindala suurus on {pindala}")
#    user = input("Kas soovite remondi teha?").capitalize()
#    if user.isalpha() and user == "Jah":
#        hind = float(input("Ruut meetri hind: "))
#        if hind>0:
#            remondi_hind = hind * pindala
#            print(f"Remondi summa on {remondi_hind}")
#            kes = input("Kes teeb remondi?").capitalize()
#            if kes.isalpha() and kes=="Ise":
#                print(f"Siis summa on {hind}")
#            else:
#                print(f"Siis summa on {hind}" + 300)
#        else:
#            print("Hind ei saa ola negativsed!")
#    else:
#        print("Head aega!")
#else:
#    print("Arvut peavad olea suurem kui 0")


#Ulesanne 4

#hind = input("Hind:")

#if hind.isdigit():
#    hind = float(hind)
#    if hind > 700:
#        hind *= 0.7
#        print(f"Soodus hind võrtub {hind}")
#else:
#    print("On vaja numbri sissetsda.")


#ülesanne 5

#temp = input("Mis temperatuur praegu on?")
#
#if temp.isdigit():
#    temp = float(temp)
#    if temp < 18:
#        print("Ilm on soe")
#    else:
#        print("Ilm ei ole soe")
#try:
#    t=float(input("Sisseta temperatur: "))
#    if t>18:
#        print("Soe")
#    else:
#        print("ei ole soe")
#except:
#    print("Palun kirjutate temperatuur!")


#üleasnne 6
#try:
#    pikk = float(input("Misugune sinu pikkus on?"))
#    if pikk < 160:
#        print("Sa oled lühike!")
#    elif pikk > 160 and pikk < 180:
#        print("Sa oled keskmine!")
#    elif pikk > 180:
#        print("Sa oled pikk!")
#except:
#    print("Palun rääkide misugune sinu pikkus on!")

#ülesanne 7

#try:
#    pikk = float(input("Misugune sinu pikkus on?"))
#    teata = input("Misugune sinu teata?")
#    if pikk < 160:
#        print(f"Sa oled lühike! ja sinu teate on {teata}")
#    elif pikk > 160 and pikk < 180:
#        print(f"Sa oled keskmine ja sinu teate on {teata}")
#    elif pikk > 180:
#        print(f"Sa oled pikk ja sinu teate on {teata}")
#except:
#    print("Palun rääkide misugune sinu pikkus on ja misugune sinu teata on!")


#ülesane 8
    
#import random


#print("Tere! Kas te saate osta midagi? Näitaks meil on:")
#piim = random.randint(1, 100)
#print(f"Piim on {piim} eurot")
#leiba = random.randint(1, 100)
#print(f"Leiba on {leiba} eurot")
#saja = random.randint(1, 100)
#print(f"Saja on {saja} eurot")
#kommid = random.randint(1, 100)
#print(f"Kommid on {kommid} eurot")
#print("Kirjuta 'jah' või 'ei'")
#user = input(" ")

#if user == "jah":
#    tahab1 = int(input("Kui palju piim te tahate?"))
#    kokku_tahab1 = tahab1 * piim
#    tahab2 = int(input("Kui palju saja te tahate?"))
#    kokku_tahab2 = tahab2 * leiba
#    tahab3 = int(input("Kui palju leiba te tahate?"))
#    kokku_tahab3 = tahab3 * saja
#    tahab4 = int(input("Kui palju kommid te tahate?"))
#   kokku_tahab4 = tahab4 * kommid
#   kokku = kokku_tahab1 + kokku_tahab2 + kokku_tahab3 + kokku_tahab4
#    print(f"See on {kokku} eurot")
#
#    
#else:
#    print("Hea taiga!")
