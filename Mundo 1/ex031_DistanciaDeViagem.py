d = float(input("Qual a distância da viagem em km: "))
if d > 200:
    p = d*0.45
else:
    p = d*0.5
print("O preço da passagem será de R${}".format(p))
