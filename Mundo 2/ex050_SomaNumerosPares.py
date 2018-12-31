soma = 0
for c in range(1, 7):
    n = int(input("Insira o {}º número inteiro: ".format(c)))
    if n % 2 == 0:
        soma += n

print("A soma de todos os números digitados que são pares é {}.".format(soma))