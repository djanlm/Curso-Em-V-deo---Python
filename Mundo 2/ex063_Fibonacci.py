n = int(input("Quantos elementos da sequência de Fibonacci desejas imprimir? "))

fib = 0
c = 2
first = 0
second = 1
if n > 1:
    print("{} ".format(first), end=' ')
    print("{} ".format(second), end=' ')
    while c < n:
        fib = first + second
        first = second
        second = fib
        print("{} ".format(fib), end=' ')
        c = c + 1
elif n == 1:
    print("{} ".format(fib))
