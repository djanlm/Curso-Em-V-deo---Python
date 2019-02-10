import random, time
print("-"*30)
print(f"{'JOGO DA MEGA SENA':^30}")
print("-"*30)
n = int(input("Quantos jogos você quer que eu sorteie? "))
lista = []
for c in range(0, n):
    sorteio = random.sample(range(1, 61), 6)  #sample nao cria números repetidos
    sorteio.sort()
    lista.append(sorteio[:])
    sorteio.clear()
string = " SORTEANDO "+str(n)+" JOGOS "
print(f"{string:=^30}")

for c in range(0, n):
    time.sleep(1)
    print(f"Jogo {c+1}: [", end="")
    for i in range(0, 6):
        if i < 5:
            print(f"{lista[c][i]:02d}, ", end="")  #02d cria um 0 extra na frente das unidades
        else:
            print(f"{lista[c][i]:02d}]")
