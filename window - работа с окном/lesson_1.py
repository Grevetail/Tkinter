import tkinter as tk

win = tk.Tk()
win.title('Первый урок')

photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)

win.config(bg='#acf0f2')

win.geometry('500x600+100+200')
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, True)


win.mainloop()