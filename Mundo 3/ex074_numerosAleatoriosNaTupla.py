import random

tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print('Os números sorteados foram: ', end="")
for c in tupla:
    print(f"{c} ", end="")
print("")
print(f'O maior valor sorteado foi {sorted(tupla)[-1]}')
print(f'O menor valor sorteado foi {sorted(tupla)[1]}')

#ou
#print(f'O maior valor sorteado foi {max(tupla)}')
#print(f'O menor valor sorteado foi {min(tupla)}')
