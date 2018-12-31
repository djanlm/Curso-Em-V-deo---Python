a = int(input("Insira o primeiro termo da PA: "))
r = int(input("Insira a razão da PA: "))
c = 0
while c < 10:
    print("{} ".format(a), end='')
    print(" -> " if c < 9 else " ", end='')
    a = a + r
    c += 1
