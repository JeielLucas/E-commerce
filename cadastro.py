import re

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


def dados(senha, confSenha, email, cpf, nome, nascimento):
    validSenha = verificarIgualdadeSenha(senha, confSenha)
    if validSenha == True:
        validEmail = verificarEmail(email)
        if validEmail == True:
            validCPF = verificarCPF(cpf)
            if validCPF == True:
                print('Cadastro feito com sucesso')
                emailCliente = open('email.txt', 'a')
                passwordCliente = open('password.txt', 'a')
                cpfCliente = open('cpf.txt', 'a')
                emailCliente.write(f'{email}\n')
                cpfCliente.write(f'{cpf}\n')
                passwordCliente.write(f'{senha}\n')
                emailCliente.close()
                passwordCliente.close()
            else:
                print('CPF Incorreto/formato inválido ou já cadastrado')
        else:
            print('Email em formato inválido ou já cadastrado')
    else:
        print('Senha em formato inválido ou não confere')

