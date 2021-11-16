import tkinter as tk

win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title('Второй урок')

label_1 = tk.Label(win, text='''Hello
my world''',
                   bg='grey',
                   fg='black',
                   font=('Arial',16,'bold'),
                   padx=20,
                   pady=20,
                   width=15,
                   height=10,
                   anchor='n',
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT)
label_1.pack()

win.mainloop()