print("Digite dois números: ")
n = float(input("Número a: "))
m = float(input("Número b: "))

if n > m:
    print("{} é maior que {}".format(n, m))
elif m > n:
    print("{} é maior que {}".format(m, n))
else:
    print("Os dois números são iguais")