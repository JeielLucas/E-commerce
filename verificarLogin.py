import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def validateLogin(email, password):
  print('oi')
  valid = False
  if re.fullmatch(regex, email):
    linha = 0
    arq = open('email.txt', 'r')
    for i in arq:
      linha +=1
      if email == i:
        senhas = open('password.txt', 'r')
        lerSenha = senhas.readlines()
        if lerSenha[linha-1] == password:
          valid = True
  return valid