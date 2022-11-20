from tkinter import *
import re
import tkinter.font as tkFont
from datetime import date

#Váriaveis comuns
qnt_parcelas = 1
qnt_itens = 1
contador = 1
valor_roupa = 20
valor_caneca = 10
carrinho_finalizar = {'Roupa': 0, 'Caneca': 0}
logado = False
total_finalizar = 1
nome_modelo_texto = ''
variavel = False
cont1 = 1

#Janela
janela = Tk()
janela.title('CompuStore')
janela.geometry('1500x850+10+20')
janela.iconbitmap(default='Imagens/Decoracoes_pagina/icon.ico')
janela.resizable(False, False)

#Váriaveis tkinter
qnt_parcelas_Var = IntVar(janela, qnt_parcelas)
qnt_itensVar = IntVar(janela, qnt_itens)
nome_modelo1 = StringVar(janela, nome_modelo_texto)

#Erros Cadastro/Login
erro_login_texto = StringVar(janela, '')
erro_senha_cadastro = StringVar(janela, '')
erro_email_cadastro = StringVar(janela, '')
erro_cpf_cadastro = StringVar(janela, '')
erro_nome = StringVar(janela, '')
erro_data_cadastro = StringVar(janela, '')
erro_sobrenome = StringVar(janela, '')
erro_numero_cartao = StringVar(janela, '')
erro_cvv_cartao = StringVar(janela, '')
erro_data_cartao = StringVar(janela, '')
erro_carrinho_vazio = StringVar(janela, '')
cadastro_realizado_mensagem = StringVar(janela, '')

#Config Frames
frame1 = Frame(janela, background='Black')
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
frame2 = Frame(janela, background='Black')
frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)
frame3 = Frame(janela, background='Black')
frame3.place(relx=0, rely= 0.86, relwidth=1, relheight= 0.15)

#Fontes
fontE = tkFont.Font(family="Arial", size=14, weight="bold")
fontSeparador = tkFont.Font(family='Arial', size=17)
fontLogin = tkFont.Font(family='Arial', size=22)
fonteDados = tkFont.Font(family='Arial', size=16)

#Página inicial
botao_seta = PhotoImage(file='Imagens/Decoracoes_pagina/seta.png')
imagem_logado = PhotoImage(file='Imagens/Decoracoes_pagina/logado.png')
camisa_pagina_inicial = PhotoImage(file='Imagens/Modelos/Modelo_Pagina_Inicial/camisa_pagina_inicial.png')
moletom_pagina_inicial = PhotoImage(file='Imagens/Modelos/Modelo_Pagina_Inicial/moletom_pagina_inicial.png')
caneca_pagina_inicial = PhotoImage(file='Imagens/Modelos/Modelo_Pagina_Inicial/caneca_pagina_inicial.png')

#Imagens dos modelos
camisas_modelos = ['Imagens/Modelos/Modelo_Camisas/camisa1_preto.png', 'Imagens/Modelos/Modelo_Camisas/camisa1_branco.png', 'Imagens/Modelos/Modelo_Camisas/camisa1_cinza.png', 'Imagens/Modelos/Modelo_Camisas/camisa2_preto.png', 'Imagens/Modelos/Modelo_Camisas/camisa2_branco.png', 'Imagens/Modelos/Modelo_Camisas/camisa2_cinza.png', 'Imagens/Modelos/Modelo_Camisas/camisa3_preto.png', 'Imagens/Modelos/Modelo_Camisas/camisa3_branco.png', 'Imagens/Modelos/Modelo_Camisas/camisa3_cinza.png', 'Imagens/Modelos/Modelo_Camisas/camisa4_preto.png', 'Imagens/Modelos/Modelo_Camisas/camisa4_branco.png', 'Imagens/Modelos/Modelo_Camisas/camisa4_cinza.png', 'Imagens/Modelos/Modelo_Camisas/camisa5_preto.png', 'Imagens/Modelos/Modelo_Camisas/camisa5_branco.png', 'Imagens/Modelos/Modelo_Camisas/camisa5_cinza.png']

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

#Comprar Roupas/Caneca
imagem_tamanho_roupa = PhotoImage(file='Imagens/Modelos/Geral/tamanho_M.png') 
imagens_tamanhos_roupas = ['Imagens/Modelos/Geral/tamanho_P.png', 'Imagens/Modelos/Geral/tamanho_M.png', 'Imagens/Modelos/Geral/tamanho_G.png', 'Imagens/Modelos/Geral/tamanho_GG.png']
img_modelo = PhotoImage(file='Imagens/Decoracoes_pagina/Modelo.png')
botao_comprar = PhotoImage(file='Imagens/Pagamento/Geral/comprar.png')
botao_cor_branca = PhotoImage(file='Imagens/Modelos/Geral/botao_cor_branco.png')
botao_cor_preto = PhotoImage(file='Imagens/Modelos/Geral/botao_cor_preto.png')
botao_cor_cinza = PhotoImage(file='Imagens/Modelos/Geral/botao_cor_cinza.png')
botoes_cores = ['Imagens/Modelos/Geral/botao_cor_branco.png', 'Imagens/Modelos/Geral/botao_cor_preto.png', 'Imagens/Modelos/Geral/botao_cor_cinza.png']
#Login e cadastro
imagens_entrada_login = PhotoImage(file='Imagens/Login_Cadastro/entrada_login.png')
imagens_entrada_cadastro = PhotoImage(file='Imagens/Login_Cadastro/entrada_cadastro.png')

# Imagens de entrega e pagamento
botao_pagamento = PhotoImage(file='Imagens/Pagamento/Geral/botao.png')
botao_pagamento_selecionado = PhotoImage(file='Imagens/Pagamento/Geral/botao_selecionado.png')
botao1_pagamento = PhotoImage(file='Imagens/Pagamento/Geral/botao_pequeno.png')
botao1_pagamento_selecionado = PhotoImage(file='Imagens/Pagamento/Geral/botao_pequeno_selecionado.png')

estilizacao_entrega = PhotoImage(file='Imagens/Pagamento/Geral/botao_entrega.png')
estilizacao_pagamento = PhotoImage(file='Imagens/Pagamento/Geral/botao_pagamento.png')

pix_logo = PhotoImage(file='Imagens/Pagamento/Geral/pixLogo.png')

entrada_nome_boleto = PhotoImage(file='Imagens/Pagamento/Boleto/boleto_nome.png')
entrada_sobrenome_boleto = PhotoImage(file='Imagens/Pagamento/Boleto/boleto_sobrenome.png')
entrada_documento_boleto = PhotoImage(file='Imagens/Pagamento/Boleto/boleto_documento.png')

nome_titular_cartao = PhotoImage(file='Imagens/Pagamento/Cartao/nome_titular.png')
numero_cartao_credito = PhotoImage(file='Imagens/Pagamento/Cartao/numero_cartao.png')
vencimento_cvc = PhotoImage(file='Imagens/Pagamento/Cartao/vencimento_cartao.png')
cpf_cartao = PhotoImage(file='Imagens/Pagamento/Cartao/cpf_cartao.png')
parcelas_cartao = PhotoImage(file='Imagens/Pagamento/Cartao/parcelas_cartao.png')

#Finalizacao
finalizar_imagem = PhotoImage(file='Imagens/Decoracoes_pagina/compra_finalizada.png')

#Frame1
img_logo = PhotoImage(file='Imagens/Decoracoes_pagina/logo.png')
carrinho = PhotoImage(file='Imagens/Decoracoes_pagina/carrinho.png')
logo_sem_nome = PhotoImage(file='Imagens/Decoracoes_pagina/logoImagem.png')
image = Label(frame1, image=img_logo, background='Black')
image.place(relx=0.05, rely= -0.5)
sacola = Button(frame1, image=carrinho, background='Black', relief='flat', cursor='hand2', bd=0, activebackground='Black', activeforeground='White', command=lambda: pagamento())
sacola.place(relx=0.87, rely=0.35)
initial_page = Button(frame1, image=logo_sem_nome, relief='flat', cursor='hand2', bd=0, command=lambda: paginaInicial())
initial_page.place(relx=0.053, rely=0.1, relwidth=0.06, relheight=0.5)

botao_login = Button(frame1, text='Login', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: login())
botao_login.place(relx=0.75, rely= 0.4, relwidth=0.04, relheight=0.2)
botao_login.configure(font=('Arial', 15))
separar = Label(frame1, text='|', background='Black', foreground='White')
separar.place(relx=0.791, rely=0.38)
separar.configure(font=(fontSeparador))
botao_cadastro = Button(frame1, text='Cadastro', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: cadastro())
botao_cadastro.configure(font=('Arial', 15))
botao_cadastro.place(relx= 0.8, rely= 0.4, relwidth=0.06, relheight=0.2)


#Frame2
def paginaInicial():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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
    botao_seta_camisa = Button(frame2, image=botao_seta, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', cursor='hand2', activeforeground='White', command=lambda: modelo_camisa())
    botao_seta_camisa.place(relx=0.22, rely=0.47)
    botao_seta_camisa.configure(font=('italic', 30))

    moletom = Label(frame2, text='Moletons', background='Black', foreground='White')
    moletom.place(relx=0.45, rely=0.3)
    moletom.configure(font=(fontE))
    img1_moletom = Button(frame2, image=moletom_pagina_inicial, background='Black', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: modelo_moletom())
    img1_moletom.place(relx=0.42, rely=0.34)
    botao_seta_moletom = Button(frame2, image=botao_seta, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', cursor='hand2', activeforeground='White', command=lambda: modelo_moletom())
    botao_seta_moletom.place(relx=0.57, rely=0.47)
    botao_seta_moletom.configure(font=('italic', 30))

    Caneca = Label(frame2, text='Canecas', background='Black', foreground='White')
    Caneca.place(relx=0.8, rely=0.3)
    Caneca.configure(font=(fontE))
    img1_caneca = Button(frame2, image=caneca_pagina_inicial, background='Black', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: modelo_caneca())
    img1_caneca.place(relx=0.75, rely=0.35)
    botao_seta_caneca = Button(frame2, image=botao_seta, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', cursor='hand2', activeforeground='White', command=lambda: modelo_caneca())
    botao_seta_caneca.place(relx=0.92, rely=0.47)
    botao_seta_caneca.configure(font=('italic', 30))

#Frame3
direitosAutorais = Label(frame3, text='© 2022 CompuStore® | Todos direitos reservados', background='Black', foreground='White')
direitosAutorais.configure(font=('Arial', 16))
direitosAutorais.place(relx=0.325, rely=0.32, relwidth=0.35, relheight=0.2)
pagamento_texto = Label(frame3, text= 'Formas de pagamento', background='Black', foreground='White')
pagamento_texto.place(relx=0.05, rely=0.05)
rodape = PhotoImage(file='Imagens/Decoracoes_pagina/formas_pagamento.png')
cartoes = Label(frame3, image=rodape, background='Black')
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

def aumentar_qnt_roupa():
    global qnt_itens
    qnt_itens += 1
    qnt_itensVar.set(qnt_itens)

def diminuir_qnt_roupa():
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
        imagem_tamanho_roupa['file'] = imagens_tamanhos_roupas[1]
    elif contador == 2:
        imagem_tamanho_roupa['file'] = imagens_tamanhos_roupas[2]
    elif contador == 3:
        imagem_tamanho_roupa['file'] = imagens_tamanhos_roupas[3]

def diminuir_tamanho_roupa():
    global contador
    if contador <= 0:
        contador = 0
    else:
        contador -=1
    if contador == 0:
        imagem_tamanho_roupa['file'] = imagens_tamanhos_roupas[0]
    elif contador == 1:
        imagem_tamanho_roupa['file'] = imagens_tamanhos_roupas[1]
    elif contador == 2:
        imagem_tamanho_roupa['file'] = imagens_tamanhos_roupas[2]

def aumentar_parcelas():
    global qnt_parcelas, qnt_parcelas_Var
    if qnt_parcelas >= 12:
        qnt_parcelas_Var.set(12)
    else:
        qnt_parcelas +=1
        qnt_parcelas_Var.set(qnt_parcelas)

def diminuir_parcelas():
    global qnt_parcelas, qnt_parcelas_Var
    if qnt_parcelas <= 1:
        qnt_parcelas_Var.set(1)
    else:
        qnt_parcelas -=1
        qnt_parcelas_Var.set(qnt_parcelas)

# Página 2
def trocar_cor_roupa(roupa, cor):
    if roupa == 'Camisa1':
        if cor == 'Preto':
            img_modelo['file'] = camisas_modelos[0]
        if cor == 'Branco':
            img_modelo['file'] = camisas_modelos[1]
        if cor == 'Cinza':
            img_modelo['file'] = camisas_modelos[2]
    elif roupa == 'Camisa2':
        if cor == 'Preto':
            img_modelo['file'] = camisas_modelos[3]
        if cor == 'Branco':
            img_modelo['file'] = camisas_modelos[4]
        if cor == 'Cinza':
            img_modelo['file'] = camisas_modelos[5]
    elif roupa == 'Camisa3':
        if cor == 'Preto':
            img_modelo['file'] = camisas_modelos[6]
        if cor == 'Branco':
            img_modelo['file'] = camisas_modelos[7]
        if cor == 'Cinza':
            img_modelo['file'] = camisas_modelos[8]
    elif roupa == 'Camisa4':
        if cor == 'Preto':
            img_modelo['file'] = camisas_modelos[9]
        if cor == 'Branco':
            img_modelo['file'] = camisas_modelos[10]
        if cor == 'Cinza':
            img_modelo['file'] = camisas_modelos[11]
    elif roupa == 'Camisa5':
        if cor == 'Preto':
            img_modelo['file'] = camisas_modelos[12]
        if cor == 'Branco':
            img_modelo['file'] = camisas_modelos[13]
        if cor == 'Cinza':
            img_modelo['file'] = camisas_modelos[14]

def modelo_camisa():
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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
    caneca1.place(relx=0.015, rely=0.35)
    #0.05 0.35
    caneca2 = Button(frame2, image= caneca_modelo2, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca2')])
    caneca2.place(relx=0.215, rely=0.35)
    #0.25 0.35
    caneca3 = Button(frame2, image= caneca_modelo3, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca3')])
    caneca3.place(relx=0.415, rely=0.35)
    #0.45 0.35
    caneca4 = Button(frame2, image= caneca_modelo4, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca4')])
    caneca4.place(relx=0.615, rely=0.35)
    #0.65 0.35
    caneca5 = Button(frame2, image= caneca_modelo5, background='Black', bd=0, activebackground='Black', activeforeground='White', command= lambda: [zerar_quantidade(), comprar_caneca('Caneca5')])
    caneca5.place(relx=0.815, rely=0.35)

# Página 3

def comprar_camisa(modelo):
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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
        nome_modelo1.set('Camisa 1')
    elif modelo == 'Camisa2':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa2_preto.png'
        nome_modelo1.set('Camisa 2')
    elif modelo == 'Camisa3':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa3_preto.png'
        nome_modelo1.set('Camisa 3')
    elif modelo == 'Camisa4':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa4_preto.png'
        nome_modelo1.set('Camisa 4')
    elif modelo == 'Camisa5':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Camisas/camisa5_preto.png'
        nome_modelo1.set('Camisa 5')

    nome_modelo = Label(frame2, textvariable=nome_modelo1, background='Black', foreground='White')
    nome_modelo.place(relx=0.4, rely=0.3)
    valor_modelo = Label(frame2, text='R$69,99', background='Black', foreground='White')
    valor_modelo.place(relx=0.4, rely=0.35)
    cor = Label(frame2, text='Cores', background='Black', foreground='White')
    cor.place(relx=0.4, rely=0.4)
    cor_preto = Button(frame2, image=botao_cor_preto, background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: trocar_cor_roupa(modelo, 'Preto'))
    cor_preto.place(relx=0.35, rely=0.45)
    cor_branca = Button(frame2, image=botao_cor_branca, background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: trocar_cor_roupa(modelo, 'Branco'))
    cor_branca.place(relx=0.4, rely=0.45)
    cor_cinza = Button(frame2, image=botao_cor_cinza, background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: trocar_cor_roupa(modelo, 'Cinza'))
    cor_cinza.place(relx=0.45, rely=0.45)

    quantidade = Label(frame2, text='Quantidade', background='Black', foreground='White')
    quantidade.place(relx=0.4, rely=0.55)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: diminuir_qnt_roupa())
    diminuir_quantidade.place(relx=0.35, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: aumentar_qnt_roupa())
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

    comprar = Button(image=botao_comprar, background='Black', bd=0, activebackground='Black', command= lambda: [adicionar_item_carrinho('Roupa'), endereco()])
    comprar.place(relx=0.7, rely=0.75)

def comprar_moletom(modelo):
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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
        nome_modelo1.set('Moletom 1')
    elif modelo == 'Moletom2':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom2.png'
        nome_modelo1.set('Moletom 2')
    elif modelo == 'Moletom3':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom3.png'
        nome_modelo1.set('Moletom 3')
    elif modelo == 'Moletom4':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom4.png'
        nome_modelo1.set('Moletom 4')
    elif modelo == 'Moletom5':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Moletom/moletom5.png'
        nome_modelo1.set('Moletom 5')

    nome_modelo = Label(frame2, textvariable=nome_modelo1, background='Black', foreground='White')
    nome_modelo.place(relx=0.4, rely=0.3)
    valor_modelo = Label(frame2, text='R$69,99', background='Black', foreground='White')
    valor_modelo.place(relx=0.4, rely=0.35)

    quantidade = Label(frame2, text='Quantidade', background='Black', foreground='White')
    quantidade.place(relx=0.4, rely=0.55)
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: diminuir_qnt_roupa())
    diminuir_quantidade.place(relx=0.35, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White',command= lambda: aumentar_qnt_roupa())
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

    comprar = Button(image=botao_comprar, background='Black', bd=0, activebackground='Black', command= lambda: [adicionar_item_carrinho('Roupa'), endereco()])
    comprar.place(relx=0.7, rely=0.75)

def comprar_caneca(modelo):
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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
        nome_modelo1.set('Caneca 1')
    elif modelo == 'Caneca2':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca2.png'
        nome_modelo1.set('Caneca 2')
    elif modelo == 'Caneca3':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca3.png'
        nome_modelo1.set('Caneca 3')
    elif modelo == 'Caneca4':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca4.png'
        nome_modelo1.set('Caneca 4')
    elif modelo == 'Caneca5':
        img_modelo['file'] = 'Imagens/Modelos/Modelo_Caneca/caneca5.png'
        nome_modelo1.set('Caneca 5')


    nome_modelo = Label(frame2, textvariable=nome_modelo1, background='Black', foreground='White')
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
    diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: diminuir_qnt_roupa())
    diminuir_quantidade.place(relx=0.75, rely=0.6)
    aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: aumentar_qnt_roupa())
    aumentar_quantidade.place(relx=0.85, rely=0.6)
    qnt_itens = Label(frame2, textvariable=qnt_itensVar, background='White', foreground='Black')
    qnt_itens.place(relx=0.8, rely=0.6)

    comprar = Button(image=botao_comprar, background='Black', bd=0, activebackground='Black', command= lambda: [adicionar_item_carrinho('Roupa'), endereco()])
    comprar.place(relx=0.7, rely=0.75)

# Login e cadastro

def login():
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

    texto = Label(frame2, text='Faça o seu login!', background='Black', foreground='White')
    texto.place(relx=0.15, rely=0.08, relwidth=0.2, relheight=0.1)
    texto.configure(font=('Arial', 20))

    emailText = Label(frame2, text='Email:', background='Black', foreground='White')
    emailText.configure(font=(fontLogin))
    emailText.place(relx= 0.1, rely=0.2, relwidth=0.1, relheight=0.2)
    imagem_entrada_login_email = Label(frame2, image=imagens_entrada_login, background='Black')
    imagem_entrada_login_email.place(relx=0.123, rely=0.35)
    email = Entry()
    email.place(relx= 0.14, rely=0.445, relwidth=0.235, relheight=0.04)
    email.configure(font=(14))

    passText = Label(frame2, text='Senha:', background='Black', foreground='White')
    passText.configure(font=(fontLogin))
    passText.place(relx= 0.1, rely=0.48, relwidth=0.1, relheight=0.2)
    imagem_entrada_login_senha = Label(frame2, image=imagens_entrada_login, background='Black')
    imagem_entrada_login_senha.place(relx=0.123, rely=0.62)
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


    texto_para_cadastro = Label(frame2, text='Não tem uma conta?', background='Black', foreground='#2CFFF8')
    texto_para_cadastro.place(relx= 0.68, rely=0.1, relwidth=0.22, relheight=0.2)
    texto_para_cadastro.configure(font=('Arial', 26))
    botao_de_cadastro = Button(frame2, text='Cadastre-se aqui', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: cadastro())
    botao_de_cadastro.configure(font=('Arial', 26))
    botao_de_cadastro.place(relx= 0.7, rely=0.4, relwidth=0.18, relheight=0.15)

def cadastro():
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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
    imagem_entrada_cadastro_nome = Label(frame2, image=imagens_entrada_cadastro, background='Black')
    imagem_entrada_cadastro_nome.place(relx=0.08, rely=0.19)
    validate_nome = Label(frame2, textvariable=erro_nome, background='Black', foreground='White')
    validate_nome.place(relx=0.1, rely=0.32)

    data_nascimento_texto = Label(frame2, text='Data de nascimento:', background='Black', foreground='White')
    data_nascimento_texto.place(relx=0.1, rely=0.37)
    data_nascimento = Entry()
    data_nascimento.configure(font=(fonteDados))
    data_nascimento.place(relx=0.1, rely=0.5, relwidth=0.3)
    imagem_entrada_cadastro_data = Label(frame2, image=imagens_entrada_cadastro, background='Black')
    imagem_entrada_cadastro_data.place(relx=0.08, rely=0.42)
    validate_data = Label(frame2, textvariable=erro_data_cadastro, background='Black', foreground='White')
    validate_data.place(relx=0.1, rely=0.55)

    cpf_texto = Label(frame2, text='Digite seu cpf:', background='Black', foreground='White')
    cpf_texto.place(relx=0.1, rely=0.6)
    cpf = Entry()
    cpf.configure(font=(fonteDados))
    cpf.place(relx=0.1, rely=0.65, relwidth=0.3)
    imagem_entrada_cadastro_cpf = Label(frame2, image=imagens_entrada_cadastro, background='Black')
    imagem_entrada_cadastro_cpf.place(relx=0.08, rely=0.65)
    validate_cpf = Label(frame2, textvariable=erro_cpf_cadastro, background='Black', foreground='White')
    validate_cpf.place(relx=0.1, rely=0.8)

    email_texto = Label(frame2, text='Digite seu email:', background='Black', foreground='White')
    email_texto.place(relx=0.65, rely=0.15)
    email = Entry()
    email.configure(font=(fonteDados))
    email.place(relx=0.65, rely=0.35, relwidth=0.3)
    imagem_entrada_cadastro_email = Label(frame2, image=imagens_entrada_cadastro, background='Black')
    imagem_entrada_cadastro_email.place(relx=0.63, rely=0.19)
    validate_email = Label(frame2, textvariable=erro_email_cadastro, background='Black', foreground='White')
    validate_email.place(relx=0.65, rely=0.32)

    senha_texto = Label(frame2, text='Digite sua senha:', background='Black', foreground='White')
    senha_texto.place(relx=0.65, rely=0.37)
    password = Entry()
    password.configure(font=(fonteDados))
    password.place(relx=0.65, rely=0.5, relwidth=0.3)
    imagem_entrada_cadastro_senha = Label(frame2, image=imagens_entrada_cadastro, background='Black')
    imagem_entrada_cadastro_senha.place(relx=0.63, rely=0.42)
    validate_senha = Label(frame2, textvariable=erro_senha_cadastro, background='Black', foreground='White')
    validate_senha.place(relx=0.65, rely=0.55)
    
    confirmar_senha_texto = Label(frame2, text='Digite sua senha novamente:', background='Black', foreground='White')
    confirmar_senha_texto.place(relx=0.65, rely=0.6)
    confPassword = Entry()
    confPassword.configure(font=(fonteDados))
    confPassword.place(relx=0.65, rely=0.65, relwidth=0.3)
    imagem_entrada_cadastro_confirmar_senha = Label(frame2, image=imagens_entrada_cadastro, background='Black')
    imagem_entrada_cadastro_confirmar_senha.place(relx=0.63, rely=0.65)
    conf_senha = Label(frame2, textvariable=erro_senha_cadastro, background='Black', foreground='White')
    conf_senha.place(relx=0.65, rely=0.8)

    cadastro = Button(frame2, text='Cadastrar', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: dados(password.get(), confPassword.get(), email.get(), cpf.get(), nome_completo.get(), data_nascimento.get()))
    cadastro.place(relx=0.75, rely=0.78)
    cadastro.configure(font=(16))

    cadastro_realizado = Label(frame2, textvariable=cadastro_realizado_mensagem, background='Black', foreground='White')
    cadastro_realizado.place(relx=0.72, rely=0.85)

def isLoged(email, password):
    global logado, erro_login_texto
    dicionario = {'e-mail': email, 'senha': password}
    linha = 0
    arq = open('Dados_cliente/email.txt', 'r')
    for i in arq:
        linha +=1
        i = i.replace(f'\n', '')
        if i == dicionario['e-mail']:
            senhas = open('Dados_cliente/password.txt', 'r')
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
        imagem_usuario_logado = Label(frame1, image=imagem_logado, background='Black')
        imagem_usuario_logado.place(relx=0.8, rely=0.35)
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

        botao_login = Button(frame1, text='Login', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: login())
        botao_login.place(relx=0.75, rely= 0.4, relwidth=0.04, relheight=0.2)
        botao_login.configure(font=('Arial', 15))
        separar = Label(frame1, text='|', background='Black', foreground='White')
        separar.place(relx=0.791, rely=0.38)
        separar.configure(font=(fontSeparador))
        botao_cadastro = Button(frame1, text='Cadastro', background='Black', foreground='White', cursor='hand2', relief='flat', bd=0, activebackground='Black', activeforeground='White', command=lambda: cadastro())
        botao_cadastro.configure(font=('Arial', 15))
        botao_cadastro.place(relx= 0.8, rely= 0.4, relwidth=0.06, relheight=0.2)

def verificarIgualdadeSenha(senha, confSenha):
    igual = False
    tamanhoSenha = len(senha)
    if tamanhoSenha < 8:
        igual = False
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
        emailCliente = open('Dados_cliente/email.txt', 'r')
        n_itens = emailCliente.readlines()
        if n_itens == []:
            valid = True
        else:
            for i in n_itens:
                i = i.replace(f'\n','')
                if i == email:
                    valid = False
                    break
                else:
                    valid = True
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
                cpfCliente = open('Dados_cliente/cpf.txt', 'r')
                n_itens = cpfCliente.readlines()
                if n_itens == []:
                    valid = True
                else:
                    for i in n_itens:
                        i = i.replace('.', '')
                        i = i.replace('-', '')
                        i = i.replace(f'\n', '')
                        if i == cpf:
                            valid = False
                            break
                        else:
                            valid = True
                cpfCliente.close()
    return valid

def verificar_nome(nome):
    valid = False
    if len(nome) != 0:
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

def verificar_data_vencimento(data_vencimento):
    valid_data = False
    try:
        mes, ano = data_vencimento.split('/', 2)
        mes = int(mes)
        ano = int(ano)
        mes = str(mes)
        ano = str(ano)
        if mes >= 1 and mes <=12:
            mes = str(mes)
            ano = str(ano)
            if (len(mes) == 2 or len(mes) == 1) and len(ano) == 4:
                mes = int(mes)
                ano = int(ano)
                valid_data = True
    except:
        valid = False

    if valid_data == True:
        data_atual = date.today()
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        if ano_atual == ano:
            if mes_atual <= mes:
                valid_data = True
            else:
                valid_data = False
        elif ano_atual < ano:
            valid = True
        else:
            valid_data = False
    return valid_data

def data_nascimento(data_nascimento):
    valid_data = False
    try:
        dia, mes, ano = data_nascimento.split('/', 3)
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if mes >= 1 and mes <=12:
            dia = str(dia)
            mes = str(mes)
            ano = str(ano)
            if (len(dia) == 1 or len(dia) == 2) and (len(mes) == 1 or len(mes) == 2) and len(ano) == 4:
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                valid_data = True
    except:
        valid_data = False

    if valid_data == True:
        data_atual = date.today()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        if (ano_atual - ano) > 18:
            valid_data = True
        elif (ano_atual - ano) == 18:
            if mes_atual == mes:
                if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                    if dia <= dia_atual:
                        valid_data = True
                elif mes==4 or mes==6 or mes==9 or mes==11:
                    if dia <= dia_atual:
                        valid_data = True
                else:
                    if (ano%4==0 and ano%100 !=0) or (ano%400==0):
                        if(dia<=29):
                            valid_data = True
                    elif(dia<=28):
                        valid_data = True
            elif mes_atual > mes:
                valid_data = True
            else:
                valid_data = False
        else:
            valid_data = False
    return valid_data

def dados(senha, confSenha, email, cpf, nome, nascimento):
    dados_cliente = []
    valid_senha = verificarIgualdadeSenha(senha, confSenha)
    valid_email = verificarEmail(email)
    valid_cpf = verificarCPF(cpf)
    valid_nome = verificar_nome(nome)
    valid_data = data_nascimento(nascimento)
    if valid_senha == False:
        erro_senha_cadastro.set('Senhas não conferem')
    else:
        erro_senha_cadastro.set('')
    if valid_email == False:
        erro_email_cadastro.set('Email inválido ou já cadastrado')
        cadastro_realizado_mensagem.set('')
    else:
        erro_email_cadastro.set('')
    if valid_cpf == False:
        erro_cpf_cadastro.set('CPF incorreto ou já cadastrado')
    else:
        erro_cpf_cadastro.set('')
    if valid_nome == False:

        erro_nome.set('Nome inválido')
    else:
        erro_nome.set('')
    if valid_data == False:
        erro_data_cadastro.set('Data inválida')
    else:
        erro_data_cadastro.set('')
    if valid_senha == True and valid_email == True and valid_cpf == True and valid_nome == True and valid_data == True:
        dados_cliente.append(nome)
        dados_cliente.append(nascimento)
        emailCliente = open('Dados_cliente/email.txt', 'a')
        passwordCliente = open('Dados_cliente/password.txt', 'a')
        cpfCliente = open('Dados_cliente/cpf.txt', 'a')
        nomeCliente = open('Dados_cliente/dados_cliente.txt', 'a')
        emailCliente.write(f'{email}\n')
        passwordCliente.write(f'{senha}\n')
        cpfCliente.write(f'{cpf}\n')
        nomeCliente.write(f'{dados_cliente}\n')
        emailCliente.close()
        passwordCliente.close()
        cpfCliente.close()
        nomeCliente.close()
        cadastro_realizado_mensagem.set('Cadastro realizado com sucesso')

# Pagamentos

def endereco():
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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

    imagem_estilo_entrega = Label(frame2, image=estilizacao_entrega, background='Black')
    imagem_estilo_entrega .place(relx=0.1, rely=0.1)

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

    botao_qualquer = Button(frame2, text='Ir para o pagamento', background='Black', foreground='White', bd=0, activebackground='Black', activeforeground='White', command= lambda: pagamento())
    botao_qualquer.place(relx=0.75, rely=0.77)

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

    imagem_estilo_pagamento  = Label(frame2, image=estilizacao_pagamento, background='Black')
    imagem_estilo_pagamento .place(relx=0.1, rely=0.1)

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

    carrinho_vazio = Label(frame2, textvariable=erro_carrinho_vazio, background='Black', foreground='White')
    carrinho_vazio.place(relx=0.7, rely=0.8)

def marcar_botao_pagamento():
    global cont1
    cont1 +=1
    if cont1 % 2 == 0:
        botao1_pagamento['file'] = 'Imagens/Pagamento/Geral/botao_pequeno_selecionado.png'
    else:
        botao1_pagamento['file'] = 'Imagens/Pagamento/Geral/botao_pequeno.png'

def pagamento_pix():
    global erro_carrinho_vazio
    menu_logado()
    if total_finalizar > 0:
        erro_carrinho_vazio.set('')
        frame2 = Frame(janela, background='Black')
        frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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

        imagem_estilo_pagamento = Label(frame2, image=estilizacao_pagamento, background='Black')
        imagem_estilo_pagamento.place(relx=0.1, rely=0.1)

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

        termos_de_uso = Button(frame2, image=botao1_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: marcar_botao_pagamento())
        termos_de_uso.place(relx=0.6, rely=0.7)
        termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
        termos.place(relx=0.62, rely=0.7)
        finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda:verificar_login_finalizar_pedido())
        finalizar.place(relx=0.75, rely=0.85)
    else:
        erro_carrinho_vazio.set('Carrinho vazio, adicione itens no carrinho')
        pagamento()

def pagamento_boleto():
    global erro_carrinho_vazio
    menu_logado()
    if total_finalizar > 0:
        erro_carrinho_vazio.set('')
        frame2 = Frame(janela, background='Black')
        frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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

        imagem_estilo_pagamento = Label(frame2, image=estilizacao_pagamento, background='Black')
        imagem_estilo_pagamento.place(relx=0.1, rely=0.1)

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
        imagem_entrada_nome_boleto = Label(frame2, image=entrada_nome_boleto, background='Black')
        imagem_entrada_nome_boleto.place(relx=0.59, rely=0.35)
        nome_entrada = Entry()
        nome_entrada.place(relx=0.598, rely=0.443, relwidth=0.12, relheight=0.028)
        erro_nome_boleto = Label(frame2, textvariable=erro_nome, background='Black', foreground='White')
        erro_nome_boleto.place(relx=0.598, rely=0.43)

        sobrenome = Label(frame2, text='Sobrenome', background='Black', foreground='White')
        sobrenome.place(relx=0.75, rely=0.3)
        imagem_entrada_sobrenome_boleto  = Label(frame2, image=entrada_sobrenome_boleto, background='Black')
        imagem_entrada_sobrenome_boleto .place(relx=0.745, rely=0.35)
        sobrenome_entrada = Entry()
        sobrenome_entrada.place(relx=0.754, rely=0.443, relwidth=0.15, relheight=0.028)
        erro_sobrenome_boleto = Label(frame2, textvariable=erro_sobrenome, background='Black', foreground='White')
        erro_sobrenome_boleto.place(relx=0.754, rely=0.43)

        documento = Label(frame2, text='Número do documento', background='Black', foreground='White')
        documento.place(relx=0.6, rely=0.5)
        imagem_entrada_cpf_boleto = Label(frame2, image=entrada_documento_boleto, background='Black')
        imagem_entrada_cpf_boleto.place(relx=0.6, rely=0.53)
        documento_entrada = Entry()
        documento_entrada.place(relx=0.611, rely=0.56, relheight=0.028, relwidth=0.179)
        erro_documento_boleto = Label(frame2, textvariable=erro_cpf_cadastro, background='Black', foreground='White')
        erro_documento_boleto.place(relx=0.611, rely=0.61)

        termos_de_uso = Button(frame2, image=botao1_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: marcar_botao_pagamento())
        termos_de_uso.place(relx=0.6, rely=0.7)
        termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
        termos.place(relx=0.62, rely=0.7)
        finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: verificar_dados_boleto(nome_entrada.get(), sobrenome_entrada.get(), documento_entrada.get()))
        finalizar.place(relx=0.75, rely=0.85)
    else:
        erro_carrinho_vazio.set('Carrinho vazio, adicione itens no carrinho')
        pagamento()

def verificar_dados_boleto(nome, sobrenome, cpf):
    valid_nome = False
    valid_sobrenome = False
    valid_cpf = False
    if len(nome) != 0:
        for i in nome:
            if i == ' ' or not i.isalpha():
                valid_nome = False
                break
            else:
                valid_nome = True
    if len(sobrenome) != 0:
        for i in sobrenome:
            if i == ' ' or not i.isalpha():
                valid_sobrenome = False
                break
            else:
                valid_sobrenome = True

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
        verificar_login_finalizar_pedido()
    if valid_cpf == False:
        erro_cpf_cadastro.set('CPF em formato inválido')
    else:
        erro_cpf_cadastro.set('')
    if valid_nome == False:
        erro_nome.set('Nome incorreto')
    else:
        erro_nome.set('')
    if valid_sobrenome == False:
        erro_sobrenome.set('Sobrenome incorreto')
    else:
        erro_sobrenome.set('')

def pagamento_cartao():
    global erro_carrinho_vazio
    menu_logado()
    if total_finalizar > 0:
        erro_carrinho_vazio.set('')
        frame2 = Frame(janela, background='Black')
        frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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

        imagem_estilo_pagamento = Label(frame2, image=estilizacao_pagamento, background='Black')
        imagem_estilo_pagamento.place(relx=0.1, rely=0.1)

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
        numero_cartao.place(relx=0.6, rely=0.28)
        imagem_entrada_numero_cartao = Label(frame2, image=numero_cartao_credito, background='Black')
        imagem_entrada_numero_cartao.place(relx=0.59, rely=0.32)
        numero_cartao_entrada = Entry()
        numero_cartao_entrada.place(relx=0.598, rely=0.423, relwidth=0.12, relheight=0.028)
        numero_cartao_erro = Label(frame2, textvariable=erro_numero_cartao, background='Black', foreground='White')
        numero_cartao_erro.place(relx=0.598, rely=0.4)

        nome = Label(frame2, text='Nome', background='Black', foreground='White')
        nome.place(relx=0.75, rely=0.28)
        imagem_entrada_nome_cartao = Label(frame2, image=nome_titular_cartao, background='Black')
        imagem_entrada_nome_cartao.place(relx=0.745, rely=0.32)
        nome_entrada = Entry()
        nome_entrada.place(relx=0.754, rely=0.423, relwidth=0.15, relheight=0.028)
        nome_cartao_erro = Label(frame2, textvariable=erro_nome, background='Black', foreground='White')
        nome_cartao_erro.place(relx=0.75, rely=0.4)

        vencimento = Label(frame2, text='Data de vencimento', background='Black', foreground='White')
        vencimento.place(relx=0.6, rely=0.45)
        imagem_entrada_data_cartao = Label(frame2, image=vencimento_cvc, background='Black')
        imagem_entrada_data_cartao.place(relx=0.6, rely=0.49)
        vencimento_entrada = Entry()
        vencimento_entrada.place(relx=0.61, rely=0.53, relwidth=0.06)
        data_cartao_erro = Label(frame2, textvariable=erro_data_cartao, background='Black', foreground='White')
        data_cartao_erro.place(relx=0.61, rely=0.55)

        codigo = Label(frame2, text='Código de segurança', background='Black', foreground='White')
        codigo.place(relx=0.75, rely=0.45)
        imagem_entrada_cvv_cartao = Label(frame2, image=vencimento_cvc, background='Black')
        imagem_entrada_cvv_cartao.place(relx=0.745, rely=0.49)
        codigo_entrada = Entry()
        codigo_entrada.place(relx=0.754, rely=0.53, relwidth=0.06)
        cvv_cartao_erro = Label(frame2, textvariable=erro_cvv_cartao, background='Black', foreground='White')
        cvv_cartao_erro.place(relx=0.75, rely=0.55)

        id = Label(frame2, text='CPF', background='Black', foreground='White')
        id.place(relx=0.6, rely=0.605)
        imagem_entrada_cpf_cartao = Label(frame2, image=cpf_cartao, background='Black')
        imagem_entrada_cpf_cartao.place(relx=0.59, rely=0.64)
        cpf_entrada = Entry()
        cpf_entrada.place(relx=0.598, rely=0.63, relwidth=0.12, relheight=0.028)
        cpf_cartao_erro = Label(frame2, textvariable=erro_cpf_cadastro, background='Black', foreground='White')
        cpf_cartao_erro.place(relx=0.598, rely=0.72)

        parcelas = Label(frame2, text='Parcelas', background='Black', foreground='White')
        parcelas.place(relx=0.8, rely=0.6)
        imagem_entrada_parcelas_cartao = Label(frame2, image=parcelas_cartao, background='Black')
        imagem_entrada_parcelas_cartao.place(relx=0.8, rely=0.64)
        parcelas_entrada = Label(frame2, textvariable=qnt_parcelas_Var, background='White')
        parcelas_entrada.place(relx=0.807, rely=0.67, relwidth=0.02, relheight=0.03)
        diminuir_quantidade = Button(frame2, text='-', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: diminuir_parcelas())
        diminuir_quantidade.place(relx=0.785, rely=0.66)
        aumentar_quantidade = Button(frame2, text='+', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: aumentar_parcelas())
        aumentar_quantidade.place(relx=0.84, rely=0.66)

        termos_de_uso = Button(frame2, image=botao1_pagamento, background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: marcar_botao_pagamento())
        termos_de_uso.place(relx=0.6, rely=0.87)
        termos = Label(frame2, text='Você concorda com nossos Termos e Condições', background='Black', foreground='White')
        termos.place(relx=0.63, rely=0.88)
        finalizar = Button(frame2, text='Finalizar pedido', background='Black', foreground='White', relief='flat', bd=0, activebackground='Black', activeforeground='White', command= lambda: verificar_dados_cartao(numero_cartao_entrada.get(), nome_entrada.get(), vencimento_entrada.get(), codigo_entrada.get(), cpf_entrada.get()))
        finalizar.place(relx=0.85, rely=0.9)
    else:
        erro_carrinho_vazio.set('Carrinho vazio, adicione itens no carrinho')
        pagamento()

def verificar_dados_cartao(numero_cartao, nome_titular, data_vencimento, codigo, cpf):
    valid_cvv = False
    valid_cpf = False
    validar_cartao = False
    validar_nome_titular = False
    validar_data = False

    #Validar nome titular
    validar_nome_titular = verificar_nome(nome_titular)

    #Validar cpf
    valid_cpf = verificarCPF(cpf)

    #Validar número cartão
    numero_cartao = numero_cartao.replace(' ', '')
    if len(numero_cartao) == 16: 
        for i in numero_cartao:
            if i.isdigit():
                validar_cartao = True
            else:
                validar_cartao = False
                break
    else:
        validar_cartao = False
    
    #Validar data de vencimento
    validar_data = verificar_data_vencimento(data_vencimento)

    #Validar codigo de segurança
    if len(codigo) == 3:
        for i in codigo:
            if i.isdigit():
                valid_cvv = True
            else:
                valid_cvv = False
                break

    if valid_cvv == True:
        erro_cvv_cartao.set('')
    else:
        erro_cvv_cartao.set('Código de segurança incorreto')
    if valid_cpf == True:
        erro_cpf_cadastro.set('')
    else:
        erro_cpf_cadastro.set('CPF em formato inválido')
    if validar_cartao == True:
        erro_numero_cartao.set('')
    else:
        erro_numero_cartao.set('Número do cartão incorreto')
    if validar_nome_titular == True:
        erro_nome.set('')
    else:
        erro_nome.set('Nome incorreto')
        
    if validar_data == True:
        erro_data_cartao.set('')
    else:
        erro_data_cartao.set('Data inválida')

def finalizar_pedido():
    global total_finalizar
    total_finalizar = 0
    menu_logado()
    frame2 = Frame(janela, background='Black')
    frame2.place(relx=0, rely=0.205, relwidth=1, relheight=0.65)

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

    text = Label(frame2, image=finalizar_imagem, background='Black')
    text.place(relx=0.25, rely=0.4)

    agradecimento = Label(frame2, text=f'Obrigado por comprar com a\nCompuStore! :)', background='Black', foreground='White')
    agradecimento.place(relx=0.4, rely=0.6)

def verificar_login_finalizar_pedido():
    if logado == True and cont1 % 2 == 0:
        finalizar_pedido()
    elif logado == True and cont1 % 2 != 0:
        print('aceite os termos')
    else:
        janela2 = Toplevel()
        janela2.title('CompuStore')
        janela2.geometry('600x400')
        janela2.iconbitmap(default='Imagens/Decoracoes_pagina/icon.ico')
        janela2.resizable(False, False)
        janela2.configure(background='Black')

        text = Label(janela2, text='Faça Login para poder comprar', background='Black', foreground='White')
        text.place(relx=0.2, rely=0.2)

        botao_login = Button(janela2, text='Login', background='Black', foreground='White', activebackground='Black', activeforeground='White', bd=0, relief='flat', command= lambda: [janela2.destroy(), login()])
        botao_login.place(relx=0.3, rely=0.3)
        botao_cadastro = Button(janela2, text='Cadastro', background='Black', foreground='White', activebackground='Black', activeforeground='White', bd=0, relief='flat', command= lambda: [janela2.destroy(), cadastro()])
        botao_cadastro.place(relx=0.5, rely=0.3)

paginaInicial()

janela.mainloop()