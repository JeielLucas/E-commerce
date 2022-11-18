from tkinter import *
import tkinter.font as tkFont
from paginaLogin import login, cadastro
from endereco import endereco, pagamento, pagamentoPix, boleto, finalizar
from modelo import modelo_moletom, modelo_caneca

qnt = 1
qnt_itens = 1
contador = 1

janela = Tk()
janela.title('CompuStore')
janela.geometry('1500x750+10+20')
janela.iconbitmap(default='Imagens/icon.ico')
janela.resizable(False, False)

qntVar = IntVar(janela, qnt)
qnt_itensVar = IntVar(janela, qnt_itens)
tamanho_roupaVar = StringVar(janela, 'M')

frame1 = Frame(janela, background='Black')
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
frame2 = Frame(janela, background='Black')
frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
frame3 = Frame(janela, background='Black')
frame3.place(relx=0, rely= 0.86, relwidth=1, relheight= 0.15)

fontSeparador = tkFont.Font(family='Arial', size=17)

#Frame1
img_logo = PhotoImage(file='Imagens/logo1.png')
carrinho = PhotoImage(file='Imagens/carrinho.png')
logo_sem_nome = PhotoImage(file='Imagens/logoImagem.png')
image = Label(frame1, image=img_logo, background='Black')
image.place(relx=0.05, rely= -0.5)
sacola = Label(frame1, image=carrinho, background='Black')
sacola.place(relx=0.87, rely=0.35)
initial_page = Button(frame1, image=logo_sem_nome, relief='flat', cursor='hand2', command=lambda: paginaInicial())
initial_page.place(relx=0.053, rely=0.17, relwidth=0.06, relheight=0.55)

Login = Button(frame1, text='Login', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: login(janela))
Login.place(relx=0.75, rely= 0.4, relwidth=0.04, relheight=0.2)
separar = Label(frame1, text='|', background='Black', foreground='White')
separar.place(relx=0.791, rely=0.38)
separar.configure(font=(fontSeparador))
Login.configure(font=('Arial', 15))
Cadastro = Button(frame1, text='Cadastro', background='Black', foreground='White', cursor='hand2', relief='flat', command=lambda: cadastro(janela))
Cadastro.configure(font=('Arial', 15))
Cadastro.place(relx= 0.8, rely= 0.4, relwidth=0.06, relheight=0.2)


#Frame2
def paginaInicial():
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_camisa(janela))
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_moletom(janela))
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', command= lambda: modelo_caneca(janela))
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


    camisa = Label(frame2, text='Camisas', background='Black', foreground='White')
    camisa.place(relx=0.1, rely=0.3)
    camisa.configure(font=(fontE))
    img_camisa = PhotoImage(file='Imagens/Camisa.png')
    img1_camisa = Label(frame2, image=img_camisa)
    img1_camisa.place(relx=0.1, rely=0.4)
    button1 = Button(frame2, text='>', background='Black', foreground='White', relief='flat', command=lambda: modelo_camisa(janela))
    button1.place(relx=0.22, rely=0.5)
    button1.configure(font=('italic', 30))

    moletom = Label(frame2, text='Moletons', background='Black', foreground='White')
    moletom.place(relx=0.45, rely=0.3)
    moletom.configure(font=(fontE))
    img_moletom = PhotoImage(file='Imagens/Moletom.png')
    img1_moletom = Label(frame2, image=img_moletom)
    img1_moletom.place(relx=0.45, rely=0.4)
    button3 = Button(frame2, text='>', background='Black', foreground='White', relief='flat', command=lambda: modelo_moletom(janela))
    button3.place(relx=0.57, rely=0.5)
    button3.configure(font=('italic', 30))

    Caneca = Label(frame2, text='Canecas', background='Black', foreground='White')
    Caneca.place(relx=0.8, rely=0.3)
    Caneca.configure(font=(fontE))
    img_caneca = PhotoImage(file='Imagens/Caneca.png')
    img1_caneca = Label(frame2, image=img_caneca)
    img1_caneca.place(relx=0.8, rely=0.4)
    button2 = Button(frame2, text='>', background='Black', foreground='White', relief='flat', command=lambda: modelo_caneca(janela))
    button2.place(relx=0.92, rely=0.5)
    button2.configure(font=('italic', 30))

#Frame3
direitosAutorais = Label(frame3, text='© 2022 CompuStore® | Todos direitos reservados', background='Black', foreground='White')
direitosAutorais.configure(font=('Arial', 16))
direitosAutorais.place(relx=0.325, rely=0.32, relwidth=0.35, relheight=0.2)

def aumentar():
    global qnt_itens
    qnt_itens += 1
    qnt_itensVar.set(qnt_itens)

def diminuir():
    global qnt_itens
    if qnt_itens <= 1:
        qnt_itensVar.set(1)
    else:
        qnt_itens -= 1
        qnt_itensVar.set(qnt_itens)

def aumentar_tamanho_roupa():
    global tamanho_roupaVar, contador
    if contador >= 3:
        contador = 3
    else:
        contador +=1
    if contador == 1:
        tamanho_roupaVar.set('M')
    elif contador == 2:
        tamanho_roupaVar.set('G')
    elif contador == 3:
        tamanho_roupaVar.set('GG')

def diminuir_tamanho_roupa():
    global tamanho_roupaVar, contador
    if contador <= 0:
        contador = 0
    else:
        contador -=1
    if contador == 0:
        tamanho_roupaVar.set('P')
    elif contador == 1:
        tamanho_roupaVar.set('M')
    elif contador == 2:
        tamanho_roupaVar.set('G')
    elif contador == 3:
        tamanho_roupaVar.set('GG')

def comprar_roupa(janela):
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
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', relief='flat', command= lambda: diminuir())
    diminuir_quantidade.place(relx=0.35, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', relief='flat', command= lambda: aumentar())
    aumentar_quantidade.place(relx=0.45, rely=0.6)
    qnt_itens = Label(frame2, textvariable=qnt_itensVar)
    qnt_itens.place(relx=0.4, rely=0.6)

    tamanho = Label(frame2, text='Tamanho', background='Black', foreground='White')
    tamanho.place(relx=0.8, rely=0.4)
    tamanho_roupa = Label(frame2, textvariable= tamanho_roupaVar)
    tamanho_roupa.place(relx=0.85, rely=0.5)
    aumentar_tamanho = Button(frame2, text='+', background='Black', foreground='White', relief='flat', command= lambda: aumentar_tamanho_roupa())
    aumentar_tamanho.place(relx=0.9, rely=0.5)
    diminuir_tamanho = Button(frame2, text='-', background='Black', foreground='White', relief='flat', command= lambda: diminuir_tamanho_roupa())
    diminuir_tamanho.place(relx=0.8, rely=0.5)

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

def comprar_caneca(janela):
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
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', command= lambda: diminuir())
    diminuir_quantidade.place(relx=0.75, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', command= lambda: aumentar())
    aumentar_quantidade.place(relx=0.85, rely=0.6)
    qnt_itens = Label(frame2, textvariable=qnt_itensVar, background='White', foreground='Black')
    qnt_itens.place(relx=0.8, rely=0.6)

    comprar = Button(text='Comprar', background='#FF34D8', foreground='White')
    comprar.place(relx=0.6, rely=0.75)
    comprar.configure(font=('Italic', 20))

def aumentar_itens():
    global qnt, qntVar
    if qnt >= 12:
        qntVar.set(12)
    else:
        qnt +=1
        qntVar.set(qnt)

def diminuir_itens():
    global qnt, qntVar
    if qnt <= 1:
        qntVar.set(1)
    else:
        qnt -=1
        qntVar.set(qnt)

def cartao(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

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

    separar3 = Label(frame2, text='')
    separar3.place(relx=0.15, rely=0.15, relheight=0.001, relwidth=0.7)

    titulo = Label(frame2, text='Pagamento', background='Black', foreground='White')
    titulo.place(relx=0.48, rely=0.17)

    pix = Label(frame2, text='Pix', background='Black', foreground='White')
    pix.place(relx=0.15, rely=0.3)
    pix_selecionar = Button(frame2, text='oi', background='Black', foreground='White', relief='flat')
    pix_selecionar.place(relx=0.1, rely=0.3)
    
    boleto = Label(frame2, text='Boleto', background='Black', foreground='White')
    boleto.place(relx=0.15, rely=0.4)
    boleto_selecionar = Button(frame2, text='oi', background='Black', foreground='White', relief='flat')
    boleto_selecionar.place(relx=0.1, rely=0.4)

    cartao = Label(frame2, text='Cartão Débito/Crédito', background='Black', foreground='White')
    cartao.place(relx=0.15, rely=0.5)
    cartao_selecionar = Button(frame2, text='oi', background='Black', foreground='White', relief='flat')
    cartao_selecionar.place(relx=0.1, rely=0.5)

    separar4 = Label(frame2, text='')
    separar4.place(relx=0.5, rely=0.25, relheight=0.65, relwidth=0.001)

    numero_cartao = Label(frame2, text='Número do cartão', background='Black', foreground='White')
    numero_cartao.place(relx=0.6, rely=0.3)
    numero_cartao_entrada = Entry()
    numero_cartao_entrada.place(relx=0.6, rely=0.44)

    nome = Label(frame2, text='Nome', background='Black', foreground='White')
    nome.place(relx=0.75, rely=0.3)
    nome_entrada = Entry()
    nome_entrada.place(relx=0.75, rely=0.44)

    vencimento = Label(frame2, text='Data de vencimento', background='Black', foreground='White')
    vencimento.place(relx=0.6, rely=0.45)
    vencimento_entrada = Entry()
    vencimento_entrada.place(relx=0.6, rely=0.53)
    
    codigo = Label(frame2, text='Código de segurança', background='Black', foreground='White')
    codigo.place(relx=0.75, rely=0.45)
    codigo_entrada = Entry()
    codigo_entrada.place(relx=0.75, rely=0.53)
    
    id = Label(frame2, text='ID', background='Black', foreground='White')
    id.place(relx=0.6, rely=0.57)
    id_entrada = Entry()
    id_entrada.place(relx=0.6, rely=0.6)

    documento = Label(frame2, text='Número do documento', background='Black', foreground='White')
    documento.place(relx=0.75, rely=0.57)
    documento_entrada = Entry()
    documento_entrada.place(relx=0.75, rely=0.6)

    parcelas = Label(frame2, text='Parcelas', background='Black', foreground='White')
    parcelas.place(relx=0.6, rely=0.68)
    parcelas_entrada = Label(frame2, textvariable=qntVar)
    parcelas_entrada.place(relx=0.63, rely=0.7, relwidth=0.02)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', relief='flat', command= lambda: diminuir_itens())
    diminuir_quantidade.place(relx=0.6, rely=0.75)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', relief='flat', command= lambda: aumentar_itens())
    aumentar_quantidade.place(relx=0.66, rely=0.75)

    termos_de_uso = Button(frame2, text='OIII', background='Black', foreground='White', relief='flat')
    termos_de_uso.place(relx=0.6, rely=0.83)
    termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
    termos.place(relx=0.62, rely=0.83)
    finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat')
    finalizar.place(relx=0.75, rely=0.9)

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
    camisa1 = Button(frame2, image= camiseta_modelo1, command= comprar_roupa(janela))
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

paginaInicial()

janela.mainloop()