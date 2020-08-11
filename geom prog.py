list = []
a = int(input("введите первый элемент\n"))
step = int(input("введите шаг прогрессии\n"))
list.append(a)
element = int(input("какой элемент вас интересует?\n"))
i = 0

while i <= element:
    a = a+step
    list.append(a + step)
    i +=1

print(list[element])
print(a)

