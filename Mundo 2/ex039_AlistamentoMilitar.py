from datetime import date
ano = int(input("Qual seu ano de nascimento? "))
anoAtual = date.today().year
idade = anoAtual - ano
if idade < 18:
    print("Você ainda vai se alistar no serviço militar em {} ano(s)".format(18 - idade))
elif idade == 18:
    print("Está na hora de se alistar no serviço militar.")
else:
    print("Você já deveria ter se alistado no serviço militar há {} anos. ".format(idade - 18))


