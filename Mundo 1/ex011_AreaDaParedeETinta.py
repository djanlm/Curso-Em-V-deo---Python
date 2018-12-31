w = float(input("Qual a largura da parede em metros? "))
h = float(input("Qual a altura da parede em metros?"))
area = w*h

#considerando que 1 litro de tinta pinta 2m^2 de área

tinta = area/2

print("Serão necessários {} litros de tinta para pintar toda a parede ".format(tinta))
