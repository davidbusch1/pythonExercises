#Faça um programa para calcular e exibir o desconto de INSS 
#conforme o valor do salário digitado pelo usuário 




salario = float(input("Digite o salario: "))

if salario <= 600:
    desconto = salario * 0.07
    print(f'O valor do desconto do INSS é R${desconto}')

elif salario > 600 and salario <= 800:
    desconto = salario * 0.08
    print(f'O valor do desconto do INSS é R${desconto}')

elif salario > 800 and salario <= 1200:
    desconto = salario * 0.09
    print(f'O valor do desconto do INSS é R${desconto}')

elif salario > 1200:
    desconto = salario * 0.11
    print(f'O valor do desconto do INSS é R${desconto}')
