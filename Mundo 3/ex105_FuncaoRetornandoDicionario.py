def notas(* n, sit=False):
    """
    ->Analisa várias notas
    :param n: tupla com as notas
    :param sit: mostra ou não a situação de acordo com a média
    :return: retorna um dicionario com o total de notas, a maior e a menor notas, a média e a situaçao
    """
    maior = max(n)
    menor = min(n)
    dic = dict()
    dic['Total'] = len(n)
    dic['Maior'] = maior
    dic['Menor'] = menor
    soma = 0
    for c in range(0, len(n)):
        soma += n[c]
    media = soma/len(n)
    dic['Média'] = media.__round__(2)
    if sit:
        if media >= 7:
            dic['Situação'] = "Boa"
        elif media < 5:
            dic['Situação'] = "Ruim"
        else:
            dic['Situação'] = "Regular"
    return dic


# Main Program
resp = notas(5, 2, 6.5, sit=True)
print(resp)
