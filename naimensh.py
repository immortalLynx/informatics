print("Yo! Вводите числа пока не устанете! Когда закончите наберите слово stop")
list = []
stopword = 0
i = 0
while stopword != 1:
    list.append(input("\n"))
    print("Вы ввели: ",list[i], "номер шага", i)
    if list[i] == "stop":
        stopword = 1
        list.remove("stop")
    else:
        i = i + 1
buf = int(list[0])

for a in range(i):
    if int(list[a])<buf:
        buf = int(list[a])

print(buf)
