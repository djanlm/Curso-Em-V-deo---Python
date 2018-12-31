print('-='*20)
print('{}VERIFIQUE SE SEU EMPRÉSTIMO SERÁ APROVADO!!{}'.format('\033[1;31m', '\033[m'))
print('-='*20)

casa = float(input("Qual o valor da casa que desejas comprar? R$"))
sal = float(input("Qual seu salário? R$"))
anos = int(input("Em quantos anos pretender pagar? "))

meses = anos*12
prestação = casa/meses

if prestação > sal*0.3:
    print("Seu empréstimo com prestação de R${:.2f} \033[1;31mnão \033[mfoi aceito".format(prestação))
else:
    print("Seu empréstimo com prestação de R${:.2f} foi aceito".format(prestação))

