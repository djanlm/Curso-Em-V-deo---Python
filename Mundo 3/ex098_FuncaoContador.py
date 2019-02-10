from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1  # caso o passo seja negativo, calcula-se o modulo
    if p == 0:
        p = 1  # Pra evitar loop infinito
        
    print("-="*20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=" ", flush=True) # o flush serve para que a funcao sleep nao impeça de mostrar o print no deccorer do programa
            sleep(0.3)
            cont += p
        print('FIM!')
    elif f < i:
        cont = i
        while cont >= f:
            print(f'{cont}', end=" ", flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem: ")
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input("Passo: "))
contador(ini, fim, passo)
