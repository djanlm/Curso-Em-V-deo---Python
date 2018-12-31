n = float(input("Nota 1: "))
m = float(input("Nota 2: "))

media = (m + n)/2

if media < 5:
    print("REPROVADO")
elif media >= 7:
    print("APROVADO")
else:
    print("RECUPERAÇÃO")