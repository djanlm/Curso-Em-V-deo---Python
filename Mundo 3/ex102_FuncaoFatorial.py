def fatorial(n, show=False):
    """
    ->Calcula o fatorial de um número
    :param n: O número cujo fatorial será calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial
    """
    fat = 1
    if n == 0:
        string = "1"
    for c in range(n, 0, -1):
        fat *= c
        if show:
            if c >1:
                print(f"{c} x ", end='')
            else:
                print("1 = ", end='')
    return fat


print(fatorial(4, True))

