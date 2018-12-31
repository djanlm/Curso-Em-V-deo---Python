print("Digite os números que deseja somar, aperte 999 para parar: ")

n = 0
soma = 0
c = 0
while n != 999:
    n = int(input(": "))
    if n != 999:
        soma = soma + n
        c += 1
print("A soma dos {} números digitados é {}.".format(c, soma))


