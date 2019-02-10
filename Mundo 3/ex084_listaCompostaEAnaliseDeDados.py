pessoas = []
pop = []
while True:
    pessoas.append(str(input("Insira o nome: ")))
    pessoas.append(float(input("Insira o peso: ")))
    pop.append(pessoas[:])
    pessoas.clear()
    user = str(input("Deseja continuar inserindo? [s/n]")).strip()
    if user in 'nN':
        break

print(f"Ao todo, você cadastrou {len(pop)} pessoas.")

for c in pop:
    if pop.index(c) == 0:
        max = min = c[1]
    else:
        if max < c[1]:
            max = c[1]
        if min > c[1]:
            min = c[1]

gordo = []
magro = []
for c in pop:
    if c[1] == max:
        gordo.append(c[0])
    if c[1] == min:
        magro.append(c[0])

print(f'O maior peso foi {max}kg. Peso de {gordo}')
print(f'O menor peso foi {min}kg. Peso de {magro}')