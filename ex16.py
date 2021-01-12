#Dado um ano d.C. (depois de Cristo), identifique se este é um ano bissexto ou não




ano = int(input("Entre com o ano: "))

if ano % 4 == 0:
    print(f'O ano é bissexto.')
else:
    print(f'O ano não é bissexto.')