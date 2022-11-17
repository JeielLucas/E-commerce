from tkinter import *
import tkinter.font as tkFont

def endereco(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat')
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat')
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat')
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

    separar3 = Label(frame2, text='')
    separar3.place(relx=0.15, rely=0.15, relheight=0.001, relwidth=0.7)
    
    titulo = Label(frame2, text='Endereço de entrega', background='Black', foreground='White')
    titulo.place(relx=0.46, rely=0.17)

    cep = Label(frame2, text='CEP', background='Black', foreground='White')
    cep.place(relx=0.15, rely=0.3)
    cep_entrada = Entry()
    cep_entrada.place(relx=0.15, rely=0.45)

    endereco = Label(frame2, text='Endereço', background='Black', foreground='White')
    endereco.place(relx=0.15, rely=0.55)
    endereco_entrada = Entry()
    endereco_entrada.place(relx=0.15, rely=0.6)

    numero = Label(frame2, text='Número', background='Black', foreground='White')
    numero.place(relx=0.25, rely=0.55)
    numero_entrada = Entry()
    numero_entrada.place(relx=0.25, rely=0.6)

    complemento = Label(frame2, text='Complemento', background='Black', foreground='White')
    complemento.place(relx=0.15, rely=0.8)
    complemento_entrada = Entry()
    complemento_entrada.place(relx=0.15, rely=0.77)

    separar = Label(frame2, text='')
    separar.place(relx=0.5, rely=0.25, relheight=0.65, relwidth=0.001)

    bairro = Label(frame2, text='Bairro', background='Black', foreground='White')
    bairro.place(relx=0.65, rely=0.3)
    bairro_entrada = Entry()
    bairro_entrada.place(relx=0.65, rely=0.45)
    
    cidade = Label(frame2, text='Cidade', background='Black', foreground='White')
    cidade.place(relx=0.65, rely=0.55)
    cidade_entrada = Entry()
    cidade_entrada.place(relx=0.65, rely=0.6)
    
    telefone = Label(frame2, text='Telefone', background='Black', foreground='White')
    telefone.place(relx=0.65, rely=0.8)
    telefone_entrada = Entry()
    telefone_entrada.place(relx=0.65, rely=0.77)
    
def pagamento(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat')
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat')
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat')
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

    pedido = Label(frame2, text='Resumo do pedido', background='Black', foreground='White')
    pedido.place(relx=0.7, rely=0.3)

    subtotal = Label(frame2, text='Sub-total', background='Black', foreground='White')
    subtotal.place(relx=0.7, rely= 0.4)
    subtotal_valor = Label(frame2, text='R$100,99', background='Black', foreground='White')
    subtotal_valor.place(relx=0.8, rely=0.4)

    frete = Label(frame2, text='Frete', background='Black', foreground='White')
    frete.place(relx=0.7, rely= 0.5)
    frete_valor = Label(frame2, text='R$10,00', background='Black', foreground='White')
    frete_valor.place(relx=0.8, rely=0.5)

    total = Label(frame2, text='Total', background='Black', foreground='White')
    total.place(relx=0.7, rely= 0.6)
    total_valor = Label(frame2, text='R$110,99', background='Black', foreground='White')
    total_valor.place(relx=0.8, rely=0.6)

def pagamentoPix(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat')
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat')
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat')
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

    
    img_pix = PhotoImage(file='Imagens/pixLogo.png')
    foto = Label(frame2, image=img_pix)
    foto.place(relx=0.55, rely=0.2)

    termos_de_uso = Button(frame2, text='OIII', background='Black', foreground='White', relief='flat')
    termos_de_uso.place(relx=0.6, rely=0.7)
    termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
    termos.place(relx=0.62, rely=0.7)
    finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat')
    finalizar.place(relx=0.75, rely=0.85)

def boleto(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat')
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat')
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat')
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

    nome = Label(frame2, text='Nome', background='Black', foreground='White')
    nome.place(relx=0, rely=0)
    nome_entrada = Entry()
    nome_entrada.place(relx=0.6, rely=0.44)

    sobrenome = Label(frame2, text='Sobrenome', background='Black', foreground='White')
    sobrenome.place(relx=0.75, rely=0.3)
    sobrenome_entrada = Entry()
    sobrenome_entrada.place(relx=0.75, rely=0.44)

    documento = Label(frame2, text='Número do documento', background='Black', foreground='White')
    documento.place(relx=0.6, rely=0.5)
    documento_entrada = Entry()
    documento_entrada.place(relx=0.6, rely=0.57)

    termos_de_uso = Button(frame2, text='OIII', background='Black', foreground='White', relief='flat')
    termos_de_uso.place(relx=0.6, rely=0.7)
    termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
    termos.place(relx=0.62, rely=0.7)
    finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat')
    finalizar.place(relx=0.75, rely=0.85)

def finalizar(janela):
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat')
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat')
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat')
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

    text = Label(frame2, text='COMPRA FINALIZADA', background='Black', foreground='#FFCFF6')
    text.place(relx=0.4, rely=0.4)

    agradecimento = Label(frame2, text=f'Obrigado por comprar com a\nCompuStore! :)', background='Black', foreground='White')
    agradecimento.place(relx=0.4, rely=0.6)
