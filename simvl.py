import collections
while True:
    pr = str(input("\nВедите предложение(Для выхода(exit)): "))
    if pr == "exit":
        break
    req = collections.Counter(pr)
    print("Количество символов:\n", str(req))
