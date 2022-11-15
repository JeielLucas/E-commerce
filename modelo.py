from tkinter import *
import tkinter.font as tkFont
qnt = 1
def aumentar_itens():
    global qnt
    qnt +=1
def diminuir_itens():
    global qnt
    qnt -=1

def modeloMoletom(janela):
    global qnt
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat')
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat')
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat')
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

    img_modelo = PhotoImage(file='Imagens/Modelo.png')
    img = Label(frame2, image=img_modelo)
    img.place(relx=0.1, rely=0.15)

    nome_modelo = Label(frame2, text='Nome do modelo', background='Black', foreground='White')
    nome_modelo.place(relx=0.4, rely=0.3)
    valor_modelo = Label(frame2, text='R$69,99', background='Black', foreground='White')
    valor_modelo.place(relx=0.4, rely=0.35)
    cor = Label(frame2, text='Cores', background='Black', foreground='White')
    cor.place(relx=0.4, rely=0.4)
    cor1 = Button(frame2, text='Preto', background='Black', foreground='White')
    cor1.place(relx=0.35, rely=0.45)
    cor2 = Button(frame2, text='Branco', background='Black', foreground='White')
    cor2.place(relx=0.4, rely=0.45)
    cor3 = Button(frame2, text='Cinza', background='Black', foreground='White')
    cor3.place(relx=0.45, rely=0.45)

    quantidade = Label(frame2, text='Quantidade', background='Black', foreground='White')
    quantidade.place(relx=0.4, rely=0.55)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', command= lambda: diminuir_itens())
    diminuir_quantidade.place(relx=0.35, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', command= lambda: aumentar_itens())
    aumentar_quantidade.place(relx=0.45, rely=0.6)
    qnt_itens = Label(frame2, text=qnt, background='White', foreground='Black')
    qnt_itens.place(relx=0.4, rely=0.6)

    tamanho = Label(frame2, text='Tamanho', background='Black', foreground='White')
    tamanho.place(relx=0.8, rely=0.4)
    tamanhoP = Button(frame2, text='P', background='Black', foreground='White', relief='flat')
    tamanhoP.place(relx=0.8, rely=0.5)
    tamanhoM = Button(frame2, text='M', background='Black', foreground='White', relief='flat')
    tamanhoM.place(relx=0.85, rely=0.5)
    tamanhoG = Button(frame2, text='G', background='Black', foreground='White', relief='flat')
    tamanhoG.place(relx=0.9, rely=0.5)
    tamanhoGG = Button(frame2, text='GG', background='Black', foreground='White', relief='flat')
    tamanhoGG.place(relx=0.95, rely=0.5)
    tamanhoP.configure(font=('Italic', 20))
    tamanhoM.configure(font=('Italic', 20))
    tamanhoG.configure(font=('Italic', 20))
    tamanhoGG.configure(font=('Italic', 20))

    frete = Label(text='Calcule o frete', background='Black', foreground='White', relief='flat')
    frete.place(relx=0.8, rely=0.65)
    frete_entrada = Entry()
    frete_entrada.insert(0, 'Digite o CEP')
    frete_entrada.place(relx=0.81, rely=0.7, relheight=0.05, relwidth= 0.15)
    frete_button = Button(text='Calcular', background='Black', foreground='White', relief='flat')
    frete_button.place(relx=0.8, rely=0.8)

    comprar = Button(text='Comprar', background='#FF34D8', foreground='White')
    comprar.place(relx=0.7, rely=0.75)
    comprar.configure(font=('Italic', 20))


def modeloCaneca(janela):
    global qnt
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat')
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat')
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat')
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

    img_modelo = PhotoImage(file='Imagens/Modelo.png')
    img = Label(frame2, image=img_modelo)
    img.place(relx=0.1, rely=0.15)

    nome_modelo = Label(frame2, text='Nome do modelo', background='Black', foreground='White')
    nome_modelo.place(relx=0.4, rely=0.3)
    valor_modelo = Label(frame2, text='R$69,99', background='Black', foreground='White')
    valor_modelo.place(relx=0.4, rely=0.35)

    frete = Label(text='Calcule o frete', background='Black', foreground='White', relief='flat')
    frete.place(relx=0.35, rely=0.55)
    frete_entrada = Entry()
    frete_entrada.insert(0, 'Digite o CEP')
    frete_entrada.place(relx=0.35, rely=0.6, relheight=0.05, relwidth= 0.15)
    frete_button = Button(text='Calcular', background='Black', foreground='White', relief='flat')
    frete_button.place(relx=0.35, rely=0.7)

    quantidade = Label(frame2, text='Quantidade', background='Black', foreground='White')
    quantidade.place(relx=0.75, rely=0.55)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', command= lambda: diminuir_itens())
    diminuir_quantidade.place(relx=0.75, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', command= lambda: aumentar_itens())
    aumentar_quantidade.place(relx=0.85, rely=0.6)
    qnt_itens = Label(frame2, text=qnt, background='White', foreground='Black')
    qnt_itens.place(relx=0.8, rely=0.6)

    comprar = Button(text='Comprar', background='#FF34D8', foreground='White')
    comprar.place(relx=0.6, rely=0.75)
    comprar.configure(font=('Italic', 20))