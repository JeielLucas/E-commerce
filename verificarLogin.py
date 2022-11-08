def validateLogin(email, password):
  valid = False
  linha = 0
  arq = open('email.txt', 'r')
  for i in arq:
    linha +=1
    i = i.replace(f'\n', '')
    if i == email:
      senhas = open('password.txt', 'r')
      lerSenha = senhas.readlines()
      lerSenha = lerSenha[linha-1].replace(f'\n', '')
      if lerSenha == password:
        valid = True
      senhas.close()
      break
  arq.close()
  print(valid)
  return valid