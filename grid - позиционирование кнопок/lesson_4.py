import tkinter as tk

win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('Четвёртый урок')

'''
btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')
btn3 = tk.Button(win, text='Hello 3')
btn4 = tk.Button(win, text='Hello 4')
btn5 = tk.Button(win, text='Hello 5')

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=0, stick='we')
btn4.grid(row=2, column=0, columnspan=2, stick='we')
btn5.grid(row=0, column=2, rowspan=3, stick='ns')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)
'''

for i in range(5):
    for j in range(2):
        tk.Button(win, text=f'Hello {i}-{j}').grid(row=i, column=j)

win.mainloop()