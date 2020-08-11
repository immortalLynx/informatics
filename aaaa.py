print("Здравствуйте!")
list = []
side = 0
'''for side in range(3):
    list.append(input(f"введите сторону с номером {side+1} \n"))'''
while side < 3:
    list.append(input(f"введите сторону с номером {side + 1} \n"))
    side += 1
print(type(list[0]))
if int(list[0])+int(list[1]) > int(list[2]) and int(list[1])+int(list[2]) > int(list[0]) and int(list[0])+int(list[2]) > int(list[1]):
    print("Треугольник существует!")
else:
    print("Не существует...")
