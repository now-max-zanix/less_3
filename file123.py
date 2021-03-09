import time
import math
while True:
    print("\nКакие вычисления будем проводить?")
    print("Простое число - 1 \nВычеслить НОД - 2 \nВычеслить НОК - 3")
    gg = (input("\nPlease,enter the number or exit:"))
    if gg == "1":
        f = True
        while f:
            p = int(input("\nВведите число(>2):"))
            if p > 1:
                for z in range(2, p):
                    if (p % z == 0):
                        print("Число составное\n")
                        time.sleep(2)
                        f = False
                        break         
                else:
                    print("Число простое\n")
                    time.sleep(2)
                    break 
            else:
                print("Число должно быть > 1 Ведите заново\n")
                time.sleep(2)
    elif gg == "2":
        a = int(input("\nВведите число a:"))
        a = abs(a)
        b = int(input("Введите число b:"))
        b = abs(b)

        while (a != 0 and b != 0):
            if a > b:
                a = a % b
            else: 
                b = b % a
        print("НОД =", a + b) 
        time.sleep(2)
    elif gg == "3":
        a = int(input("\nВведите число a:"))
        a = abs(a)
        b = int(input("Введите число b:"))
        b = abs(b)
        z = abs(a * b)

        while (a != 0 and b != 0):
            if a > b:
                a = a % b
            else: 
                b = b % a
        nod = a+b
        nok = z / nod
        print("NOK =", nok) 
        time.sleep(2)
    elif gg == "exit":
        break
    else:
        print("Ввели некоррктные значения")


        

        
    