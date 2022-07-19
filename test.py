from tkinter import *

root = Tk()
root.config(bg='white')
root.geometry('800x600')
root.minsize(width=600, height=400)
root.title('Purgador')

root.columnconfigure(0, weight=10)
root.rowconfigure(0, weight=10)
root.columnconfigure(0, weight=50)
root.rowconfigure(1, weight=50)
root.columnconfigure(0, weight=3)
root.rowconfigure(2, weight=3)

frame1 = Frame(root, bg='gray26')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(root, bg='white')
frame2.grid(column=0, row=1, sticky='nsew')
frame3 = Frame(root, bg='gray20')
frame3.grid(column=0, row=2, sticky='nsew')


root.mainloop()