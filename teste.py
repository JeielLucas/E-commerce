from tkinter import *
import tkinter.font as tkFont


janela = Tk()
janela.title('CompuStore')
janela.geometry('1500x900')
janela.iconbitmap(default='icon.ico')
janela.resizable(True, True)
janela.minsize(400, 400)

bg = PhotoImage(file='pag.png')
oi = Label(image=bg)
oi.place(relx=0, rely=0, relwidth=1, relheight=1)

janela.mainloop()