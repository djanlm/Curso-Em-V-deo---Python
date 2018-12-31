nome = str(input("Digite seu nome completo: ")).strip().split() #o split cria uma lista com cada nome
qtd = len(nome)
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é {}".format(nome[qtd-1]))
