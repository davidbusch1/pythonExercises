#Questão 7. Faça um programa para calcular e exibir o 
#valor dos juros de um empréstimo bancário, conforme o 
#valor emprestado e o número de parcelas digitado pelo usuário 




valor, parcela = float(input("Entre com o valor do empréstimo: ")), int(input("Entre com a quantidade de parcelas: "))

if parcela <= 3:
    juros = valor * 0.06
    print(f'O valor do juros sobre o empréstimo é de R${juros}')

elif parcela > 3 and parcela <= 6:
    juros = valor * 0.09
    print(f'O valor do juros sobre o empréstimo é de R${juros}')

elif parcela > 6 and parcela <= 12:
    juros = valor * 0.22
    print(f'O valor do juros sobre o empréstimo é de R${juros}')

elif parcela > 12:
    juros = valor * 0.34
    print(f'O valor do juros sobre o empréstimo é de R${juros}')