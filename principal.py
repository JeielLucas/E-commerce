from tkinter import *
import re
import tkinter.font as tkFont

#Váriaveis
qnt_parcelas = 1
qnt_itens = 1
contador = 1
valor_roupa = 20
valor_caneca = 10
carrinho_finalizar = {'Roupa': 0, 'Caneca': 0}
logado = False
total_finalizar = 0

#Janela
janela = Tk()
janela.title('CompuStore')
janela.geometry('1500x850+10+20')
janela.iconbitmap(default='Imagens/icon.ico')
janela.resizable(False, False)

#Váriaveis
qntVar = IntVar(janela, qnt_parcelas)
qnt_itensVar = IntVar(janela, qnt_itens)

#Erros Cadastro/Login
erro_login_texto = StringVar(janela, '')
erro_senha_cadastro = StringVar(janela, '')
erro_email_cadastro = StringVar(janela, '')
erro_cpf_cadastro = StringVar(janela, '')
erro_nome_cadastro = StringVar(janela, '')
erro_data_cadastro = StringVar(janela, '')

#Config Frame
frame1 = Frame(janela, background='Black')
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
frame2 = Frame(janela, background='Black')
frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
frame3 = Frame(janela, background='Black')
frame3.place(relx=0, rely= 0.86, relwidth=1, relheight= 0.15)

fontSeparador = tkFont.Font(family='Arial', size=17)


#Imagens dos modelos
img_modelo = PhotoImage(file='Imagens/Modelo.png')
camiseta_modelo1 = PhotoImage(file='Imagens/Modelos/Modelo_Camisas/camisa1_preto.png')
camiseta_modelo2 = PhotoImage(file='Imagens/Modelos/Modelo_Camisas/camisa2_preto.png')
camiseta_modelo3 = PhotoImage(file='Imagens/Modelos/Modelo_Camisas/camisa3_preto.png')
camiseta_modelo4 = PhotoImage(file='Imagens/Modelos/Modelo_Camisas/camisa4_preto.png')
camiseta_modelo5 = PhotoImage(file='Imagens/Modelos/Modelo_Camisas/camisa5_preto.png')

moletom_modelo1 = PhotoImage(file='Imagens/Modelos/Modelo_Moletom/moletom1.png')
moletom_modelo2 = PhotoImage(file='Imagens/Modelos/Modelo_Moletom/moletom2.png')
moletom_modelo3 = PhotoImage(file='Imagens/Modelos/Modelo_Moletom/moletom3.png')
moletom_modelo4 = PhotoImage(file='Imagens/Modelos/Modelo_Moletom/moletom4.png')
moletom_modelo5 = PhotoImage(file='Imagens/Modelos/Modelo_Moletom/moletom5.png')

caneca_modelo1 = PhotoImage(file='Imagens/Modelos/Modelo_Caneca/caneca1.png')
caneca_modelo2 = PhotoImage(file='Imagens/Modelos/Modelo_Caneca/caneca2.png')
caneca_modelo3 = PhotoImage(file='Imagens/Modelos/Modelo_Caneca/caneca3.png')
caneca_modelo4 = PhotoImage(file='Imagens/Modelos/Modelo_Caneca/caneca4.png')
caneca_modelo5 = PhotoImage(file='Imagens/Modelos/Modelo_Caneca/caneca5.png')

camisa_pagina_inicial = PhotoImage(file='Imagens/Modelos/Modelo_Pagina_Inicial/camisa_pagina_inicial.png')
moletom_pagina_inicial = PhotoImage(file='Imagens/Modelos/Modelo_Pagina_Inicial/moletom_pagina_inicial.png')
caneca_pagina_inicial = PhotoImage(file='Imagens/Modelos/Modelo_Pagina_Inicial/caneca_pagina_inicial.png')

imagem_tamanho_roupa = PhotoImage(file='Imagens/tamanho_M.png')

pix_logo = PhotoImage(file='Imagens/pixLogo.png')

botao_pagamento = PhotoImage(file='Imagens/botao.png')
botao_pagamento_selecionado = PhotoImage(file='Imagens/botao_selecionado.png')

botao1_pagamento = PhotoImage(file='Imagens/botao_pequeno.png')
botao1_pagamento_selecionado = PhotoImage(file='Imagens/botao_pequeno_selecionado.png')

finalizar = PhotoImage(file='Imagens/compra_finalizada.png')

a = PhotoImage(file='Imagens/botao_entrega.png')

ab = PhotoImage(file='Imagens/botao_pagamento.png')

abc = PhotoImage(file='Imagens/seta.png')

cor_branca = PhotoImage(file='Imagens/branco.png')

cor_preto = PhotoImage(file='Imagens/preto.png')

cor_cinza = PhotoImage(file='Imagens/cinza.png')

en = PhotoImage(file='Imagens/entrada.png')
ena = PhotoImage(file='Imagens/Entrega/entrada.png')

i = PhotoImage(file='Imagens/Pagamento/Boleto/boleto_nome.png')
i1 = PhotoImage(file='Imagens/Pagamento/Boleto/boleto_sobrenome.png')
i2 = PhotoImage(file='Imagens/Pagamento/Boleto/boleto_documento.png')

nome_titular_cartao = PhotoImage(file='Imagens/Pagamento/Cartao/nome_titular.png')
numero_cartao_credito = PhotoImage(file='Imagens/Pagamento/Cartao/numero_cartao.png')
vencimento_cvc = PhotoImage(file='Imagens/Pagamento/Cartao/vencimento_cartao.png')
cpf_cartao = PhotoImage(file='Imagens/Pagamento/Cartao/cpf_cartao.png')
parcelas_cartao = PhotoImage(file='Imagens/Pagamento/Cartao/parcelas_cartao.png')

log = PhotoImage(file='Imagens/logado.png')

#Frame1
img_logo = PhotoImage(file='Imagens/logo.png')
carrinho = PhotoImage(file='Imagens/carrinho.png')
logo_sem_nome = PhotoImage(file='Imagens/logoImagem.png')
image = Label(frame1, image=img_logo, background='Black')
image.place(relx=0.05, rely= -0.5)
sacola = Button(frame1, image=carrinho, background='Black', relief='flat', cursor='hand2', bd=0, activebackground='Black', activeforeground='White', command=lambda: pagamento())
sacola.place(relx=0.87, rely=0.35)
initial_page = Button(frame1, image=logo_sem_nome, relief='flat', cursor='hand2', bd=0, command=lambda: paginaInicial())
initial_page.place(relx=0.053, rely=0.1, relwidth=0.06, relheight=0.5)

Login = Button(frame1, text='Login', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: login())
Login.place(relx=0.75, rely= 0.4, relwidth=0.04, relheight=0.2)
separar = Label(frame1, text='|', background='Black', foreground='White')
separar.place(relx=0.791, rely=0.38)
separar.configure(font=(fontSeparador))
Login.configure(font=('Arial', 15))
Cadastro = Button(frame1, text='Cadastro', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: cadastro())
Cadastro.configure(font=('Arial', 15))
Cadastro.place(relx= 0.8, rely= 0.4, relwidth=0.06, relheight=0.2)


#Frame2
def paginaInicial():
    if logado == True:
        menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
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
    img1_camisa = Button(frame2, image=camisa_pagina_inicial, background='Black', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: modelo_camisa())
    img1_camisa.place(relx=0.07, rely=0.4)
    button1 = Button(frame2, image=abc, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', cursor='hand2', activeforeground='White', command=lambda: modelo_camisa())
    button1.place(relx=0.22, rely=0.47)
    button1.configure(font=('italic', 30))

    moletom = Label(frame2, text='Moletons', background='Black', foreground='White')
    moletom.place(relx=0.45, rely=0.3)
    moletom.configure(font=(fontE))
    img1_moletom = Button(frame2, image=moletom_pagina_inicial, background='Black', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: modelo_moletom())
    img1_moletom.place(relx=0.42, rely=0.34)
    button2 = Button(frame2, image=abc, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', cursor='hand2', activeforeground='White', command=lambda: modelo_moletom())
    button2.place(relx=0.57, rely=0.47)
    button2.configure(font=('italic', 30))

    Caneca = Label(frame2, text='Canecas', background='Black', foreground='White')
    Caneca.place(relx=0.8, rely=0.3)
    Caneca.configure(font=(fontE))
    img1_caneca = Button(frame2, image=caneca_pagina_inicial, background='Black', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: modelo_caneca())
    img1_caneca.place(relx=0.75, rely=0.35)
    button3 = Button(frame2, image=abc, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', cursor='hand2', activeforeground='White', command=lambda: modelo_caneca())
    button3.place(relx=0.92, rely=0.47)
    button3.configure(font=('italic', 30))

#Frame3
direitosAutorais = Label(frame3, text='© 2022 CompuStore® | Todos direitos reservados', background='Black', foreground='White')
direitosAutorais.configure(font=('Arial', 16))
direitosAutorais.place(relx=0.325, rely=0.32, relwidth=0.35, relheight=0.2)
pagamento_texto = Label(frame3, text= 'Formas de pagamento', background='Black', foreground='White')
pagamento_texto.place(relx=0.05, rely=0.05)
ig = PhotoImage(file='Imagens/formas_pagamento.png')
cartoes = Label(frame3, image=ig, background='Black')
cartoes.place(relx=0.05, rely=0.2)
contato = Label(frame3, text='Contato', background='Black', foreground='White')
contato.place(relx=0.8, rely=0.2)
contato_email = Label(frame3, text='contato@compustore.com.br', background='Black', foreground='White')
contato_email.place(relx=0.8, rely=0.4)

# Aumentar quantidades

def zerar_quantidade():
    global qnt_itens
    qnt_itens = 1
    qnt_itensVar.set(qnt_itens)

def adicionar_item_carrinho(item):
    global qnt_itens, total_finalizar, valor_roupa, valor_caneca
    carrinho_finalizar[item] += qnt_itens
    if item == 'Roupa':
        total_finalizar += carrinho_finalizar[item] * valor_roupa
    else: 
        total_finalizar += carrinho_finalizar[item] * valor_caneca
    carrinho_finalizar[item] = 0

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
    global contador
    if contador >= 3:
        contador = 3
    else:
        contador +=1
    if contador == 1:
        imagem_tamanho_roupa['file'] = 'Imagens/tamanho_M.png'
    elif contador == 2:
        imagem_tamanho_roupa['file'] = 'Imagens/tamanho_G.png'
    elif contador == 3:
        imagem_tamanho_roupa['file'] = 'Imagens/tamanho_GG.png'

def diminuir_tamanho_roupa():
    global contador
    if contador <= 0:
        contador = 0
    else:
        contador -=1
    if contador == 0:
        imagem_tamanho_roupa['file'] = 'Imagens/tamanho_P.png'
    elif contador == 1:
        imagem_tamanho_roupa['file'] = 'Imagens/tamanho_M.png'
    elif contador == 2:
        imagem_tamanho_roupa['file'] = 'Imagens/tamanho_G.png'

def aumentar_parcelas():
    global qnt_parcelas, qntVar
    if qnt_parcelas >= 12:
        qntVar.set(12)
    else:
        qnt_parcelas +=1
        qntVar.set(qnt_parcelas)

def diminuir_parcelas():
    global qnt_parcelas, qntVar
    if qnt_parcelas <= 1:
        qntVar.set(1)
    else:
        qnt_parcelas -=1
        qntVar.set(qnt_parcelas)

# Página 2
def trocar_cor_roupa(roupa, cor):
    if roupa == 'Camisa1':
        if cor == 'Preto':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa1_preto.png'
        if cor == 'Branco':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa1_branco.png'
        if cor == 'Cinza':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa1_cinza.png'
    elif roupa == 'Camisa2':
        if cor == 'Preto':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa2_preto.png'
        if cor == 'Branco':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa2_branco.png'
        if cor == 'Cinza':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa2_cinza.png'
    elif roupa == 'Camisa3':
        if cor == 'Preto':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa3_preto.png'
        if cor == 'Branco':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa3_branco.png'
        if cor == 'Cinza':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa3_cinza.png'
    elif roupa == 'Camisa4':
        if cor == 'Preto':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa4_preto.png'
        if cor == 'Branco':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa4_branco.png'
        if cor == 'Cinza':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa4_cinza.png'
    elif roupa == 'Camisa5':
        if cor == 'Preto':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa5_preto.png'
        if cor == 'Branco':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa5_branco.png'
        if cor == 'Cinza':
            img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa5_cinza.png'

def modelo_camisa():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White')
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
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

    camisa1 = Button(frame2, image=camiseta_modelo1, background='Black', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_camisa('Camisa1')])
    camisa1.place(relx=0.05, rely=0.35)

    camisa2 = Button(frame2, image=camiseta_modelo2, background='Black', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_camisa('Camisa2')])
    camisa2.place(relx=0.25, rely=0.35)

    camisa3 = Button(frame2, image= camiseta_modelo3, background='Black', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_camisa('Camisa3')])
    camisa3.place(relx=0.45, rely=0.35)

    camisa4 = Button(frame2, image= camiseta_modelo4, background='Black', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_camisa('Camisa4')])
    camisa4.place(relx=0.65, rely=0.35)

    camisa5 = Button(frame2, image= camiseta_modelo5, background='Black', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_camisa('Camisa5')])
    camisa5.place(relx=0.85, rely=0.35)

def modelo_moletom():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White')
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

    moletom1 = Button(frame2, image= moletom_modelo1, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_moletom('Moletom1')])
    moletom1.place(relx=0.03, rely=0.35)

    moletom2 = Button(frame2, image= moletom_modelo2, background='Black',bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_moletom('Moletom2')])
    moletom2.place(relx=0.23, rely=0.35)

    moletom3 = Button(frame2, image= moletom_modelo3, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_moletom('Moletom3')])
    moletom3.place(relx=0.43, rely=0.35)

    moletom4 = Button(frame2, image= moletom_modelo4, background='Black',bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_moletom('Moletom4')])
    moletom4.place(relx=0.63, rely=0.35)

    moletom5 = Button(frame2, image= moletom_modelo5,background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_moletom('Moletom5')])
    moletom5.place(relx=0.83, rely=0.35)

def modelo_caneca():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White')
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
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

    caneca1 = Button(frame2, image= caneca_modelo1, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca1')])
    caneca1.place(relx=0.05, rely=0.35)
    #0.05 0.35
    caneca2 = Button(frame2, image= caneca_modelo2, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca2')])
    caneca2.place(relx=0.25, rely=0.35)
    #0.25 0.35
    caneca3 = Button(frame2, image= caneca_modelo3, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca3')])
    caneca3.place(relx=0.45, rely=0.35)
    #0.45 0.35
    caneca4 = Button(frame2, image= caneca_modelo4, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca4')])
    caneca4.place(relx=0.65, rely=0.35)
    #0.65 0.35
    caneca5 = Button(frame2, image= caneca_modelo5, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca5')])
    caneca5.place(relx=0.85, rely=0.35)

# Página 3

def comprar_camisa(modelo):
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: modelo_caneca())
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: modelo_moletom())
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

    
    img = Label(frame2, image=img_modelo, background='Black')
    img.place(relx=0.15, rely=0.3)
    if modelo == 'Camisa1':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa1_preto.png'
    elif modelo == 'Camisa2':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa2_preto.png'
    elif modelo == 'Camisa3':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa3_preto.png'
    elif modelo == 'Camisa4':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa4_preto.png'
    elif modelo == 'Camisa5':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa5_preto.png'

    nome_modelo = Label(frame2, text='Nome do modelo', background='Black', foreground='White')
    nome_modelo.place(relx=0.4, rely=0.3)
    valor_modelo = Label(frame2, text='R$69,99', background='Black', foreground='White')
    valor_modelo.place(relx=0.4, rely=0.35)
    cor = Label(frame2, text='Cores', background='Black', foreground='White')
    cor.place(relx=0.4, rely=0.4)
    cor1 = Button(frame2, image=cor_preto, background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: trocar_cor_roupa(modelo, 'Preto'))
    cor1.place(relx=0.35, rely=0.45)
    cor2 = Button(frame2, image=cor_branca, background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: trocar_cor_roupa(modelo, 'Branco'))
    cor2.place(relx=0.4, rely=0.45)
    cor3 = Button(frame2, image=cor_cinza, background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: trocar_cor_roupa(modelo, 'Cinza'))
    cor3.place(relx=0.45, rely=0.45)

    quantidade = Label(frame2, text='Quantidade', background='Black', foreground='White')
    quantidade.place(relx=0.4, rely=0.55)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: diminuir())
    diminuir_quantidade.place(relx=0.35, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: aumentar())
    aumentar_quantidade.place(relx=0.45, rely=0.6)
    qnt_itens = Label(frame2, textvariable=qnt_itensVar)
    qnt_itens.place(relx=0.4, rely=0.6)

    tamanho = Label(frame2, text='Tamanho', background='Black', foreground='White')
    tamanho.place(relx=0.8, rely=0.4)
    tamanho_roupa = Label(frame2, image=imagem_tamanho_roupa, background='Black')
    tamanho_roupa.place(relx=0.83, rely=0.47)
    aumentar_tamanho = Button(frame2, text='+', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: aumentar_tamanho_roupa())
    aumentar_tamanho.place(relx=0.9, rely=0.5)
    diminuir_tamanho = Button(frame2, text='-', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: diminuir_tamanho_roupa())
    diminuir_tamanho.place(relx=0.8, rely=0.5)

    frete = Label(text='Calcule o frete', background='Black', foreground='White', relief='flat')
    frete.place(relx=0.8, rely=0.65)
    frete_entrada = Entry()
    frete_entrada.insert(0, 'Digite o CEP')
    frete_entrada.place(relx=0.81, rely=0.7, relheight=0.05, relwidth= 0.15)
    frete_button = Button(text='Calcular', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',)
    frete_button.place(relx=0.8, rely=0.8)

    comprar = Button(text='Comprar', background='#FF34D8', foreground='White', bd=0, activebackground='#FF34D8', activeforeground='White', command= lambda: [adicionar_item_carrinho('Roupa'), endereco()])
    comprar.place(relx=0.7, rely=0.75)
    comprar.configure(font=('Italic', 20))

def comprar_moletom(modelo):
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: modelo_caneca())
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: modelo_moletom())
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

    
    img = Label(frame2, image=img_modelo, background='Black')
    img.place(relx=0.15, rely=0.3)
    if modelo == 'Moletom1':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom1.png'
    elif modelo == 'Moletom2':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom2.png'
    elif modelo == 'Moletom3':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom3.png'
    elif modelo == 'Moletom4':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom4.png'
    elif modelo == 'Moletom5':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom5.png'

    nome_modelo = Label(frame2, text='Nome do modelo', background='Black', foreground='White')
    nome_modelo.place(relx=0.4, rely=0.3)
    valor_modelo = Label(frame2, text='R$69,99', background='Black', foreground='White')
    valor_modelo.place(relx=0.4, rely=0.35)

    quantidade = Label(frame2, text='Quantidade', background='Black', foreground='White')
    quantidade.place(relx=0.4, rely=0.55)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: diminuir())
    diminuir_quantidade.place(relx=0.35, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: aumentar())
    aumentar_quantidade.place(relx=0.45, rely=0.6)
    qnt_itens = Label(frame2, textvariable=qnt_itensVar)
    qnt_itens.place(relx=0.4, rely=0.6)

    tamanho = Label(frame2, text='Tamanho', background='Black', foreground='White')
    tamanho.place(relx=0.8, rely=0.4)
    tamanho_roupa = Label(frame2, image=imagem_tamanho_roupa, background='Black')
    tamanho_roupa.place(relx=0.83, rely=0.47)
    aumentar_tamanho = Button(frame2, text='+', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: aumentar_tamanho_roupa())
    aumentar_tamanho.place(relx=0.9, rely=0.5)
    diminuir_tamanho = Button(frame2, text='-', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: diminuir_tamanho_roupa())
    diminuir_tamanho.place(relx=0.8, rely=0.5)

    frete = Label(text='Calcule o frete', background='Black', foreground='White', relief='flat')
    frete.place(relx=0.8, rely=0.65)
    frete_entrada = Entry()
    frete_entrada.insert(0, 'Digite o CEP')
    frete_entrada.place(relx=0.81, rely=0.7, relheight=0.05, relwidth= 0.15)
    frete_button = Button(text='Calcular', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',)
    frete_button.place(relx=0.8, rely=0.8)

    comprar = Button(text='Comprar', background='#FF34D8', foreground='White', bd=0, activebackground='#FF34D8', activeforeground='White', command= lambda: [adicionar_item_carrinho('Roupa'), endereco()])
    comprar.place(relx=0.7, rely=0.75)
    comprar.configure(font=('Italic', 20))

def comprar_caneca(modelo):
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=17)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
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

    img = Label(frame2, image=img_modelo, background='black')
    img.place(relx=0.1, rely=0.15)
    if modelo == 'Caneca1':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca1.png'
    elif modelo == 'Caneca2':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca2.png'
    elif modelo == 'Caneca3':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca3.png'
    elif modelo == 'Caneca4':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca4.png'
    elif modelo == 'Caneca5':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca5.png'


    nome_modelo = Label(frame2, text='Nome do modelo', background='Black', foreground='White')
    nome_modelo.place(relx=0.4, rely=0.3)
    valor_modelo = Label(frame2, text='R$69,99', background='Black', foreground='White')
    valor_modelo.place(relx=0.4, rely=0.35)

    frete = Label(text='Calcule o frete', background='Black', foreground='White', relief='flat')
    frete.place(relx=0.35, rely=0.55)
    frete_entrada = Entry()
    frete_entrada.insert(0, 'Digite o CEP')
    frete_entrada.place(relx=0.35, rely=0.6, relheight=0.05, relwidth= 0.15)
    frete_button = Button(text='Calcular', background='Black', foreground='White', relief='flat', command= lambda: deslogar())
    frete_button.place(relx=0.35, rely=0.7)

    quantidade = Label(frame2, text='Quantidade', background='Black', foreground='White')
    quantidade.place(relx=0.75, rely=0.55)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: diminuir())
    diminuir_quantidade.place(relx=0.75, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: aumentar())
    aumentar_quantidade.place(relx=0.85, rely=0.6)
    qnt_itens = Label(frame2, textvariable=qnt_itensVar, background='White', foreground='Black')
    qnt_itens.place(relx=0.8, rely=0.6)

    comprar = Button(text='Comprar', background='#FF34D8', foreground='White', bd=0, activebackground='#FF34D8', activeforeground='White', command= lambda: [adicionar_item_carrinho('Caneca'), pagamento()])
    comprar.place(relx=0.6, rely=0.75)
    comprar.configure(font=('Italic', 20))

# Login e cadastro

def login():
    global erro_login_texto
    fontLogin = tkFont.Font(family='Arial', size=22)

    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

    texto = Label(frame2, text='Faça o seu login!', background='Black', foreground='White')
    texto.place(relx=0.15, rely=0.08, relwidth=0.2, relheight=0.1)
    texto.configure(font=('Arial', 20))

    emailText = Label(frame2, text='Email:', background='Black', foreground='White')
    emailText.configure(font=(fontLogin))
    emailText.place(relx= 0.1, rely=0.2, relwidth=0.1, relheight=0.2)
    ee = Label(frame2, image=en, background='Black')
    ee.place(relx=0.123, rely=0.35)
    email = Entry()
    email.place(relx= 0.14, rely=0.445, relwidth=0.235, relheight=0.04)
    email.configure(font=(14))

    passText = Label(frame2, text='Senha:', background='Black', foreground='White')
    passText.configure(font=(fontLogin))
    passText.place(relx= 0.1, rely=0.48, relwidth=0.1, relheight=0.2)
    aa = Label(frame2, image=en, background='Black')
    aa.place(relx=0.123, rely=0.62)
    password = Entry(show='*')
    password.place(relx= 0.14, rely=0.62, relwidth=0.235, relheight=0.04)
    password.configure(font=(16))
    erro_login = Label(frame2, textvariable=erro_login_texto, background='Black', foreground='White')
    erro_login.place(relx=0.18, rely=0.73)
    erro_login.configure(font=(30))

    separar = Label(frame2, text='')
    separar.place(relx=0.6, rely=0.1, relheight=0.8, relwidth=0.001)
    
    login = Button(frame2, text='Login', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: isLoged(email.get(), password.get()))
    login.place(relx= 0.2, rely=0.8, relwidth=0.05, relheight=0.08)
    login.configure(font=('Arial', 20))


    po = Label(frame2, text='Não tem uma conta?', background='Black', foreground='#2CFFF8')
    po.place(relx= 0.68, rely=0.1, relwidth=0.22, relheight=0.2)
    po.configure(font=('Arial', 26))
    op = Button(frame2, text='Cadastre-se aqui', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',)
    op.configure(font=('Arial', 26))
    op.place(relx= 0.7, rely=0.4, relwidth=0.18, relheight=0.15)

def cadastro():
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    
    fonteDados = tkFont.Font(family='Arial', size=16)

    info = Label(frame2, text='Informações pessoais', background='Black', foreground='#2CFFF8')
    info.place(relx=0.15, rely=0.08)
    info.configure(font=(fonteDados))

    infoLogin = Label(frame2, text='Informações de login', background='Black', foreground='#FF34D8')
    infoLogin.place(relx=0.7, rely=0.08)
    infoLogin.configure(font=(fonteDados))

    nome_completo_texto = Label(frame2, text='Nome completo:', background='Black', foreground='White')
    nome_completo_texto.place(relx=0.1, rely=0.15)
    nome_completo = Entry()
    nome_completo.configure(font=(fonteDados))
    nome_completo.place(relx=0.1, rely=0.35, relwidth=0.3)
    lg = Label(frame2, image=ena, background='Black')
    lg.place(relx=0.08, rely=0.19)
    validate_nome = Label(frame2, textvariable=erro_nome_cadastro, background='Black', foreground='White')
    validate_nome.place(relx=0.1, rely=0.32)

    data_nascimento_texto = Label(frame2, text='Data de nascimento:', background='Black', foreground='White')
    data_nascimento_texto.place(relx=0.1, rely=0.37)
    data_nascimento = Entry()
    data_nascimento.configure(font=(fonteDados))
    data_nascimento.place(relx=0.1, rely=0.5, relwidth=0.3)
    lga = Label(frame2, image=ena, background='Black')
    lga.place(relx=0.08, rely=0.42)
    validate_data = Label(frame2, textvariable=erro_data_cadastro, background='Black', foreground='White')
    validate_data.place(relx=0.1, rely=0.55)

    cpf_texto = Label(frame2, text='Digite seu cpf:', background='Black', foreground='White')
    cpf_texto.place(relx=0.1, rely=0.6)
    cpf = Entry()
    cpf.configure(font=(fonteDados))
    cpf.place(relx=0.1, rely=0.65, relwidth=0.3)
    lgb = Label(frame2, image=ena, background='Black')
    lgb.place(relx=0.08, rely=0.65)
    validate_cpf = Label(frame2, textvariable=erro_cpf_cadastro, background='Black', foreground='White')
    validate_cpf.place(relx=0.1, rely=0.8)

    email_texto = Label(frame2, text='Digite seu email:', background='Black', foreground='White')
    email_texto.place(relx=0.65, rely=0.15)
    email = Entry()
    email.configure(font=(fonteDados))
    email.place(relx=0.65, rely=0.35, relwidth=0.3)
    lgaa = Label(frame2, image=ena, background='Black')
    lgaa.place(relx=0.63, rely=0.19)
    validate_email = Label(frame2, textvariable=erro_email_cadastro, background='Black', foreground='White')
    validate_email.place(relx=0.65, rely=0.32)

    senha_texto = Label(frame2, text='Digite sua senha:', background='Black', foreground='White')
    senha_texto.place(relx=0.65, rely=0.37)
    password = Entry()
    password.configure(font=(fonteDados))
    password.place(relx=0.65, rely=0.5, relwidth=0.3)
    lgab = Label(frame2, image=ena, background='Black')
    lgab.place(relx=0.63, rely=0.42)
    validate_senha = Label(frame2, textvariable=erro_senha_cadastro, background='Black', foreground='White')
    validate_senha.place(relx=0.65, rely=0.55)
    
    confirmar_senha_texto = Label(frame2, text='Digite sua senha novamente:', background='Black', foreground='White')
    confirmar_senha_texto.place(relx=0.65, rely=0.6)
    confPassword = Entry()
    confPassword.configure(font=(fonteDados))
    confPassword.place(relx=0.65, rely=0.65, relwidth=0.3)
    lgabc = Label(frame2, image=ena, background='Black')
    lgabc.place(relx=0.63, rely=0.65)
    conf_senha = Label(frame2, textvariable=erro_senha_cadastro, background='Black', foreground='White')
    conf_senha.place(relx=0.65, rely=0.8)

    cadastro = Button(text='Cadastrar', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: dados(password.get(), confPassword.get(), email.get(), cpf.get(), nome_completo.get(), data_nascimento.get()))
    cadastro.place(relx=0.75, rely=0.73)
    cadastro.configure(font=(16))

def isLoged(email, password):
    global logado, erro_login_texto
    dicionario = {'e-mail': email, 'senha': password}
    linha = 0
    arq = open('email.txt', 'r')
    for i in arq:
        linha +=1
        i = i.replace(f'\n', '')
        if i == dicionario['e-mail']:
            senhas = open('password.txt', 'r')
            lerSenha = senhas.readlines()
            lerSenha = lerSenha[linha-1].replace(f'\n', '')
            if lerSenha == dicionario['senha']:
                logado = True
            senhas.close()
        break
    arq.close()

    if logado == True:
        erro_login_texto.set('')
        paginaInicial()
        menu_logado
    else:
        erro_login_texto.set('Email e/ou senha incorreto(s)')

def deslogar():
    global logado
    logado = False
    menu_logado()

def menu_logado():
    if logado == True:
        frame1 = Frame(janela, background='Black')
        frame1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        image = Label(frame1, image=img_logo, background='Black')
        image.place(relx=0.05, rely= -0.5)
        sacola = Button(frame1, image=carrinho, background='Black', relief='flat', cursor='hand2', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento())
        sacola.place(relx=0.87, rely=0.35)
        initial_page = Button(frame1, image=logo_sem_nome, relief='flat', cursor='hand2', bd=0, command=lambda: paginaInicial())
        initial_page.place(relx=0.053, rely=0.1, relwidth=0.06, relheight=0.5)
        logq = Label(frame1, image=log, background='Black')
        logq.place(relx=0.8, rely=0.35)
        botao_sair = Button(frame1, text='Sair', background='Black', foreground='White', relief='flat', cursor='hand2', bd=0, activebackground='Black', activeforeground='White', command= lambda: deslogar())
        botao_sair.place(relx=0.8, rely=0.7, relheight=0.13, relwidth=0.035)
        botao_sair.configure(font=(16))
    else:
        frame1 = Frame(janela, background='Black')
        frame1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        image = Label(frame1, image=img_logo, background='Black')
        image.place(relx=0.05, rely= -0.5)
        sacola = Button(frame1, image=carrinho, background='Black', relief='flat', cursor='hand2', bd=0, activebackground='Black', activeforeground='White', command=lambda: pagamento())
        sacola.place(relx=0.87, rely=0.35)
        initial_page = Button(frame1, image=logo_sem_nome, relief='flat', cursor='hand2', bd=0, command=lambda: paginaInicial())
        initial_page.place(relx=0.053, rely=0.1, relwidth=0.06, relheight=0.5)

        Login = Button(frame1, text='Login', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: login())
        Login.place(relx=0.75, rely= 0.4, relwidth=0.04, relheight=0.2)
        separar = Label(frame1, text='|', background='Black', foreground='White')
        separar.place(relx=0.791, rely=0.38)
        separar.configure(font=(fontSeparador))
        Login.configure(font=('Arial', 15))
        Cadastro = Button(frame1, text='Cadastro', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: cadastro())
        Cadastro.configure(font=('Arial', 15))
        Cadastro.place(relx= 0.8, rely= 0.4, relwidth=0.06, relheight=0.2)

def verificarIgualdadeSenha(senha, confSenha):
    igual = False
    tamanhoSenha = len(senha)
    if tamanhoSenha < 8:
        pass
    else:
        if senha == confSenha:
            for i in senha:
                if i == ' ' or i == '':
                    igual = False
                    break
                else:
                    igual = True
    return igual

def verificarEmail(email):
    valid = False
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        emailCliente = open('email.txt', 'r')
        n_itens = emailCliente.readlines()
        if n_itens == []:
            valid = True
        else:
           # emailClient = open('email.txt', 'r')
            for i in n_itens:
                i = i.replace(f'\n','')
                if i == email:
                    valid = False
                    break
                else:
                    valid = True
            #emailClient.close()
        emailCliente.close()
    return valid

def verificarCPF(cpf):
    valid = False
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if len(cpf) == 11:
        digito1 = 0
        digito2 = 0
        mult = 10
        soma = 0
        newCPF = cpf[:9]
        for i in newCPF:
            num = int(i)
            num = num * mult
            mult -=1
            soma +=num
        resto = soma%11
        if resto >= 2:
            digito1 = 11 - resto
        if digito1 == int(cpf[9]):
            mult = 11
            soma = 0
            newCPF = cpf[:10]
            for i in newCPF:
                num = int(i)
                num = num * mult
                mult -=1
                soma +=num
            resto = soma%11
            if resto >= 2:
                digito2 = 11 - resto
            if digito2 == int(cpf[10]):
                cpfCliente = open('cpf.txt', 'r')
                n_itens = cpfCliente.readlines()
                if n_itens == []:
                    valid = True
                else:
                    #cpfClient = open('cpf.txt', 'r')
                    for i in n_itens:
                        i = i.replace('.', '')
                        i = i.replace('-', '')
                        i = i.replace(f'\n', '')
                        if i == cpf:
                            valid = False
                            break
                        else:
                            valid = True
                    #cpfClient.close()
                cpfCliente.close()
    return valid

def verificar_nome(nome):
    valid = False
    if nome[0] != ' ' and nome[-1] != ' ':  
        for i in nome:
            if i.isalpha():
                valid = True
            elif i == ' ':
                valid = True
            else:
                valid = False
                break
    return valid

def dados(senha, confSenha, email, cpf, nome, nascimento):
    global erro_cpf_cadastro, erro_data_cadastro, erro_email_cadastro, erro_nome_cadastro, erro_senha_cadastro
    valid_senha = verificarIgualdadeSenha(senha, confSenha)
    valid_email = verificarEmail(email)
    valid_cpf = verificarCPF(cpf)
    valid_nome = verificar_nome(nome)
    if valid_senha == True and valid_email == True and valid_cpf == True and valid_nome == True:
        print('entrou')
        emailCliente = open('email.txt', 'a')
        passwordCliente = open('password.txt', 'a')
        cpfCliente = open('cpf.txt', 'a')
        nomeCliente = open('nome.txt', 'a')
        emailCliente.write(f'{email}\n')
        passwordCliente.write(f'{senha}\n')
        cpfCliente.write(f'{cpf}\n')
        nomeCliente.write(f'{nome}\n')
        emailCliente.close()
        passwordCliente.close()
        cpfCliente.close()
        nomeCliente.close()
    if valid_senha == False:
        erro_senha_cadastro.set('Senhas não conferem')
    else:
        erro_senha_cadastro.set('')
    if valid_email == False:
        erro_email_cadastro.set('Email inválido ou já cadastrado')
    else:
        erro_email_cadastro.set('')
    if valid_cpf == False:
        erro_cpf_cadastro.set('CPF incorreto ou já cadastrado')
    else:
        erro_cpf_cadastro.set('')
    if valid_nome == False:
        print('oi')
        erro_nome_cadastro.set('Nome inválido')
    else:
        print('ola')
        erro_nome_cadastro.set('')
    '''if valid_data == False:
        erro_data_cadastro.set('Data inválida')
    else:
        erro_data_cadastro.set('')'''

# Pagamentos

def endereco():
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
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

    e = Label(frame2, image=a, background='Black')
    e.place(relx=0.1, rely=0.1)

    separar3 = Label(frame2, text='', background='#FF34D8')
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

def entrega(cep, num, bairro, cidade, complemento, rua):
    valid_cep = False
    valid_numero = False
    valid_bairro = False
    valid_cidade = False
    valid_complemento = False
    valid_rua = False

    #Cep
    cep = cep.replace('-', '')
    if len(cep) == 8:
        valid_cep = True

    #Número
    for i in num:
        if i.isdigit():
            valid_numero = True
        else:
            valid_numero = False
            break
    
    #Bairro
    if bairro[0] != ' ' and bairro[-1] != ' ':
        for i in bairro:
            if i.isalpha() or i == ' ':
                valid_bairro = True
            elif i.isdigit():
                valid_bairro = True
            else:
                valid_bairro = False
                break
    
    #Cidade
    if cidade[0] != ' ' and cidade[-1] != ' ':
        for i in cidade:
            if i.isalpha() or i == ' ':
                valid_cidade = True
            else:
                valid_cidade = False
                break
    
    #Complemento
    if complemento[0] != ' ' and complemento[-1] != ' ':
        for i in complemento:
            if i.isalpha() or i == ' ':
                valid_complemento = True
            else:
                valid_complemento = False
                break  
    
    #Rua
    if rua[0] != ' ' and rua[-1] != ' ':
        for i in rua:
            if i.isalpha() or i == ' ':
                valid_rua = True
            else:
                valid_rua = False
                break

def pagamento():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
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

    eh = Label(frame2, image=ab, background='Black')
    eh.place(relx=0.1, rely=0.1)

    separar3 = Label(frame2, text='', background='#2CFFF8')
    separar3.place(relx=0.15, rely=0.15, relheight=0.001, relwidth=0.7)

    titulo = Label(frame2, text='Pagamento', background='Black', foreground='White')
    titulo.place(relx=0.48, rely=0.17)

    pix = Label(frame2, text='Pix', background='Black', foreground='White')
    pix.place(relx=0.15, rely=0.3)
    pix_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento_pix())
    pix_selecionar.place(relx=0.1, rely=0.3)
    
    boleto = Label(frame2, text='Boleto', background='Black', foreground='White')
    boleto.place(relx=0.15, rely=0.4)
    boleto_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento_boleto())
    boleto_selecionar.place(relx=0.1, rely=0.4)

    cartao = Label(frame2, text='Cartão Débito/Crédito', background='Black', foreground='White')
    cartao.place(relx=0.15, rely=0.5)
    cartao_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento_cartao())
    cartao_selecionar.place(relx=0.1, rely=0.5)

    separar4 = Label(frame2, text='')
    separar4.place(relx=0.5, rely=0.25, relheight=0.65, relwidth=0.001)

    pedido = Label(frame2, text='Resumo do pedido', background='Black', foreground='White')
    pedido.place(relx=0.7, rely=0.3)

    subtotal = Label(frame2, text='Sub-total', background='Black', foreground='White')
    subtotal.place(relx=0.7, rely= 0.4)
    subtotal_valor = Label(frame2, text=f'R$ {total_finalizar}', background='Black', foreground='White')
    subtotal_valor.place(relx=0.8, rely=0.4)

    frete = Label(frame2, text='Frete', background='Black', foreground='White')
    frete.place(relx=0.7, rely= 0.5)
    frete_valor = Label(frame2, text='Frete grátis', background='Black', foreground='White')
    frete_valor.place(relx=0.8, rely=0.5)

    total = Label(frame2, text='Total', background='Black', foreground='White')
    total.place(relx=0.7, rely= 0.6)
    total_valor = Label(frame2, text=f'R$ {total_finalizar}', background='Black', foreground='White')
    total_valor.place(relx=0.8, rely=0.6)

def pagamento_pix():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', bd=0, activebackground='Black', activeforeground='White', relief='flat', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', bd=0, activebackground='Black', activeforeground='White', relief='flat', command= lambda: modelo_moletom())
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', bd=0, activebackground='Black', activeforeground='White', relief='flat', command= lambda: modelo_caneca())
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

    eh = Label(frame2, image=ab, background='Black')
    eh.place(relx=0.1, rely=0.1)

    separar3 = Label(frame2, text='', background='#2CFFF8')
    separar3.place(relx=0.15, rely=0.15, relheight=0.001, relwidth=0.7)

    titulo = Label(frame2, text='Pagamento', background='Black', foreground='White')
    titulo.place(relx=0.48, rely=0.17)

    pix = Label(frame2, text='Pix', background='Black', foreground='White')
    pix.place(relx=0.15, rely=0.3)
    pix_selecionar = Button(frame2, image=botao_pagamento_selecionado, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', )
    pix_selecionar.place(relx=0.1, rely=0.3)
    
    boleto = Label(frame2, text='Boleto', background='Black', foreground='White')
    boleto.place(relx=0.15, rely=0.4)
    boleto_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento_boleto())
    boleto_selecionar.place(relx=0.1, rely=0.4)

    cartao = Label(frame2, text='Cartão Débito/Crédito', background='Black', foreground='White')
    cartao.place(relx=0.15, rely=0.5)
    cartao_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento_cartao())
    cartao_selecionar.place(relx=0.1, rely=0.5)

    separar4 = Label(frame2, text='')
    separar4.place(relx=0.5, rely=0.25, relheight=0.65, relwidth=0.001)

    imagem_pix = Label(frame2, image=pix_logo, background='Black')
    imagem_pix.place(relx=0.55, rely=0.2)

    termos_de_uso = Button(frame2, image=botao1_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White')
    termos_de_uso.place(relx=0.6, rely=0.7)
    termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
    termos.place(relx=0.62, rely=0.7)
    finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White')
    finalizar.place(relx=0.75, rely=0.85)

def pagamento_boleto():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
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

    eh = Label(frame2, image=ab, background='Black')
    eh.place(relx=0.1, rely=0.1)

    separar3 = Label(frame2, text='', background='#2CFFF8')
    separar3.place(relx=0.15, rely=0.15, relheight=0.001, relwidth=0.7)

    titulo = Label(frame2, text='Pagamento', background='Black', foreground='White')
    titulo.place(relx=0.48, rely=0.17)

    pix = Label(frame2, text='Pix', background='Black', foreground='White')
    pix.place(relx=0.15, rely=0.3)
    pix_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento_pix())
    pix_selecionar.place(relx=0.1, rely=0.3)
    
    boleto = Label(frame2, text='Boleto', background='Black', foreground='White')
    boleto.place(relx=0.15, rely=0.4)
    boleto_selecionar = Button(frame2, image=botao_pagamento_selecionado, background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', relief='flat')
    boleto_selecionar.place(relx=0.1, rely=0.4)

    cartao = Label(frame2, text='Cartão Débito/Crédito', background='Black', foreground='White')
    cartao.place(relx=0.15, rely=0.5)
    cartao_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento_cartao())
    cartao_selecionar.place(relx=0.1, rely=0.5)

    separar4 = Label(frame2, text='')
    separar4.place(relx=0.5, rely=0.25, relheight=0.65, relwidth=0.001)

    nome = Label(frame2, text='Nome', background='Black', foreground='White')
    nome.place(relx=0.6, rely=0.3)
    ak = Label(frame2, image=i, background='Black')
    ak.place(relx=0.59, rely=0.35)
    nome_entrada = Entry()
    nome_entrada.place(relx=0.598, rely=0.443, relwidth=0.12, relheight=0.028)

    sobrenome = Label(frame2, text='Sobrenome', background='Black', foreground='White')
    sobrenome.place(relx=0.75, rely=0.3)
    ak1 = Label(frame2, image=i1, background='Black')
    ak1.place(relx=0.745, rely=0.35)
    sobrenome_entrada = Entry()
    sobrenome_entrada.place(relx=0.754, rely=0.443, relwidth=0.15, relheight=0.028)

    documento = Label(frame2, text='Número do documento', background='Black', foreground='White')
    documento.place(relx=0.6, rely=0.5)
    ak2 = Label(frame2, image=i2, background='Black')
    ak2.place(relx=0.6, rely=0.53)
    documento_entrada = Entry()
    documento_entrada.place(relx=0.611, rely=0.56, relheight=0.028, relwidth=0.179)

    termos_de_uso = Button(frame2, image=botao1_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', )
    termos_de_uso.place(relx=0.6, rely=0.7)
    termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
    termos.place(relx=0.62, rely=0.7)
    finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: verificar_dados_boleto(nome_entrada.get(), sobrenome_entrada.get(), documento_entrada.get()))
    finalizar.place(relx=0.75, rely=0.85)

def verificar_dados_boleto(nome, sobrenome, cpf):
    valid_nome = True
    valid_sobrenome = True
    valid_cpf = False
    for i in nome:
        if i == ' ' or not i.isalpha():
            valid_nome = False
            break
    for i in sobrenome:
        if i == ' ' or not i.isalpha():
            valid_sobrenome = False
            break
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if len(cpf) == 11:
        digito1 = 0
        digito2 = 0
        mult = 10
        soma = 0
        newCPF = cpf[:9]
        for i in newCPF:
            num = int(i)
            num = num * mult
            mult -=1
            soma +=num
        resto = soma%11
        if resto >= 2:
            digito1 = 11 - resto
        if digito1 == int(cpf[9]):
            mult = 11
            soma = 0
            newCPF = cpf[:10]
            for i in newCPF:
                num = int(i)
                num = num * mult
                mult -=1
                soma +=num
            resto = soma%11
            if resto >= 2:
                digito2 = 11 - resto
            if digito2 == int(cpf[10]):
                valid_cpf = True
    if valid_cpf == True and valid_sobrenome == True and valid_nome == True:
        finalizar_pedido()
    else:
        pass #printar erro

def pagamento_cartao():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
    canecas.place(relx=0.561, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
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

    eh = Label(frame2, image=ab, background='Black')
    eh.place(relx=0.1, rely=0.1)

    separar3 = Label(frame2, text='', background='#2CFFF8')
    separar3.place(relx=0.15, rely=0.15, relheight=0.001, relwidth=0.7)

    titulo = Label(frame2, text='Pagamento', background='Black', foreground='White')
    titulo.place(relx=0.48, rely=0.17)

    pix = Label(frame2, text='Pix', background='Black', foreground='White')
    pix.place(relx=0.15, rely=0.3)
    pix_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', command= lambda: pagamento_pix())
    pix_selecionar.place(relx=0.1, rely=0.3)
    
    boleto = Label(frame2, text='Boleto', background='Black', foreground='White')
    boleto.place(relx=0.15, rely=0.4)
    boleto_selecionar = Button(frame2, image=botao_pagamento, background='Black', foreground='White', relief='flat', command= lambda: pagamento_boleto())
    boleto_selecionar.place(relx=0.1, rely=0.4)

    cartao = Label(frame2, text='Cartão Débito/Crédito', background='Black', foreground='White')
    cartao.place(relx=0.15, rely=0.5)
    cartao_selecionar = Button(frame2, image=botao_pagamento_selecionado, background='Black', foreground='White', relief='flat')
    cartao_selecionar.place(relx=0.1, rely=0.5)

    separar4 = Label(frame2, text='')
    separar4.place(relx=0.5, rely=0.25, relheight=0.65, relwidth=0.001)

    numero_cartao = Label(frame2, text='Número do cartão', background='Black', foreground='White')
    numero_cartao.place(relx=0.6, rely=0.3)
    ca = Label(frame2, image=numero_cartao_credito, background='Black')
    ca.place(relx=0.59, rely=0.35)
    numero_cartao_entrada = Entry()
    numero_cartao_entrada.place(relx=0.598, rely=0.443, relwidth=0.12, relheight=0.028)

    nome = Label(frame2, text='Nome', background='Black', foreground='White')
    nome.place(relx=0.75, rely=0.3)
    cc = Label(frame2, image=nome_titular_cartao, background='Black')
    cc.place(relx=0.745, rely=0.35)
    nome_entrada = Entry()
    nome_entrada.place(relx=0.754, rely=0.443, relwidth=0.15, relheight=0.028)

    vencimento = Label(frame2, text='Data de vencimento', background='Black', foreground='White')
    vencimento.place(relx=0.6, rely=0.45)
    o = Label(frame2, image=vencimento_cvc, background='Black')
    o.place(relx=0.6, rely=0.49)
    vencimento_entrada = Entry()
    vencimento_entrada.place(relx=0.61, rely=0.53, relwidth=0.06)
    
    codigo = Label(frame2, text='Código de segurança', background='Black', foreground='White')
    codigo.place(relx=0.75, rely=0.45)
    o1 = Label(frame2, image=vencimento_cvc, background='Black')
    o1.place(relx=0.75, rely=0.49)
    codigo_entrada = Entry()
    codigo_entrada.place(relx=0.76, rely=0.53, relwidth=0.06)
    
    id = Label(frame2, text='CPF', background='Black', foreground='White')
    id.place(relx=0.6, rely=0.57)
    o2 = Label(frame2, image=cpf_cartao, background='Black')
    o2.place(relx=0.59, rely=0.62)
    cpf_entrada = Entry()
    cpf_entrada.place(relx=0.598, rely=0.62, relwidth=0.12, relheight=0.028)

    parcelas = Label(frame2, text='Parcelas', background='Black', foreground='White')
    parcelas.place(relx=0.6, rely=0.68)
    o2 = Label(frame2, image=parcelas_cartao, background='Black')
    o2.place(relx=0.61, rely=0.73)
    parcelas_entrada = Label(frame2, textvariable=qntVar, background='White')
    parcelas_entrada.place(relx=0.618, rely=0.76, relwidth=0.02, relheight=0.03)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: diminuir_parcelas())
    diminuir_quantidade.place(relx=0.6, rely=0.75)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: aumentar_parcelas())
    aumentar_quantidade.place(relx=0.66, rely=0.75)

    termos_de_uso = Button(frame2, image=botao1_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White')
    termos_de_uso.place(relx=0.6, rely=0.83)
    termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
    termos.place(relx=0.62, rely=0.83)
    finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: verificar_dados_cartao(numero_cartao_entrada.get(), nome_entrada.get(), vencimento_entrada.get(), codigo_entrada.get(), cpf_entrada.get()))
    finalizar.place(relx=0.75, rely=0.9)

def verificar_dados_cartao(numero_cartao, nome_titular, data_vencimento, codigo, cpf):
    valid_cvv = False
    valid_cpf = False
    validar_cartao = True
    validar_nome_titular = False

    #Validar nome titular
    validar_nome_titular = verificar_nome(nome_titular)

    #Validar cpf
    valid_cpf = verificarCPF(cpf)

    #Validar número cartão
    numero_cartao = numero_cartao.replace(' ', '')
    if len(numero_cartao) == 16: 
        for i in numero_cartao:
            if not i.isdigit():
                validar_cartao = False
                break
    else:
        validar_cartao = False
    
    #Validar data de vencimento

    #Validar codigo de segurança
    if len(codigo) == 3:
        for i in codigo:
            if i.isdigit():
                valid_cvv = True
            else:
                valid_cvv = False
                break

def finalizar_pedido():
    global total_finalizar
    total_finalizar = 0
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
    fontE = tkFont.Font(family="Arial", size=14, weight="bold")
    fontSeparador = tkFont.Font(family='Arial', size=30)

    camisas = Button(frame2, text='Camisas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_camisa())
    camisas.place(relx=0.345, rely=0.01, relwidth=0.085, relheight=0.08)

    moletom = Button(frame2, text='Moletons', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_moletom())
    moletom.place(relx=0.452, rely=0.01, relwidth=0.085, relheight=0.08)

    canecas = Button(frame2, text='Canecas', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: modelo_caneca())
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

    text = Label(frame2, image=finalizar, background='Black', foreground='#FFCFF6')
    text.place(relx=0.25, rely=0.4)

    agradecimento = Label(frame2, text=f'Obrigado por comprar com a\nCompuStore! :)', background='Black', foreground='White')
    agradecimento.place(relx=0.4, rely=0.6)

paginaInicial()

janela.mainloop()