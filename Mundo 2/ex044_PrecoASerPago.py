print('{:=^40}'.format('Lojas Djan'))

p = float(input("Qual o preço do produto? "))
print("Qual a condição de pagamento? ")
print("1-Dinheiro/Cheque(10% de desconto)")
print("2-Cartão à vista (5% de desconto)")
print("3-Cartão em 2x (Preço normal")
print("4-Cartão em 3x ou mais (20% de juros)")
o = int(input(": "))
if o == 1:
    print("O valor a ser pago pelo produto será R${}.".format(p*0.9))
elif o == 2:
    print("O valor a ser pago pelo produto será R${}.".format(p * 0.95))
elif o == 3:
    print("O valor a ser pago pelo produto será R${}.".format(p))
elif o == 4:
    print("O valor a ser pago pelo produto será R${}.".format(p * 1.2))
else:
    print("Opção inválida.")
