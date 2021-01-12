#Faça um programa para calcular e exibir o desconto de 
#IR conforme o valor do salário digitado pelo usuário 



salario = float(input("Digite o valor do seu salário: "))

if salario <= 1250:
    print(f'O valor do desconto IR é R$0')

elif salario > 1250 and salario <= 1900:
    ir = salario * 0.11
    print(f'O valor do desconto IR é de R${ir}')

elif salario > 1900 and salario <= 2700:
    ir = salario * 0.25
    print(f'O valor do desconto IR é de R${ir}')

elif salario > 2700:
    ir = salario * 0.275
    print(f'O valor do desconto IR é de R${ir}')