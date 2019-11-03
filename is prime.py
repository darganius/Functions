def is_prime(x):
    divisor=2
    while divisor<(x//2):
        if x%divisor == 0:
            return False
        divisor+=1
    return True
a = is_prime()
print(a)