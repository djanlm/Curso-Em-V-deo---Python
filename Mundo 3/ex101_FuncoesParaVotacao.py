def voto(ano):
    import datetime
    anoAtual = datetime.date.today().year
    idade = anoAtual - ano
    if idade < 16:
        return "NÃO VOTA"
    elif 18 <= idade <= 65:
        return "VOTO OBRIGATÓRIO"
    else:
        return "VOTO OPCIONAL"


nascimento = int(input("Ano de nascimento: "))
print(voto(nascimento))
