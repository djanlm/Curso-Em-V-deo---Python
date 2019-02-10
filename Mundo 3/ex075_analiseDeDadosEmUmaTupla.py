a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))
c = int(input("Insira o terceiro valor: "))
d = int(input("Insira o quarto valor: "))

tupla = (a, b, c, d)

print(f'Você digitou os valor {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vez(es).')

if 3 in tupla:
    print(f'O valor 3 apareceu na posição {tupla.index(3)}')
else:
    print("O valor 3 não foi digitado.")

print("Os valores pares digitados foram ", end="")
for c in tupla:
    if c % 2 == 0:
        print(f'{c} ', end="")
