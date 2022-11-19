from datetime import date


def validar_data_vencimento(data_vencimento):
    valid = False

    data_atual = date.today()
    data_atual = data_atual.strftime('%d/%m/%Y')
    dia_atual, mes_atual, ano_atual = data_atual.split('/')
    dia, mes, ano = data_vencimento.split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    dia_atual = int(dia_atual)
    mes_atual = int(mes_atual)
    ano_atual = int(ano_atual)
    if ano_atual <= ano:
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            if(dia<=31):
                valid = True
        elif( mes==4 or mes==6 or mes==9 or mes==11):
            if(dia<=30):
                valid = True
        elif mes==2:
            if (ano%4==0 and ano%100!=0) or (ano%400==0):
                if(dia<=29):
                    valid = True
            elif(dia<=28):
                valid = True
    else:
        valid = False


# Validar telefone e data