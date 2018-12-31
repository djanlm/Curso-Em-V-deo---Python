import math
a = float(input("Digite um ângulo qualquer: "))
a = a*math.pi/180 #ou math.radians(a)
seno = math.sin(a)
cosseno = math.cos(a)
tangente = math.tan(a)
print("seno = {:.2f}".format(seno))
print("cosseno = {:.2f}".format(cosseno))
print("tangente = {:.2f}".format(tangente))

