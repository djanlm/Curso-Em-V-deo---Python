from random import randint
from time import sleep


def sorteio(n):
    print(f"Sorteando 5 valores da lista: ", end="", flush=True)
    for c in range(0, 5):
        n.append(randint(0, 10))
        sleep(0.4)
        print(f"{n[c]}", end=" ", flush=True)
    print("PRONTO!", flush=True)


def somaPares(l):
    soma = 0
    sleep(0.3)
    for c in l:
        if c % 2 == 0:
            soma += c
    print(f"Somando os valores pares de {l}, temos {soma}")


#Main program
lista = []
sorteio(lista)
somaPares(lista)
