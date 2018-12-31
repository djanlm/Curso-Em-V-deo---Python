import math
ca = float(input("Qual o comprimento do cateto a: "))
cb = float(input("Qual o comprimento do cateto b: "))
h = math.sqrt(pow(ca, 2) + math.pow(cb, 2))
print("O valor da hipotenusa desse triângulo retângulo é {:.2f}".format(h))

#outro método
hi = math.hypot(ca, cb)
