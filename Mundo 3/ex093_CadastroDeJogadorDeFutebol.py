dic = {}
dic['nome'] = str(input("Nome do jogador: "))
partidas = int(input("Quantas partidas ele jogou?"))
dic['gols'] = []
for c in range(0, partidas):
    dic['gols'].append(int(input(f"Quantos gols na partida {c}? ")))
total = sum(dic['gols'])
dic['total'] = total
print("-="*30)
print(dic)
print("-="*30)
for k, v in dic.items():
    print(f'{k}: {v}')
print("-="*30)
print(f"O jogador {dic['nome']} jogou {partidas} partidas.")
for i, v in enumerate(dic['gols']):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dic["total"]} gols.')
