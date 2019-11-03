import math
def square_func(a):
    area = a*a
    print("Площадь квадрата:{}".format(area))
    perim = a+a+a+a
    print("Периметр квадрата:{}".format(perim))
    diag = a*math.sqrt(2)
    print("Диагональ квадрата:{}".format(diag))
    return area, perim, diag
b = square_func(7)

    