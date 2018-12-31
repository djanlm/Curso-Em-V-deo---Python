n = float(input("Insira o primeiro número: "))
m = float(input("Insira o segundo número: "))
opcao = 0
while opcao != 5:

    print("[1]Somar")
    print("[2]Multiplicar")
    print("[3]Maior")
    print("[4]Novos Números")
    print("[5]Sair")
    opcao = int(input(": "))
    if opcao == 1:
        print("{} + {} = {}".format(n, m, n+m))
    elif opcao == 2:
        print("{} x {} = {}".format(n, m, n*m))
    elif opcao == 3:
        if m > n:
            print("{} > {}".format(m, n))
        elif n > m:
            print("{} > {}".format(n, m))
        else:
            print(" Os números são iguais.")
    elif opcao == 4:
        n = float(input("Insira o primeiro número: "))
        m = float(input("Insira o segundo número: "))
print("Saindo do programa...")