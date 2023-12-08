def obter_signo(dia, mes):
    if (mes == 4 and dia >= 19) or (mes == 5 and dia <=13):
        return "Áries"

    if (mes == 5 and dia >= 14) or (mes == 6 and dia <=19):
        return "Touro"

    if (mes == 6 and dia >= 20) or (mes == 7 and dia <=20):
        return "Gêmeos"

    if (mes == 7 and dia >= 21) or (mes == 8 and dia <=9):
        return "Câncer"

    if (mes == 8 and dia >= 10) or (mes == 9 and dia <=15):
        return "Leão"

    if (mes == 9 and dia >= 16) or (mes == 10 and dia <=30):
        return "Virgem"

    if (mes == 10 and dia >= 31) or (mes == 11 and dia <=22):
        return "Libra"

    if (mes == 11 and dia >= 23) or (mes == 11 and dia <=29):
        return "Escorpião"

    if (mes == 11 and dia >= 30) or (mes == 12 and dia <=17):
        return "Serpentário"

    if (mes == 12 and dia >= 18) or (mes == 1 and dia <=18):
        return "Sagitário"

    if (mes == 1 and dia >= 19) or (mes == 2 and dia <=15):
        return "Capricornio"

    if (mes == 2 and dia >= 16) or (mes == 3 and dia <=11):
        return "Aquario"

    if (mes == 3 and dia >= 12) or (mes == 4 and dia <=16):
        return "Peixes"

data_nascimento = input("Digite a data de nascimento (dia/mes): ")
dia, mes = map(int, data_nascimento.split('/'))

signo = obter_signo(dia, mes)
print(f"Seu signo é {signo}.")