import collections
import time
while True:
    print("\nВвеедите диапазон чисел->")
    p = int(input("Введите число ОТ:"))
    a =int(input("Введите число ДО:"))
    list = str([*range(p, a + 1)])
    req = collections.Counter(list)
    print("Цифра 0 повторяется: ", req['0'])
    print("Цифра 1 повторяется: ", req['1'])
    print("Цифра 2 повторяется: ", req['2'])
    print("Цифра 3 повторяется: ", req['3'])
    print("Цифра 4 повторяется: ", req['4'])
    print("Цифра 5 повторяется: ", req['5'])
    print("Цифра 6 повторяется: ", req['6'])
    print("Цифра 7 повторяется: ", req['7'])
    print("Цифра 8 повторяется: ", req['8'])
    print("Цифра 9 повторяется: ", req['9'])
    time.sleep(2)



