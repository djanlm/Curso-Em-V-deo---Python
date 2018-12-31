sal = float(input("Qual seu salário? "))

if sal > 1250:
    print("O seu salário aumentará para R${}".format(sal*1.10))
else:
    print("O seu salário aumentará para R${}".format(sal * 1.15))