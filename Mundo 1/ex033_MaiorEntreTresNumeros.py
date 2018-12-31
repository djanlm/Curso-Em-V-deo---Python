print("Digite 3 números: ")
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

if n1 > n2:
    if n1 > n3:
        print("{} é o maior número. ".format(n1))
else:
    if n2 > n3:
        print("{} é o maior número. ".format(n2))
    else:
        print("{} é o maior número. ".format(n3))

if n1 < n2:
    if n1 < n3:
        print("{} é o menor número. ".format(n1))
else:
    if n2 < n3:
        print("{} é o menor número. ".format(n2))
    else:
        print("{} é o menor número. ".format(n3))
