lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    user = str(input("Quer continuar? [s/n]")).strip().lower()
    if user == 'n':
        break
print("="*30)
print(lista)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não faz parte da lista")