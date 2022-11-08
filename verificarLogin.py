def validateLogin(email, password):
  valid = False
  linha = 0
  arq = open('email.txt', 'r')
  for i in arq:
    linha +=1
    if i == email:
      senhas = open('password.txt', 'r')
      lerSenha = senhas.readlines()
      if lerSenha[linha-1] == password:
        valid = True
        senhas.close()
      break
  arq.close()
  print(valid)
  return valid