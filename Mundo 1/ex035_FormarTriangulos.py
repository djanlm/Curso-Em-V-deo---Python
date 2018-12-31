print("Insira o comprimento de 3 retas.")
r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if r1+r2 > r3:
    if r1+r3 > r2:
        if r2+r3 > r1:
            print("As retas podem formar um triângulo. ")
        else:
            print("As retas \033[1;31mnão\033[m podem formar um triângulo. ")
    else:
        print("As retas \033[1;31mnão\033[m podem formar um triângulo. ")
else:
    print("As retas \033[1;31mnão\033[m podem formar um triângulo. ")