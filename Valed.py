from math import * #import oli valesti tehtud
import math
print("Ruudu karakteristikud") 
a= float(input('Sisesta ruudu k�lje pikkus => ')) #a oli string, vaja oli int v�i float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu �mberm��t", round(S, 1)) #round ja sulg
di=a*math.sqrt(2) #puudus math.
print("Ruudu diagonaal", round(di,2))
print() 
print("Ristk�liku karakteristikud") #sulgud olid vales kohas
b= float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
c= float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
S=b*c
print("Ristk�liku pindala", S) #sulgud olid vales kohas
P=2*(b+c) #puudus *
print("Ristk�liku �mberm��t", P)
di=math.sqrt(b**2+c**2) #puudus math.
print("Ristk�liku diagonaal", round(di, 2)) #puudus sulg
print() 
print("Ringi karakteristikud")
r=input('Sisesta ringi raadiusi pikkus => ') #sulgud olid vales kohas #lisa sulg
d=2*r #puudus *
print(f"Ringi l�bim��t", round(di, 1)) #puudus round ja sulg
S=pi*r**2 #vale 
print("Ringi pindala", round(S, 1))
C=2*pi**r #puudus *24
print("Ringjoone pikkus", round(C, 2)) #puudus sulg





