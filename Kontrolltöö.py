
#esimene ülesanne
try:
    n = int(input("Sisestage puude arv (1–9): "))
    
    if 1 <= n <= 9:
        kuusk = [
            "   /V\\   ",
            "  / V \\  ",
            " / V V \\ ",
            "/VV V VV\\"
        ]
        
        for rida in kuusk:
            print((rida + " ") * n)
    else:
        print("Sa ei saa sisestada numbrit, mis on väiksem kui 1 ega suurem kui 9.")
except ValueError:
    print("Vaja on täisarvu")




#teine ülesanne
try:
    R = int(input("Sisesta number R:"))
    rez = 1 

    for i in range(1, R+1): 
        if i % 2 != 0:
            rez = rez * i 

    print(f"Kõigi paaritute arvude korrutis on: {rez}")
except Exception:
    print("viga")


#kolme ülesanne
try:
    num = input("Sisseta numbrid: ")
    positivsed = 0 
    for arv in num:
        try:
            value = int(arv)
            if value > 0: 
                positivsed += 1 
            else:
                print("Numbrid peavad olema positivsed!")
        except ValueError:
            print(f"Viga! {value} ei ole num!")

    print(f"Позтитвынх чисел {positivsed}")
except Exception:
    print("Viga!")



#nelja ülesanne 
try:
    arv = input("Sisseta numbrid: ")

    chet = 0
    ne_chet = 0

    for num in arv:
        num =int(num)
        if num % 2 == 0: 
            chet += 1
        else:
            ne_chet += 1

    print(f"paarisarvud: {chet}, veider {ne_chet}")
except Exception:
    print("Value!")


#viies ülesanne
try:
    A = int(input("Введите первое число: "))
    B = int(input("Введите второе число: "))

    summa = 0

    for i in range(A, B + 1): 
        summa += i 
    print(f"Сумма чисел от {A} до {B } равна {summa}")
except Exception:
    print("Value!")