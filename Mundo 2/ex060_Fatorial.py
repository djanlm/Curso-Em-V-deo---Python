n = int(input("Qual número deseja saber o fatorial? "))
m = n
fatorial = 1
if n != 0:
    while n != 0:
        fatorial = fatorial * n
        n -= 1

print("{}! = {}".format(m, fatorial))
