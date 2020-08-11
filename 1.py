print("Здравствуйте")
a = int(input("введите число а\n"))

b = int(input("введите число b\n"))

c = int(input("введите число c\n"))

primer = (a,"x2",b,"x",c)
print(primer)
disc = b*b - 4*a*c
print(disc)
x1 = 0
x2 = 0
korenIzDisc = int(disc**0.5)
znamenatel = 0
if disc > 0:
    print("ОГО, 2 корня!")
    x1 = int(korenIzDisc - b)
    znamenatel = 2*a
    x1 = x1/znamenatel
    x2 = (-1*korenIzDisc - b)
    x2 = x2/znamenatel
    print("x1 = ",x1)
    print("x2 = ",x2)
elif disc < 0:
    print("Не доложили корней")
    print("ИХ ПРОСТО НЕТ! :(((")
else:
    print("Только один корень!")
    x1 = x2 = (korenIzDisc - b)
    x1 = x2 = x1/znamenatel
    print("Единственный корень равен = ",x1)


