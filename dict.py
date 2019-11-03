def func():
    retakelist = []
    userdata = {}
    while True:
        aty = input("Enter your name:")
        if aty == "ok":
            break
        ball = int(input("Enter your score:"))
        userdata[aty] = ball
    print(userdata)
    average = sum(userdata.values())/len(userdata)
    print("Average score is:{}".format(average))
    for i in range(len(userdata)):
        if list(userdata.items())[i][1]<average:
            print(list(userdata.items())[i][i])
func()