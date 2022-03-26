from cmath import sqrt


print("Выберите номер программы ")
print("Готовые программы: 1, 2, 8, 9, 10, 12, 13 ")

task = int(input("Выбранная программа: "))
if task == 1:
    print("424+2*(-2)*424+2*(-2) = " + str(424+2*(-2)*424+2*(-2)))    
if task == 2:
    print("9**19 - int(float(9**19)) = " + str(9**19 - int(float(9**19))))    

elif task == 8:
    a = float(input())
    b = float(input())
    c = input()
    if b == 0 and c == '/' or c == 'mod' or c == 'div':
        print("Деление на 0!")
    elif с == '*':
        print(a * b)
    elif c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '/':
        print(a / b)
    elif c == 'div':
        print(a // b)
    elif c == 'mod':
        print(a % b)
    elif c == 'pow':
        print(a ** b)

elif task ==9:
    f = str(input("Введите форму комнаты: "))
    if f == 'прямоугольник':
        a = int(input())
        b = int(input())
        print (a * b)
    elif f == 'треугольник': 
        a = int(input())
        b = int(input())
        c = int(input())
        p = (a + b + c) / 2
        print ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    elif f == 'круг':
        r = int(input())
        print (3.14 * r **2)

elif task == 10:
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    c = int(input("Третье число: "))
    s = a + b + c
    print("Максимум: ", max(a,b,c))
    print("Минимум: ", min(a,b,c))
    print("Оставшееся число: ", s - max(a,b,c) - min(a,b,c))

elif task == 12:
    n = input("Введите строку из 6 цифр: ")
    s1 = int(n[0]) + int(n[1]) + int(n[2])
    s2 = int(n[3]) + int(n[4]) + int(n[5])
    if s1 == s2:
        print('Счастливый')
    else:
        print('Обычный')

elif task == 13:
    a = float(input("Введите первую сторону треугольника: "))
    b = float(input("Введите второую сторону треугольника: "))
    c = float(input("Введите третью сторону треугольника: "))
    p = (a+b+c)/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    print("Периметр треугольника: " + str(S))