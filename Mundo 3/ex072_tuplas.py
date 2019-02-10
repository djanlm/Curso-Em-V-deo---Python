numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito'
           , 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

user = int(input("Insira um número entre 0 e 20: "))
while user < 0 or user > 20:
    user = int(input("Insira um número entre 0 e 20: "))

print(numbers[user])
