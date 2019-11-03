def bank():
    a = int(input("Введите сумму вашего вклада:"))
    years = int(input("На какой срок хотите внести ваши деньги:"))
    for i in range(years):
        sum = (a*0.1)*years+a
    print("За {} лет у вас накопится {}".format(years,sum))
bank()