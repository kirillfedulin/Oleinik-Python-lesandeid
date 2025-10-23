#1
#k=0 #loendur
#for i in range(15):
#    arv = float(input(f"Sissesta {i+1}. arv: "))
#    if int(arv)==arv:
#         print(f"{arv} on täisarv")
#         k+=1
#print(f"Täisarve oli kokku {k} tk")



#2
#A = int(input("Sisesta arv A: "))
#summa = 0
#for i in range(1,A+1):
#    summa += i
#    print(f"Summa on {summa}")



#3
#for i in range(8):
#    while True:
#        try:
#            arv = int(input("Sissesta arvu:"))
#            if arv < 0:
#                print("Sisseta palun ainult positiivne arvu")
#                break
#            else:
#                arv2 = arv * arv
#        except:
#            print(f"{arv2}")


#4
#try:
#    for i in range(10, 21):
#        ruut=i ** 2
#        print(f"Arvu {i} ruut on {ruut}")
#except:
#    print("Tekkis viga!")
    
#5
#N = int(input("Sisesta arv N: "))
#sum_neagtive = 0
#for _ in range(N):
#    num = float(input("Sisesta arv: "))
#    if num < 0:
#        sum_neagtive += num
#    else:
#        pass
#  
#print("Summ negativsed arved on:", sum_neagtive)



#6
#N = int(input("Sisesta arved: "))
#
#plussed = 0
#negativsed = 0
#null = 0
#
#for _ in range(N):
#    arv = float(input("Sisesta arv: "))
#    if arv > 0:
#        plussed += 1
#    elif arv < 0:
#        negativsed += 1
#    else:
#        null += 1
#
#print("Positiivsed arvud:", plussed)
#print("Negatiivsed arvud:", negativsed)
#print("Nullid:", null)    


#7
#try:
#    A = int(input("Sisesta arv A: "))
#    B = int(input("Sisesta arv B: "))
#    K = int(input("Sisesta arv K: "))
#
#    for i in range(A, B + 1):
#        if i % K == 0:
#         print(i)
#except:
#    print("Viga sisestuses!")


#8

