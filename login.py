from tkinter import *
import tkinter.font as tkFont
from email2 import validateLogin
def login2(janela):
    fontLogin = tkFont.Font(family='Arial', size=22)

    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

    texto = Label(frame2, text='Faça o seu login!', background='Black', foreground='White')
    texto.place(relx=0.15, rely=0.08, relwidth=0.2, relheight=0.1)
    texto.configure(font=('Arial', 20))

    emailText = Label(frame2, text='Email:', background='Black', foreground='White')
    emailText.configure(font=(fontLogin))
    emailText.place(relx= 0.1, rely=0.2, relwidth=0.1, relheight=0.2)
    email = Entry()
    email.place(relx= 0.123, rely=0.43, relwidth=0.2, relheight=0.05)
    email.configure(font=(14))

    passText = Label(frame2, text='Senha:', background='Black', foreground='White')
    passText.configure(font=(fontLogin))
    passText.place(relx= 0.1, rely=0.48, relwidth=0.1, relheight=0.2)
    password = Entry(show='•')
    password.configure(font=(16))
    password.place(relx= 0.123, rely=0.62, relwidth=0.2, relheight=0.05)
    def oi():
        e = email.get()
        p = password.get()
        print(e,p)
        return e, p
    logina = Button(frame2, text='Login', background='Black', foreground='White', relief='flat', command=validateLogin(email, password))
    logina.place(relx= 0.2, rely=0.8, relwidth=0.05, relheight=0.08)
    logina.configure(font=('Arial', 20))

    separar = Label(frame2, text='')
    separar.place(relx=0.6, rely=0.1, relheight=0.8, relwidth=0.001)
    


    po = Label(frame2, text='Não tem uma conta?', background='Black', foreground='White')
    po.place(relx= 0.68, rely=0.1, relwidth=0.22, relheight=0.2)
    po.configure(font=('Arial', 26))
    op = Button(frame2, text='Cadastre-se aqui', background='Black', foreground='White', relief='flat')
    op.configure(font=('Arial', 26))
    op.place(relx= 0.7, rely=0.4, relwidth=0.18, relheight=0.15)