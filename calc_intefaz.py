import tkinter as tk

root = tk.Tk()
numero1 = tk.IntVar()
numero2 = tk.IntVar()
mensaje = tk.IntVar()


def suma():
    a = numero1.get()
    b = numero2.get()
    res = a + b
    mensaje.set(res)


def resta():
    a = numero1.get()
    b = numero2.get()
    res = a - b
    mensaje.set(res)


def multiplica():
    a = numero1.get()
    b = numero2.get()
    res = a * b
    mensaje.set(res)


def divide():
    a = numero1.get()
    b = numero2.get()
    if b == 0:
        mensaje.set('error!')
    else:
        res = a / b
        mensaje.set(res)


root.geometry('250x300')
root.title('Calculadora')
root.configure(bg="#3F51B5")
tk.Label(root, justify='center', text='CALCULADORA', bg="#303F9F", fg='#FFFFFF', width="22", font=('', 15)).place(x=0, y=0)
tk.Entry(root, justify='center', textvariable=numero1, width="5", fg='#303F9F', font=('', 25)).place(x=30, y=35)
tk.Entry(root, justify='center', textvariable=numero2, width="5", fg='#303F9F', font=('', 25)).place(x=130, y=35)
tk.Entry(root, justify='center', textvariable=mensaje, width="7", fg='#212121', font=('', 35)).place(x=30, y=200)
tk.Button(root, text=' +', bd=0, command=suma, bg="#009688", fg='#FFFFFF', font=('', 25)).place(x=10, y=100)
tk.Button(root, text=' - ', bd=0, command=resta, bg="#009688", fg='#FFFFFF', font=('', 25)).place(x=70, y=100)
tk.Button(root, text=' * ', bd=0, command=multiplica, bg="#009688", fg='#FFFFFF', font=('', 25)).place(x=130, y=100)
tk.Button(root, text=' / ', bd=0, command=divide, bg="#009688", fg='#FFFFFF', font=('', 25)).place(x=190, y=100)
root.mainloop()
