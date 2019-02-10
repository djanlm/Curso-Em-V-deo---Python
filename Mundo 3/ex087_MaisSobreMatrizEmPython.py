matrix = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matrix[i].append(int(input(f"Digite um valor para [{i}][{j}]: ")))
print("-="*30)
somaPar = 0
somaColuna = 0
maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[i][j]:^5}]', end="")
        if matrix[i][j] % 2 == 0:
            somaPar += matrix[i][j]
        if j == 2:
            somaColuna += matrix[i][j]
        if i == 1:  # Caso esteja na segunda linha
            if j == 0:
                maior = matrix[i][j]
            elif maior < matrix[i][j]:
                maior = matrix[i][j]
    print("")

print(f'A soma dos valores pares é {somaPar}.')
print(f'A soma dos valores da terceira coluna é {somaColuna}.')
print(f'O maior valor da segunda linha é {maior}.')
