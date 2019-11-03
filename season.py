def season():
    print("Введите месяц:")
    a = int(input())
    if 1 <= a <=2 or a == 12:
        print("Это зима")
    elif 3 <= a <= 5:
        print("Это весна")
    elif 6 <= a <= 8:
        print("Это лето")
    elif 9 <= a <= 11:
        print("Это осень")
    else:
        print("Ошибка. Такого месяца нет!")
def matem(x,y):
    add = x+y
    multi = x*y
    div = x/y
    print("Addition {}, Multipliyng {}, Division {}".format(add,multi,div))