kolvoelementov = int(input("введите кол-во чисел в прогрессии\n"))
list = []
a = int(input("какое первое число?\n"))
n = int(input("введите число n\n"))
list.append(a)
for i in range(int(kolvoelementov)-1):
    a = a+n
    list.append(a)
summ = 0
for i in range(int(kolvoelementov)):
    summ += int(list[i])

print(summ)

'''найти сумму геом прогрессии
    дан 1ый элемент + 2ой
    шага не дано
    кол-во элементов дано
    нужно восстановить всю прогрессию'''
