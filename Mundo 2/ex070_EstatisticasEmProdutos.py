total = qtdProdCaros = 0
prodMaisBarato = 9999999999999999
nomeBarato = user = ''

while True:
    nome = str(input("Qual o nome do produto? ")).strip().title()
    preco = float(input("Qual o preco do produto? "))
    if preco > 1000:
        qtdProdCaros += 1
    if prodMaisBarato > preco:
        prodMaisBarato = preco
        nomeBarato = nome
    total += preco
    while user !='N' and user != 'S':
        user = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if user == 'N':
        break
    user = ''

print("{:-^40}".format("Fim do Programa"))
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {qtdProdCaros} produtos custando mais de R$1000,00")
print(f"O produto mais barato foi {nomeBarato} que custa R${prodMaisBarato}")