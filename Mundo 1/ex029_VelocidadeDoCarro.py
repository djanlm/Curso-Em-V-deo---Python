v = float(input("Qual a velocidade do carro? "))
if v > 80:
    print("Você foi multado e terá que pagar uma multa de R${}".format((v-80)*7))
