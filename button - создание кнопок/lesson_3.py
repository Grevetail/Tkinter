import tkinter as tk
from colorutils import random_web

def say_hello():
    print('Hello')

def add_label():
    label = tk.Label(win, text='Hello')
    label.pack()

def counter():
    global count
    count += 1
    btn4['text'] = f'Счётчик: {count}'
    win.config(bg=random_web())
    if count%2 == 0:
        btn3['state'] = tk.DISABLED
        btn3['text'] = 'Не активна'
    else:
        btn3['state'] = tk.NORMAL
        btn3['text'] = 'Активна'

count = 0

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title("Третий урок")

btn1 = tk.Button(win, text='Hello in console',
                 command=say_hello
                 )

btn2 = tk.Button(win, text='Add Hello',
                 command=add_label
                 )

btn3 = tk.Button(win, text='Add new lambda',
                 command=lambda: tk.Label(win, text='new lambda').pack()
                 )

btn4 = tk.Button(win, text=f'Счётчик: {count}',
                 command=counter,
                 activebackground='grey',
                 bg='red',
                 fg='white',
                 state=tk.NORMAL
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

win.mainloop()