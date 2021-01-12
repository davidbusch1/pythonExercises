#Efetuar a leitura de um valor numérico inteiro positivo ou negativo 
#representado pela variável N e apresentar o valor lido como sendo positivo. 



N = float(input("Entre com um número: "))

if N < 0:
    x = N * (-1)
    print(f'O valor do número é {x}')
else:
    print(f'O valor do número é {N}')