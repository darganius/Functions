def sort_students(x = []):
    students1 = []
    for each in x:
        if len(each) < 5:
            students1.append(each)
            if len(students1)>4:
                break
    return students1
a = ["Michael","Bob","Tracy","Elun","Sam","Shakespear","Abay","Al-Farabi","Darkhan","Dean"]            
print(sort_students(a))