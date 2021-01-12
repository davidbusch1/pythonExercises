#Faça um programa que leia um número inteiro e diga se este é positivo, negativo ou zero




num = int(input("Entre com um número inteiro: "))

if num == 0:
    print(f'Seu número é 0')

elif num > 0:
    print(f'Seu número é positivo')

elif num < 0:
    print(f'Seu número é negativo')