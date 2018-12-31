frase = str(input("Escreva uma frase: ")).strip().lower()
qtd = frase.count('a')
print("A letra 'A' aparece {} vezes.".format(qtd))
primeira = frase.find('a')
print("A letra 'A' aparece pela primeira vez na posição {}".format(primeira))

print("A letra 'A' aparece pela última vez na posição {}".format(frase.rfind('a')))

