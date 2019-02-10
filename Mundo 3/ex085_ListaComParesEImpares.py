lista = [[], []]
for c in range(1, 8):
    n = int(input(f"Insira o {c}º valor: "))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()
print(f'Os valor pares digitados foram: {lista[0]}')
print(f'Os valor impares digitados foram: {lista[1]}')
