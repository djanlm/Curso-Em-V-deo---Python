from random import randint
from time import sleep
from operator import itemgetter
dic = {}
dic['jogador1'] = randint(1, 6)
dic['jogador2'] = randint(1, 6)
dic['jogador3'] = randint(1, 6)
dic['jogador4'] = randint(1, 6)
ranking = list()
print("Valores sorteados: ")
for k, v in dic.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)

# sorted vai transformarem uma lista de listas.
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)  #o 1 dentro do itemgetter indica que vai ordenar de acordo com o valores no dicionario
print("Ranking dos jogadores: ")
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]} pontos')
    sleep(0.5)
