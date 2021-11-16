import tkinter as tk

def add_digit(d):
    print(d)

def back_char():
    pass

def result():
    pass

def plus():
    pass

def minus():
    pass

def multiplication():
    pass

def division():
    pass

win = tk.Tk()
win.geometry("230x266+100+200")
win['bg'] = '#7787b1'
win['padx'] = 15
win['pady'] = 15
win.resizable(0, 0)
win.title('Calculator')

calc = tk.Entry(win)
calc.grid(row=0, column=0, columnspan=4, stick='wens', padx=3, pady=3)

count = 1

for i in range(4):
    for j in range(3):
        if count < 10:
            tk.Button(win, text=f'{count}', bd=2).grid(row=i+1, column=j, stick='wens', padx=3, pady=3)
        elif count == 10:
            tk.Button(win, text='C', bd=2, command=back_char).grid(row=i + 1, column=0, stick='wens', padx=3, pady=3)
            tk.Button(win, text='0', bd=2, command=lambda: add_digit(0)).grid(row=i + 1, column=1, stick='wens', padx=3, pady=3)
            tk.Button(win, text='=', bd=2, command=result).grid(row=i + 1, column=2, stick='wens', padx=3, pady=3)
            count = 1
            break
        count += 1

tk.Button(win, text='+', bd=2, command=plus).grid(row=1, column=3, stick='wens', padx=3, pady=3)
tk.Button(win, text='-', bd=2, command=minus).grid(row=2, column=3, stick='wens', padx=3, pady=3)
tk.Button(win, text='/', bd=2, command=division).grid(row=3, column=3, stick='wens', padx=3, pady=3)
tk.Button(win, text='*', bd=2, command=multiplication).grid(row=4, column=3, stick='wens', padx=3, pady=3)

for i in range(4):
    win.grid_columnconfigure(i, minsize=50)
    if (i == 0):
        win.grid_rowconfigure(i, minsize=40)
    elif (i == 3):
        win.grid_rowconfigure(i, minsize=50)
        win.grid_rowconfigure(i+1, minsize=50)
    else:
        win.grid_rowconfigure(i, minsize=50)


for wid in win.winfo_children():
    wid.config(font=('Arial', 11))

win.mainloop()