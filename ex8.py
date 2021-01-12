#Faça um programa para calcular e exibir a quantidade de parcelas sem juros 
#e o valor de cada parcela, conforme o valor da compra digitado pelo usuário 




valor = float(input("Entre com o valor da compra: "))

if valor <= 100:
    parcela = 2
    valorParcela = valor/2
    print(f'A quantidade de parcelas é {parcela}\nCada parcela será de {valorParcela}')

elif valor > 100 and valor <= 200:
    parcela = 3
    valorParcela = valor/3
    print(f'A quantidade de parcelas é {parcela}\nCada parcela será de {valorParcela}')

elif valor > 200 and valor <= 400:
    parcela = 4
    valorParcela = valor/4
    print(f'A quantidade de parcelas é {parcela}\nCada parcela será de {valorParcela}')

elif valor > 400:
    parcela = 5
    valorParcela = valor/5
    print(f'A quantidade de parcelas é {parcela}\nCada parcela será de {valorParcela}')