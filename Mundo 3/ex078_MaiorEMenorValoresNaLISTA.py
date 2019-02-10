lista = []

for c in range(0, 5):
    lista.append(float(input("Insira um valor: ")))
maior = max(lista)
menor = min(lista)

print(f'Os números digitados foram: {lista}')

print(f'O maior número da lista é {maior} na(s) posição(ões) ', end="")
for pos, c in enumerate(lista):
    if c == maior:
        print(f'{pos}', end="...")

print(f'\nO menor número da lista é {menor} na(s) posição(ões) ', end='')
for pos, c in enumerate(lista):
    if c == menor:
        print(f'{pos}', end="...")


