#Faça um programa para calcular e exibir a valor
#do imposto de ICMS de um produto, conforme a classificação
#do tipo de produto e do valor de custo do mesmo digitado pelo usuário 
#Cesta básica	isento
#Eletrônicos	25%
#Serviços	18%
#Os demais produtos	12%



clas, valor = int(input("Digite a classificação do produto:\n1 para cesta basica\n2 para eletronicos\n3 para serviços\n4 para demais produtos: ")), float(input("Digite o valor de custo do produto: "))

if clas == 1:
    float(valor)
    print(f'O valor do imposto de ICMS sobre seu produto é de {valor}')

elif clas == 2:
    imposto = valor * 0.25
    float(imposto)
    print(f'O valor do imposto de ICMS sobre seu produto é de {imposto}')

elif clas == 3:
    imposto = valor * 0.18
    float(imposto)
    print(f'O valor do imposto de ICMS sobre seu produto é de {imposto}')

elif clas == 4:
    imposto = valor * 0.12
    float(imposto)
    print(f'O valor do imposto de ICMS sobre seu produto é de {imposto}')