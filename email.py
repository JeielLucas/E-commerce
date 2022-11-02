email = 'jeiellucas@..com'
caracter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
# Não pode conter caracter especial V
# Não pode conter . no inicio V
# Não pode conter @ no inicio V
# Nâo pode conter . no final do local V
# Não pode conter . no final do dominio V
# Apenas letras, números e . V
# Existência de @ e .com no email V
# Existir um dominio antes do .com V
# Não deixar 2 pontos consecutivos
def validateEmail(email):
    isValid = True
    if email[0] == '@' or email[0] == '.':
        isValid = False
    else:
        if '@' in email and '.com' in email:
            inicioEmail, dominio = email.split('@', 1)
            print(inicioEmail) # retirar
            print(dominio) # retirar
            print(len(dominio)) # retirar
            if inicioEmail[-1] == '.' or dominio[-1] == '.' or len(dominio) <= 4:
                isValid = False
            else:
                for i in inicioEmail:
                    if i in caracter:
                        isValid = True
                    else:
                        isValid = False
                        break
                if isValid == True:
                    for i in dominio:
                        if i in caracter:
                            isValid = True
                        else:
                            isValid = False
                            break
    return isValid

validate = validateEmail(email)
print(validate)

'''with open('email.txt') as f:
        for i in f:
            if i == email:
                isValid = False'''