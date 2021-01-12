#Faça um programa para calcular e exibir a valor do imposto de 
#ISS de uma nota fiscal de serviços, conforme o valor total de 
#serviços especificado na mesma digitado pelo usuário 





servicos = float(input("Entre com o valor total de serviços na nota fiscal: "))

if servicos <= 5000:
    imposto = servicos * 0.04
    print(f'O valor do imposto ISS sobre a nota é ed R${imposto}')

elif servicos > 5000 and servicos <= 10000:
    imposto = servicos * 0.06
    print(f'O valor do imposto ISS sobre a nota é ed R${imposto}')

elif servicos > 10000 and servicos <= 20000:
    imposto = servicos * 0.13
    print(f'O valor do imposto ISS sobre a nota é ed R${imposto}')

elif servicos > 20000:
    imposto = servicos * 0.16
    print(f'O valor do imposto ISS sobre a nota é ed R${imposto}')