from tkinter import *
import tkinter.font as tkFont

def modelo_camisa(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_camisa(janela))
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_caneca(janela))
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_moletom(janela))
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    separar1 = Label(frame2, text='|', background='Black', foreground='White')
    separar1.place(relx=0.437, rely=0.01)
    separar1.configure(font=(fontSeparador))
    separar2 = Label(frame2, text='|', background='Black', foreground='White')
    separar2.place(relx=0.546, rely=0.01)
    separar2.configure(font=(fontSeparador))

    canecas.configure(font=(fontE))
    camisas.configure(font=(fontE))
    moletom.configure(font=(fontE))

    camisa = Label(frame2, text='Camisas', background='Black', foreground='White')
    camisa.place(relx=0.2, rely=0.25)

    camiseta_modelo1 = PhotoImage(file='Imagens/Camisa.png')
    camisa1 = Button(frame2, image= camiseta_modelo1)
    camisa1.place(relx=0.05, rely=0.35)

    camiseta_modelo2 = PhotoImage(file='Imagens/Camisa.png')
    camisa2 = Button(frame2, image= camiseta_modelo2)
    camisa2.place(relx=0.25, rely=0.35)

    camiseta_modelo3 = PhotoImage(file='Imagens/Camisa.png')
    camisa3 = Button(frame2, image= camiseta_modelo3)
    camisa3.place(relx=0.45, rely=0.35)

    camiseta_modelo4 = PhotoImage(file='Imagens/Camisa.png')
    camisa4 = Button(frame2, image= camiseta_modelo4)
    camisa4.place(relx=0.65, rely=0.35)

    camiseta_modelo5 = PhotoImage(file='Imagens/Camisa.png')
    camisa5 = Button(frame2, image= camiseta_modelo5)
    camisa5.place(relx=0.85, rely=0.35)

def modelo_moletom(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_camisa(janela))
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_caneca(janela))
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_moletom(janela))
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    separar1 = Label(frame2, text='|', background='Black', foreground='White')
    separar1.place(relx=0.437, rely=0.01)
    separar1.configure(font=(fontSeparador))
    separar2 = Label(frame2, text='|', background='Black', foreground='White')
    separar2.place(relx=0.546, rely=0.01)
    separar2.configure(font=(fontSeparador))

    canecas.configure(font=(fontE))
    camisas.configure(font=(fontE))
    moletom.configure(font=(fontE))

    moletom = Label(frame2, text='Moletons', background='Black', foreground='White')
    moletom.place(relx=0.2, rely=0.25)

    camiseta_modelo1 = PhotoImage(file='Imagens/Moletom.png')
    moletom1 = Button(frame2, image= camiseta_modelo1)
    moletom1.place(relx=0.05, rely=0.35)

    camiseta_modelo2 = PhotoImage(file='Imagens/Moletom.png')
    moletom2 = Button(frame2, image= camiseta_modelo2)
    moletom2.place(relx=0.25, rely=0.35)

    camiseta_modelo3 = PhotoImage(file='Imagens/Moletom.png')
    moletom3 = Button(frame2, image= camiseta_modelo3)
    moletom3.place(relx=0.45, rely=0.35)

    camiseta_modelo4 = PhotoImage(file='Imagens/Moletom.png')
    moletom4 = Button(frame2, image= camiseta_modelo4)
    moletom4.place(relx=0.65, rely=0.35)

    camiseta_modelo5 = PhotoImage(file='Imagens/Moletom.png')
    moletom5 = Button(frame2, image= camiseta_modelo5)
    moletom5.place(relx=0.85, rely=0.35)

def modelo_caneca(janela):

    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_camisa(janela))
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_caneca(janela))
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_moletom(janela))
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    separar1 = Label(frame2, text='|', background='Black', foreground='White')
    separar1.place(relx=0.437, rely=0.01)
    separar1.configure(font=(fontSeparador))
    separar2 = Label(frame2, text='|', background='Black', foreground='White')
    separar2.place(relx=0.546, rely=0.01)
    separar2.configure(font=(fontSeparador))

    canecas.configure(font=(fontE))
    camisas.configure(font=(fontE))
    moletom.configure(font=(fontE))

    caneca = Label(frame2, text='Canecas', background='Black', foreground='White')
    caneca.place(relx=0.2, rely=0.25)

    camiseta_modelo1 = PhotoImage(file='Imagens/Caneca.png')
    caneca1 = Button(frame2, image= camiseta_modelo1)
    caneca1.place(relx=0.05, rely=0.35)

    camiseta_modelo2 = PhotoImage(file='Imagens/Caneca.png')
    caneca2 = Button(frame2, image= camiseta_modelo2)
    caneca2.place(relx=0.25, rely=0.35)

    camiseta_modelo3 = PhotoImage(file='Imagens/Caneca.png')
    caneca3 = Button(frame2, image= camiseta_modelo3)
    caneca3.place(relx=0.45, rely=0.35)

    camiseta_modelo4 = PhotoImage(file='Imagens/Caneca.png')
    caneca4 = Button(frame2, image= camiseta_modelo4)
    caneca4.place(relx=0.65, rely=0.35)

    camiseta_modelo5 = PhotoImage(file='Imagens/Caneca.png')
    caneca5 = Button(frame2, image= camiseta_modelo5)
    caneca5.place(relx=0.85, rely=0.35)
