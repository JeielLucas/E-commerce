def validateLogin(email, password):
  valid = False
  linha = 0
  arq = open('email.txt', 'r')
  print(f'parametro: {email}')
  for i in arq:
    print(f'email atual: {i}')
    linha +=1
    if email == i:
      print(f'oi {i}')
      senhas = open('password.txt', 'r')
      lerSenha = senhas.readlines()
      print(i)
      if lerSenha[linha-1] == password:
        valid = True
        senhas.close()
      break
    else:
      print(f'ola {i}')
  arq.close()
  print(valid)
  return valid

validateLogin('jeiel@gmail.com', 'Jejeu')