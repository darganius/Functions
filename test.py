from factsum import factorial
def input_digit():
    list = []
    while True:
        a = input("Введите число, если закончили то введите OK: ")
        if a == "ok":
            break
        if isa('a'):
            print("try again")
        a = int(float(a))
        list.append(a)
        c = sum(list)
    b = factorial(c)
    print(b)
input_digit()