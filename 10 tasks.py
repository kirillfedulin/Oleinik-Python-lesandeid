

#esimene ülesanne
#Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
#“Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

import random
import math



#print("Hello World!")
#name = str(input("What is ur name?"))
#print(f"Hello World! Hello {name.upper()}!")
#age = int(input("What is ur age?"))
#print(f"Hello World! Hello {name.upper()}!{name.upper()} are {age} years old!")




#Mis tüüpi on järgnevad muutujad:
#a) vanus = 18
#b) eesnimi = "Jaak"
#c) pikkus = 16.5
#d) kas_käib_koolis = True
#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
#Kirjuta kood tüüpide kontrollimiseks.


#vanus = int(input("Enter ut age: "))
#eesnimi = str(input("Enter ur name: "))
#pikkus = float(input("Enter ur tall"))
#kas_käib_koolis = bool(input("Do u go to school?"))




#Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on. 

#candy = random.randint(1, 100)
#print(f"We have {candy} candys")
# = int(input("How much candys u want?"))
#end = candy-want
#if end < 0:
#    print("We cant do this")
#else:
#    print(f"U get {end} candys")
#end




#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
#ask = int(input("The wood: "))
#Dia = ask // 3.14
#Pikk = Dia*3.14
#print(Pikk)





#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt
#N = float(input("Enter first num: "))
#M = float(input("Enter second num: "))
#D = math.sqrt(N*N + M*M)
#print(round(D, 2))


#Leidke järgnevast näiteprogrammist loogiline viga:
#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = teepikkus / aeg 
#print("Sinu kiirus oli " + str(kiirus) + " km/h")
#Ответ: Время делеться на растояние (ошибка)



#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
#Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.
#nums = list(map(float, input("Введите 5 чисел через пробел: ").split()))
#total = sum(nums)
#total2 = total / len(nums)
#print(total2)


#Joonista samasugune konn
#Head = "@..@"
#print('  ' + Head)
#Neck = '(----)'
#print(' ' + Neck)
#Body = '( \__/ )'
#print('' + Body)
#Legs = '^^ "" ^^  '
#print(Legs)


#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
#a = int(input("First num: "))
#b = int(input("Second num: "))
#c = int(input("End num: "))
#P = a + b + c
#print(P)



#Pitsa
#Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
#Jätate teenindajale 10% jootraha.
#Koosta programm, mis arvutab, kui palju igaüks peab maksma.

#ask = int(input("How much people: "))
#pizza = 12.90
#prots = pizza * 0.10
#end_price = pizza + prots
#half = end_price / ask
#print(f'U need to pay {half:.2f}')