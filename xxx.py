import math
import cmath
import time

while True:
    print("\nax^2 + bx + c = 0")
    print("Введите значения (а не равно 0):")
    
    while True:
        a = float(input("a = "))
        if a == 0:
            print("ERROR\n")
            continue
        else:
            b = float(input("b = "))
            c = float(input("c = "))
            break

    D = b ** 2 - 4 * a * c
    print("\nD = {:.2f}".format(D))

    if D > 0:
        x1 = (-b + math.sqrt(D)) / 2 * a 
        x2 = (-b - math.sqrt(D)) / 2 * a 
        print("X1 = {:.2f}".format(x1))
        print("X2 = {:.2f}".format(x2))
        time.sleep(2)
    elif D == 0:
        x = -b/(2*a)
        print("X = {:.2f}".format(x))
        time.sleep(2)
    else:
        x1 = (-b + cmath.sqrt(D)) / 2 * a 
        x2 = (-b - cmath.sqrt(D)) / 2 * a
        print("X1 = {:.2f}".format(x1))
        print("X2 = {:.2f}".format(x2))
        time.sleep(2)
