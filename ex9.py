#Faça um programa para calcular e exibir o 
#desconto na compra do cliente em uma farmácia, 
#conforme o valor da compra do mesmo digitado pelo usuário 




compra = float(input("Digite o valor da compra: "))

if compra <= 150:
    desconto = compra * 0.05
    print(f'O valor do desconto é R${desconto}')

elif compra > 150 and compra <= 300:
    desconto = compra * 0.07
    print(f'O valor do desconto é R${desconto}')

elif compra > 300 and compra <= 500:
    desconto = compra * 0.10
    print(f'O valor do desconto é R${desconto}')

elif compra > 500:
     desconto = compra * 0.20
     print(f'O valor do desconto é R${desconto}')