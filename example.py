from factsum import factorial
sum1 = 0
a = ""
total = 0
numlist = []
numbers = []
for i in range(10):
    numbers.append(str(i))
numbers.append('.')
print(numbers)
while True:
    x = input("Санды енгизиниз: ")
    if x == "ok":
        break
    for each in x:
        if each in numbers:
            sum1 += 1
    if int(len(x)) == sum1:
        if '.' in x:
            print("Its a float. plz enter int number")
            sum1=0
        else:
            numlist.append(int(x))
            sum1=0
    else:
        print("its a string. plz enter int number")
        sum1=0
total = (sum(numlist))
if total==0:
    total=''
else:
    print(total)
    c = factorial(total)
    print("Factorial of Total number is:{}".format(c))
    