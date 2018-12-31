from datetime import date
anoAtual = date.today().year

cont = 0
for c in range(1, 8):
    ano = int(input("Insira o ano de nascimento da {}º pessoa:".format(c)))
    if anoAtual - ano > 20:
        cont = cont + 1

print("{} pessoas atingiram a maioriadade.".format(cont))
print("{} pessoas ainda não atingiram a maioriadade.".format(7-cont))