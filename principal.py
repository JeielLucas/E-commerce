from tkinter import *
import tkinter.font as tkFont
from paginaLogin import login2, cadastro1

janela = Tk()
janela.title('CompuStore')
janela.geometry('1500x750+10+20')
janela.iconbitmap(default='icon.ico')
janela.resizable(False, False)


frame1 = Frame(janela, background='Black')
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
frame2 = Frame(janela, background='Black')
frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
frame3 = Frame(janela, background='Black')
frame3.place(relx=0, rely= 0.86, relwidth=1, relheight= 0.15)





fontSeparador = tkFont.Font(family='Arial', size=17)


#Frame1
img_logo = PhotoImage(file='logo.png')
carrinho = PhotoImage(file='carrinho.png')
image = Label(frame1, image=img_logo, background='Black')
image.place(relx=0.05, rely= -0.5)
sacola = Label(frame1, image=carrinho, background='Black')
sacola.place(relx=0.87, rely=0.35)

login = Button(frame1, text='Login', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: login2(janela))
login.place(relx=0.75, rely= 0.4, relwidth=0.04, relheight=0.2)
separar = Label(frame1, text='|', background='Black', foreground='White')
separar.place(relx=0.791, rely=0.38)
separar.configure(font=(fontSeparador))
login.configure(font=('Arial', 15))
cadastro = Button(frame1, text='Cadastro', background='Black', foreground='White', cursor='hand2', relief='flat', command=lambda:[frame2.destroy(), cadastro1(janela)])
cadastro.configure(font=('Arial', 15))
cadastro.place(relx= 0.8, rely= 0.4, relwidth=0.06, relheight=0.2)

#Frame2
fontE = tkFont.Font(family="Arial", size=14, weight="bold")

camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat')
moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat')
canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat')
camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)
moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)
canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)
separar1 = Label(frame2, text='|', background='Black', foreground='White')
separar1.place(relx=0.437, rely=0.01)
separar1.configure(font=(fontSeparador))
separar2 = Label(frame2, text='|', background='Black', foreground='White')
separar2.place(relx=0.546, rely=0.01)
separar2.configure(font=(fontSeparador))
canecas.configure(font=(fontE))
camisas.configure(font=(fontE))
moletom.configure(font=(fontE))

#Frame3
direitosAutorais = Label(frame3, text='© 2022 CompuStore® | Todos direitos reservados', background='Black', foreground='White')
direitosAutorais.configure(font=('Arial', 16))
direitosAutorais.place(relx=0.325, rely=0.32, relwidth=0.35, relheight=0.2)



janela.mainloop()