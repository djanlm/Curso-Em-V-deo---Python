print("Insira o peso de 5 pessoas. ")

menor = 0
maior = 0
for c in range(1, 6):
    p = float(input("Digite o peso da {}ª pessoa: ".format(c)))
    if c == 1:
        menor = p
        maior = p
    else:
        if menor > p:
            menor = p
        if maior < p:
            maior = p

print("O maior peso foi {}kg.".format(maior))
print("O menor peso foi {}kg.".format(menor))
