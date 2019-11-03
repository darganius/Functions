#Функция, которая добвляет имена студентов в список stu_list
def studentsl():
    stu_list = []
    students_list = []
    while True:
        studentslist = input("Введите имя студента, когда закончите введите 'ok': ")
        if studentslist == "ok":
            break
        else:
            stu_list.append(studentslist)
    return stu_list
#--------------------------------------------------------------
a = studentsl()
print(a)
#Функция, которая добавляет баллы к каждому студенту.
def stu_scores():
    score = []
    scores = []
    for each in a:
        score = int(input("Введите количество баллов набранные учеником {}:".format(each)))
        scores.append(score)
    return scores
#-------------------------------------------------------------
b = stu_scores()
print(a)
print(b)
#Функция, которая находит средний балл студентов и оставляет на пересдачу тех стуентов, которые набрали меньше среднего балла.
def retake():
    sum = 0
    retakelist = []
    allscores = 0
    students = {}
#Функция, которая находит средний балл.
    for j in b:
        sum+=1
        allscores +=j
    average = allscores/sum
#-------------------------------------
    for k in b:
        if k<average:
            n = b.index(k)
            print("Ученик под именем {} должен пересдать экзамен".format(a[n]))
    #for i in n:
     #   students[a[n]]=b[n]
    #print(students)
    return retakelist
retake()
