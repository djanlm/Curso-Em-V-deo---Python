print("Digite números para saber a média, o maior e o menor: ")
maior = 0
menor = 0
soma = 0
media = 0
o = ""
n = 0
c = 0
while o !='N':
    n = float(input(": "))
    soma += n
    if c == 0:
        maior = n
        menor = n
    c += 1
    if maior < n:
        maior = n

    if menor > n:
        menor = n
    o = str(input("Deseja continuar? [S/N]")).upper()
media = soma/c
print("O maior número é {}, o menor número é {} e a média é {}.".format(maior, menor, media))
