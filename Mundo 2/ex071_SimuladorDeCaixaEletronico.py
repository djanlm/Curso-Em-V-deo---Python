print("{:=^50}".format("CAIXA ELETRÔNICO"))

valor = int(input("Qual o valor a ser sacado(inteiro)? R$"))
qtd50 = qtd20 = qtd10 = qtd1 = 0

qtd50 = valor//50
valor = valor - 50*qtd50
qtd20 = valor//20
valor = valor - 20*qtd20
qtd10 = valor // 10
valor = valor - 10 * qtd10
qtd1 = valor
valor = valor - qtd1

print(f"Notas de R$50: {qtd50}")
print(f"Notas de R$20: {qtd20}")
print(f"Notas de R$10: {qtd10}")
print(f"Notas de R$1: {qtd1}")

