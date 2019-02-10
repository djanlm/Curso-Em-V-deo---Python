lista = []
while True:
    valor = float(input("Digite um valor: "))
    if valor not in lista:
        lista.append(valor)
    else:
        print("Valor duplicado! Insira outro número...")
    user = str(input("Quer continuar? [s/n]")).strip().lower()
    if user[0] == 'n':
        break
lista.sort()
print(f"Você digitou os valores {lista}")
