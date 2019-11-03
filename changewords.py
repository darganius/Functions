def sent():
    sentence = "Найти в строке указанную подстроку и заменить ее на новую. Строку, ее подстроку для замены и новую подстроку вводит пользователь."
    a = input("Введите слово: ")
    b = input("Слово на которое хотите заменить: ")
    sentences = sentence.split(" ")
    print(sentences)
    for i in range(len(sentences)):
        if a in sentences:
            sentences.remove(a)
            c = sentences.append(b)
    print(sentences)
sent()