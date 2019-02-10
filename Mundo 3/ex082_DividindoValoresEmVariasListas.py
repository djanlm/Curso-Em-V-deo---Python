lista = []
listap = []
listai = []
while True:
    lista.append(int(input("Insira um número inteiro: ")))
    user = str(input("Deseja continuar? [S/N] ")).lower().strip()
    if user == 'n':
        break

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        listap.append(lista[c])
    else:
        listai.append(lista[c])
print(f"A lista complera é {lista}")
print(f"A lista de pares é {listap}")
print(f"A lista de impares é {listai}")