from random import randint
comp = randint(0, 10)
print('\033[1;33m=-'*20)
print('\033[1;32m{:^40}'.format('JOGO DA ADIVINHAÇÃO'))
print('\033[1;33m=-'*20+'\033[m')
guess = int(input("Qual número entre 0 e 10 eu pensei? "))
tentativas = 1
while guess != comp:
    print("\033[1;34mO número que pensei não foi esse, tente novamente.\033[m")
    guess = int(input("Qual número entre 0 e 10 eu pensei? "))
    tentativas += 1
print("Após {} tentativas você ACERTOU!!! ".format(tentativas))
