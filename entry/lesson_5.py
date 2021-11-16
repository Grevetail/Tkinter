import tkinter as tk

def get_name():
    global NAME
    NAME = name.get()
    if NAME:
        name.delete(0, tk.END)
        btn_insert['state'] = tk.NORMAL
        btn_get['state'] = tk.DISABLED
        return(NAME)
    else:
        return('Empty entry')

#Разобраться
def backspace_name():
    name.delete(len(name.get()) - 1)
    btn_insert['state'] = tk.DISABLED
    btn_get['state'] = tk.NORMAL

def del_name():
    name.delete(0, tk.END)
    btn_get['state'] = tk.NORMAL

def submit():
    print(name.get())
    print(password.get())
    del_name()
    password.delete(0, tk.END)

NAME = ''

win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('Пятый урок')

tk.Label(win, text='Имя').grid(row=0, column=0, stick='we')
name = tk.Entry(win)
name.grid(row=0, column=1, stick='we')

tk.Label(win, text='Пароль').grid(row=1, column=0, stick='we')
password = tk.Entry(win, show='*')
password.grid(row=1, column=1, stick='we')

btn_get = tk.Button(win, text='Get', command=get_name)
btn_get.grid(row=2, column=0, stick='we')

btn_insert = tk.Button(win, text='Insert', command=lambda: name.insert(0, NAME), state=tk.DISABLED)
btn_insert.grid(row=3, column=0, stick='we')

tk.Button(win, text='Backspace', command=backspace_name).grid(row=2, column=1, stick='we')
tk.Button(win, text='Delete All', command=del_name).grid(row=3, column=1, stick='we')

tk.Button(win, text='Submit', command=submit).grid(row=4, column=0, stick='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()