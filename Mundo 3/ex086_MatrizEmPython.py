matrix = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matrix[i].append(int(input(f"Digite um valor para [{i}][{j}]: ")))
print("-="*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[i][j]:^5}]', end="")
    print("")
