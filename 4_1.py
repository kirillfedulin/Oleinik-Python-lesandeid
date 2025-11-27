#ülesanne 1

#import string
#t = ["a", "e", "i", "o", "u", "ü", "ä", "õ", "ö"]
#k = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "t"]
#m = string.punctuation + string.whitespace
#
#print("Porgram loenab mitu täishäälikut ja mitu kaashäälikut, kui sisestati lause – loeneb ka tühikud ja kirjavahemärgid ")
#words = input("Sisseta sinu sõnad: ").lower()
#t2 = 0
#k2 = 0
#m2 = 0
#for täht in words:
#    if täht in t:
#        t2+=1
#    elif täht in k:
#        k2 += 1
#    elif täht in m:
#        m2 += 1
#
#print(f"Sõnas/lausees on {t2} täishäälikut")
#print(f"{k2} kaashäälikut ja {m2} märki. ")


#ülesanne 2
#names = []

#for i in range(5):
#    ask = input("Sisseta palun 5 nime: ")
#    names.append(ask)

#print(names)
#vimane_nimi = names[-1]
#names.sort()
#print(names)
#print(vimane_nimi)

#replace = input("Kas sa tahad muuta nimi? ")
#if replace == "jah":
#    vana_nimi = input("Mis nimi muutame? ")
#    uus_nimi = input("Mis uus nimi? ")
#    find = names.index(vana_nimi)
#    names[find] = uus_nimi
#    print(names)
#else:
#    print(names)


#2.2
#nimed = ["kirill", "yarik", "nikita", "oleg"]
#ilma_korusteda = list(set(nimed))
#print(ilma_korusteda)

#2.3
#vanus = [22, 44, 66, 33, 99]
#suurim = max(vanus)
#kogusumma = min(vanus)
#keskmine = kogusumma / len(vanus)
#print(f"suurim on {suurim}, kogusuma on {kogusumma}, keskmine {keskmine}")


#ülesanne 3
#values = [15, 25, 60, 46, 34]

#for i in values:
#    print("*" * i)


#ülesanne 4
#city = ["Tallinn", "Narva", "Kohtla Järve", "Ida Viruuma", "Tartu", "Tartuma", "Viljandima", "Pärnuma", "Läänema"]
#while True:
#    try:
#        ask= int(input("Sisseta number: "))
#        if len(str(ask))==5:
#            break
#        else:
#            print("Peab olema 5 numbrid")
#    except:
#            print("Vigane!")
#ask_list = list(ask)
#n1=int(ask_list[0])
#print(f"Sinu postiinedksiga {ask} kuulud piirkonda {city[n1-1]}")
#if n1 in [0,1,2,7]:
#    print("Mine merre!")
#else:
#    print("Mine metsa!")

#ülesanne 5
#import random
#loend_arvud = []
#loend_tähed = []
#loend_kaashäälikud = []
#mitu=random.randint(2,20)
#for i in range(mitu):
#    elem = random.randint(0,100)
#    loend_arvud.append(elem)
#    elem=chr(random.randint(65, 90))
#    loend_tähed.append(elem)
#    elem=random.choice(k)
#    loend_kaashäälikud.append(elem)
#print(loend_arvud)
#print(loend_kaashäälikud)
#print(loend_tähed)



#ülesanne 6
#import random
#loend_arvud = []
#mitu=random.randint(2,20)
#for i in range(mitu):
#    elem = random.randint(0,100)
#    loend_arvud.append(elem)
#print("Alguses loend", loend_arvud)
#suurim=max(loend_arvud)
#kus_asub=loend_arvud.index(suurim)
#suurim_muudatud = suurim/mitu
#loend_arvud[kus_asub]=round(suurim_muudatud,2 )
#print("Muurmise järel:", loend_arvud)


#ülesanne 7
