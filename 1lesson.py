print("Здравствуйте")
a = int(input("введите число а\n"))

b = int(input("введите число b\n"))

c = int(input("введите число c\n"))

primer = (a, "x2", b, "x", c)
print(primer)
disc = b*b - 4*a*c
print(disc)
x1 = 0
x2 = 0
if disc >= 0:
    korenIzDisc = disc**0.5
else:
    print("Дискриминант отрицательный")

if disc > 0:
    print("ОГО, 2 корня!")
    x1 = round((korenIzDisc - b)/2*a,2)
    x2 = round((-korenIzDisc - b)/2*a,2)
    print("x1 = ", x1)
    print("x2 = ", x2)
elif disc < 0:
    print("Не доложили корней")
    print("ИХ ПРОСТО НЕТ! :(((")
else:
    print("Только один корень!")
    x1 = (-b)/2*a
    print("Единственный корень равен = ", x1)


