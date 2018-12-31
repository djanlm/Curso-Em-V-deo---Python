n = int(input("Qual número deseja saber a tabuada? "))

print('{:=^40}'.format('Tabuada do {}'.format(n)))

for c in range(1, 11):
    print("{} x {:>2} = {}".format(n, c, n*c))
