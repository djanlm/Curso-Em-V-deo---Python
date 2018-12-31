n = int(input("Digite um número inteiro: "))
print("Escolha para qual base deseja realizar a conversão:")
print("1-Binário")
print("2-Octal")
print("3-Hexadecimal")

opcao = input()

if opcao == '1':
    print(bin(n)[2:]) #começa a mostrar a partir do segundo digito para cortar o 0b no inicio do numero
elif opcao == '2':
    print(oct(n)[2:])
elif opcao == '3':
    print(hex(n)[2:])
else:
    print("Opção inválida! ")


