c = float(input("Digite a temperatura em ºC: "))
k = 40/72 #constante de conversão
f = (c + 32*k)/k

print("{}ºC equivale a {}ºF.".format(c, f))
