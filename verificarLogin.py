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
  print(valid)
  return valid
validateLogin('jeiel', 'lucas')