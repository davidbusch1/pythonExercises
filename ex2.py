#Faça um programa para calcular e exibir a porcentagem
#de comissão de vendas de um vendedor, conforme o volume
#mensal de vendas do mesmo digitado pelo usuário 




vendas = float(input("Digite o valor de vendas: "))

if vendas <= 5000:
    comissao = vendas * 0.02
    print(f'O valor da sua comisão é de {comissao}.')

elif vendas > 5000 and vendas <= 10000:
    comissao = vendas * 0.05
    print(f'O valor da sua comisão é de {comissao}.')

elif vendas > 10000 and vendas <= 15000:
    comissao = vendas * 0.07
    print(f'O valor da sua comisão é de {comissao}.')

elif vendas > 15000:
    comissao = vendas * 0.09
    print(f'O valor da sua comisão é de {comissao}.')