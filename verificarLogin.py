from tkinter import *
import tkinter.font as tkFont

def validateLogin(email, password):
  dicionario = {'e-mail': email, 'senha': password}
  valid = False
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
        valid = True
      senhas.close()
      break
  arq.close()
  return valid

def isLoged(janela, email, password):
  valid = validateLogin(email, password)
  if valid == True:
    print('ola')
  else:
    frame1 = Frame(janela, background='Black')
    frame1.place(relx=0, rely=0, relwidth=1, relheight=0.2)
    img_logo1 = PhotoImage(file='Imagens\logo1.png')
    carrinho1 = PhotoImage(file='Imagens\carrinho.png')
    logo_sem_nome1 = PhotoImage(file='Imagens\logoImagem.png')
    image = Label(frame1, image=img_logo1, background='Black')
    image.place(relx=0.05, rely= -0.5)
    sacola = Label(frame1, image=carrinho1, background='Black')
    sacola.place(relx=0.87, rely=0.35)
    initial_page = Button(frame1, image=logo_sem_nome1, relief='flat', cursor='hand2')
    initial_page.place(relx=0.053, rely=0.17, relwidth=0.06, relheight=0.55)