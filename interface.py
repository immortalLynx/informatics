import tkinter
def calculate ():
    a = int(e1.get())
    b = int(e2.get())
    c = int(e3.get())
    lable4 = tkinter.Label(window,text = "y = " + str(a) +"x2 " + str(b) +"x " +str(c))
    lable4.place(x =100,y = 50)

    diskr = b*b - 4*a*c
    diskrvijet = tkinter.Label(window,text = "Дискриминант равен " + str(diskr), fg = "red")
    diskrvijet.place(x=100, y = 70)

    x1 = 0
    x2 = 0
    korenIzDisc = int(diskr ** 0.5)
    znamenatel = 0

    korneynet = tkinter.Label(window, text="корней нет")
    if diskr > 0:
        x1 = int(korenIzDisc - b)
        znamenatel = 2 * a
        x1 = x1 / znamenatel
        x2 = (-1 * korenIzDisc - b)
        x2 = x2 / znamenatel
        x1vijet = tkinter.Label(window, text="x1 = " + str(x1))
        x2vijet = tkinter.Label(window, text="x2 = " + str(x2))
        x1vijet.place(x=100,y=100)

        x2vijet.place(x=100,y=130)

    elif diskr < 0:
        korneynet.place(x=100,y=100)
    else:

        x1 = x2 = (korenIzDisc - b)
        x1 = x2 = x1 / znamenatel
        x1vijet = tkinter.Label(window, text="x1 = " + str(x1))
        x2vijet = tkinter.Label(window, text="x2 = " + str(x2))
        x1vijet.place(x=100, y=100)

window = tkinter.Tk()
window.geometry("300x200")
window.title("окно")

menu = tkinter.Menu(window)
window.config(menu = menu)
menu.add_command(label = "Поиск корней")
menu.add_command(label = "Игра")

lable1 = tkinter.Label(window,text= "коофициент a")
lable2 = tkinter.Label(window,text= "коофициент b")
lable3 = tkinter.Label(window,text= "коофициент c")
lable1.place(x=5,y=5)
lable2.place(x=5,y=20)
lable3.place(x=5,y=35)
e1 = tkinter.Entry(window)
e2 = tkinter.Entry(window)
e3 = tkinter.Entry(window)
e1.place(x=100,y=5)
e2.place(x=100,y=20)
e3.place(x=100,y=35)

b1 = tkinter.Button(window,text="посчитать", fg = "white", bg = "blue", command = calculate)
b1.place(x=230,y=15)

window.mainloop()

