l = []
for i in range (2000,3201):
    if i % 7 ==0 and i % 5 != 0:
        l.append(i)
print(l)
result = ''
sum = 0
for each in range(0, len(l)-1):
        sum+=1
        result = result + str(l[each]) + ','
print(result + str(l[-1]))