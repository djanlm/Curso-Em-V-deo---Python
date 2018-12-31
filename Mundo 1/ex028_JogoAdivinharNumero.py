import random
#Biblioteca pra usar a função sleep
from time import sleep

print('=*'*10 + "JOGO DE ADIVINHAÇÃO" + '=*'*10)
resp = int(input("Digite um número entre 0 e 5: "))
#Gera número aleatorio entre 0 e 5
n = random.randint(0, 5)

print("PROCESSANDO...")
sleep(3)

if resp == n:
    print("Parabéns!!! Você acertou!")
else:
    print("Hmmm... Não foi dessa vez. Resposta errada. Pensei no número {}.".format(n))



