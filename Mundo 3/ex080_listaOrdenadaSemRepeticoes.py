lista = []
for c in range(0, 5):
    valor = int(input("Insira um número: "))
    if len(lista) == 0:
        lista.append(valor)

    else:
        for i in range(0, len(lista)):
            if valor < lista[i]:
                lista.insert(i, valor)
                break  #depois que insere o num da lista, sai do loop
            if i == len(lista) - 1: #quando chega na ultima posicao da lista e nao havia nenhum valor menor
                lista.append(valor)


print(lista)
