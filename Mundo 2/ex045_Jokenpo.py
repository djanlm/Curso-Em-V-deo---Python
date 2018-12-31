import random
from time import sleep
print("-="*20)
print(" "*15+"JOKENPO")
print("-="*20)

print("Escolha entre pedra, papel e tesoura")
p = str(input("Digite o nome da opção escolhida: ")).strip().lower()

opcoes = ['pedra', 'papel', 'tesoura']

comp = random.choice(opcoes)
sleep(1)
if comp == p:
    print("Você escolheu {} e o computador escolheu {}, jogo empatado.".format(p, comp))
elif p == 'pedra' and comp == 'papel' or p == 'papel' and comp == 'tesoura' or p == "tesoura" and comp == "pedra":
    print("Você escolheu {} e o computador escolheu {}, você perdeu.".format(p, comp))
elif p == 'pedra' and comp == 'tesoura' or p == 'papel' and comp == 'pedra' or p == "tesoura" and comp == "papel":
    print("Você escolheu {} e o computador escolheu {}, você VENCEU.".format(p, comp))
else:
    print("Opção inválida!")
