
km = float(input("Quantos km foram percorridos com o carro? "))
dias = int(input("Por quantos dias o carro foi alugado? "))

preco = 60*dias + 0.15*km

print("O preço a pagar pelo aluguel é R${:.2f}.".format(preco))
