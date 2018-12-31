p = int(input("Qual o primeiro termo da PA? "))
r = int(input("Qual a razão da PA? "))

for c in range(p, p+10*r, r):
    print("{} ".format(c), end='')

