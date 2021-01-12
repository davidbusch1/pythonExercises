#Faça um programa que determine se um dado número é par ou ímpar.




num = int(input("Entre com um número: "))

if num % 2 == 0:
    print(f'Seu número é par!')

elif num % 2 != 0:
    print(f'Seu número é ímpar!')