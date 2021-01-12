#Faça um programa para calcular e exibir o desconto na compra 
#do cliente, conforme o valor da compra do mesmo digitado pelo usuário 




compra = float(input("Valor da compra: "))

if compra <= 50:
    desconto = compra * 0.95
    print(f'O valor com desconto é R${desconto}')

elif compra > 50 and compra <= 100:
    desconto = compra * 0.92
    print(f'O valor com desconto é R${desconto}')

elif compra > 100 and compra <= 150:
    desconto = compra * 0.88
    print(f'O valor com desconto é R${desconto}')

elif compra > 150:
    desconto = compra * 0.85
    print(f'O valor com desconto é R${desconto}')
