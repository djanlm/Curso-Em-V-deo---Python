countIdade = countMen = countMulher = 0

while True:
    sexo = user = ''
    idade = int(input("Idade: "))

    if idade >= 18:
        countIdade += 1
    while sexo != 'M' and sexo != 'F':
        sexo = str(input("Sexo[M/F]:")).strip().upper()
        if sexo == 'M':
            countMen += 1
        if sexo == 'F' and idade < 20:
            countMulher += 1
    while user !='N' and user != 'S':
        user = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if user == 'N':
        break

print("===== Fim do Programa =====")
print(f"Total de pessoas com mais de 18 anos: {countIdade}")
print(f"Ao todo temos {countMen} homens cadastrados.")
print(f"E temos {countMulher} mulheres com menos de 20 anos.")