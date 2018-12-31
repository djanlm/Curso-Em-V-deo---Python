a = int(input("Insira o primeiro termo da PA: "))
r = int(input("Insira a razão da PA: "))
i = 10
c = 0
while i != 0:
    print("{} ".format(a), end=' ')
    a = a + r
    c += 1
    print(" -> " if c != i else " ", end='')
    if c == i:
        print("")
        i = int(input("Quantos mais termos você deseja mostrar? "))
        c = 0