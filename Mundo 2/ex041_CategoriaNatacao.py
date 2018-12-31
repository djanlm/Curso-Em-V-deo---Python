from datetime import date
ano = int(input("Qual seu ano de nascimento? "))
anoAtual = date.today().year
idade = anoAtual - ano
if idade <= 9:
    print("Idade: {}. MIRIM".format(idade))
elif idade <= 14:
    print("Idade: {}. INFANTIL".format(idade))
elif idade <= 19:
    print("Idade: {}. JUNIOR".format(idade))
elif idade <= 25:
    print("Idade: {}. SENIOR".format(idade))
else:
    print("Idade: {}. MASTER".format(idade))

