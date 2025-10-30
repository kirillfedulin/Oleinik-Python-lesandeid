
#esimene ülesanne
#n = int(input("Введите количество ёлок (1–9): "))
#if n > 0 and n < 10:    
#     kuusk = [
#     "   /V\\   ",
#     "  / V \\  ",
#     " / V V \\ ",
#     "/VV V VV\\"
#     ]
#
#     for rida in kuusk:
#         print((" " + rida) * n)
#else:
#    print("Нельзя вводить число меньше 1 или больше 9")




#teine ülesanne
#R = int(input("Введите число R: "))
#rez = 1 #обнулит
#
#for i in range(1, R+1): #от 1 до R
#    if i % 2 != 0: #не четное
#        rez = rez * i #умножаем
#
#print(f"Произведение всех нечетных чисел равно: {rez}")


#kolme ülesanne
#num = input("Введите числа через пробел:").split() #делит строку
#positivsed = 0 #счетчик положительных
#for arv in num:
#    if int(arv) > 0: #текст в число
#        positivsed += 1 #+1 если положительное
#    else:
#        print("Числа должны быть положительные!")
#
#print(f"Позтитвынх чисел {positivsed}")

#nelja ülesanne 
#arv = input("Введите число: ")
#
#chet = 0
#ne_chet = 0
#
#for num in arv:
#    num =int(num)
#    if num % 2 == 0: #четное или не четное
#        chet += 1
#    else:
#        ne_chet += 1
#
#print(f"Четных чисел: {chet}, нечетных {ne_chet}")


#viies ülesanne
#A = int(input("Введите первое число: "))
#B = int(input("Введите второе число: "))
#
#summa = 0
#
#for i in range(A, B + 1): #создает все числа от A до B
#    summa += i #добовляем каждое число
#print(f"Сумма чисел от {A} до {B } равна {summa}")