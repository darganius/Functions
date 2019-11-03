sum1=0
numbers = ['.','0','1','2','3','4','5','6','7','8','9']
numlist=[]
numtuple = ()
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
            numtuple = list(numtuple)
            numtuple.append(int(x))
            numtuple = tuple(numtuple)
            sum1=0
    else:
        print("its a string. plz enter int number")
        sum1=0
print(numlist)
print(numtuple)