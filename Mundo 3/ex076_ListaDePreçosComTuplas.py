tupla = ('Pão', 2, 'Leite', 3.50, 'Biscoito', 4.10, 'Miojo', 1, 'Cebolitos', 16.50)
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)

for c in range(0, len(tupla), 2):
    print('{:.<30}'.format(tupla[c])+'R$'+"{:>8.2f}".format(tupla[c+1]))

print('-'*40)

