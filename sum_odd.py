def odd(n):
    sum = 0
    b = 0
    for i in range(n):
        if i%2==0:
            continue
        else:
            b = i**3
            sum +=b
    return sum
a = odd(50)
print(a)