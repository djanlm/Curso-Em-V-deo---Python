print("Insira nome, idade e sexo de 4 pessoas. ")
contMulheres = 0
maisVelho = 0
nomeMaisVelho = 0
somaIdades = 0

for c in range(1, 5):
    nome = str(input("Insira o nome da {}ª pessoa: ".format(c))).strip()
    idade = int(input("Insira a idade da {}ª pessoa: ".format(c)))
    sexo = str(input("Insira o sexo da {}ª pessoa (M ou F): ".format(c))).strip()
    somaIdades += idade
    if sexo == 'F' and idade < 20:
        contMulheres += 1
    if sexo == 'M':
        if maisVelho < idade:
            maisVelho = idade
            nomeMaisVelho = nome
media = somaIdades/4

print("A média de idade é {}.".format(media))
print("O homem mais velho é {}".format(nomeMaisVelho))
print("{} mulher(es) têm menos de 20 anos de idade.".format(contMulheres))
