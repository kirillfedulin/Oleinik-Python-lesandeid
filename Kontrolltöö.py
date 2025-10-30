
#esimene ülesanne
#n = int(input("Введите количество ёлок (1–9): "))
#if n > 0 and n < 10:    
#    kuusk = [
#    "   /V\\   ",
#    "  / V \\  ",
#    " / V V \\ ",
#    "/VV V VV\\"
#    ]
#
#    for rida in kuusk:
#        print((" " + rida) * n)
#else:
#    print("Нельзя вводить число меньше 0 или больше 9")




#teine ülesanne
#R = int(input("Введите число R: "))
#
#rez = 1
#
#for i in range(1, R+1):
#    if i % 2 != 0:
#        rez = rez * i
#
#print(f"Произведение всех нечетных чисел равно: {rez}")


#kolme ülesanne
#num = input("Введите числа через пробел:").split()
#positivsed = 0
#for arv in num:
#    if int(arv) > 0:
#        positivsed += 1
#
#print(f"Позтитвынх чисел {positivsed}")

#nelja ülesanne 
#arv = input("Введите число: ")
#
#paaris = 0
#paaritud = 0
#
#for num in arv:
#    num =int(num)
#    if num % 2 == 0:
#        paaris += 1
#    else:
#        paaritud += 1
#
#print(f"Четных чисел: {paaris}, нечетных {paaritud}")


#viies ülesanne
#A = int(input("Введите первое число: "))
#B = int(input("Введите второе число: "))
#
#summa = 0
#
#for i in range(A, B + 1):
#    summa += i
#print(f"Сумма чисел от {A} до {B } равна {summa}")