from tkinter import *
import tkinter.font as tkFont
from verificarLogin import validateLogin

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

    separar = Label(frame2, text='')
    separar.place(relx=0.6, rely=0.1, relheight=0.8, relwidth=0.001)
    
    login = Button(frame2, text='Login', background='Black', foreground='Red', relief='flat', command= lambda: validateLogin(email.get(), password.get()))
    login.place(relx= 0.2, rely=0.8, relwidth=0.05, relheight=0.08)
    login.configure(font=('Arial', 20))


    po = Label(frame2, text='Não tem uma conta?', background='Black', foreground='#30dcd0')
    po.place(relx= 0.68, rely=0.1, relwidth=0.22, relheight=0.2)
    po.configure(font=('Arial', 26))
    op = Button(frame2, text='Cadastre-se aqui', background='Black', foreground='White', relief='flat')
    op.configure(font=('Arial', 26))
    op.place(relx= 0.7, rely=0.4, relwidth=0.18, relheight=0.15)



def cadastro1(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    
    fonteDados = tkFont.Font(family='Arial', size=16)

    info = Label(frame2, text='Informações pessoais', background='Black', foreground='#30dcd0')
    info.place(relx=0.15, rely=0.08)
    info.configure(font=(fonteDados))

    infoLogin = Label(frame2, text='Informações de login', background='Black', foreground='#eb42a7')
    infoLogin.place(relx=0.7, rely=0.08)
    infoLogin.configure(font=(fonteDados))

    nomeCompleto = Entry()
    nomeCompleto.insert(0, 'Digite seu nome completo')
    nomeCompleto.configure(font=(fonteDados))
    nomeCompleto.place(relx=0.1, rely=0.35, relwidth=0.3)

    dataNascimento = Entry()
    dataNascimento.insert(0, 'Data de nascimento')
    dataNascimento.configure(font=(fonteDados))
    dataNascimento.place(relx=0.1, rely=0.5, relwidth=0.3)

    cpf = Entry()
    cpf.insert(0, 'Digite seu CPF')
    cpf.configure(font=(fonteDados))
    cpf.place(relx=0.1, rely=0.65, relwidth=0.3)
        
    email = Entry()
    email.insert(0, 'Digite seu email')
    email.configure(font=(fonteDados))
    email.place(relx=0.65, rely=0.35, relwidth=0.3)

    password = Entry()
    password.insert(0, 'Digite uma senha')
    password.configure(font=(fonteDados))
    password.place(relx=0.65, rely=0.5, relwidth=0.3)

    confPassword = Entry()
    confPassword.insert(0,'Confirme a sua senha')
    confPassword.configure(font=(fonteDados))
    confPassword.place(relx=0.65, rely=0.65, relwidth=0.3)

    cadastro = Button(text='Cadastrar', background='Black', foreground='White', relief='flat')
    cadastro.place(relx=0.75, rely=0.73)
    cadastro.configure(font=(16))

