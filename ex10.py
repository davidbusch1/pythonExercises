#Faça um programa para calcular e exibir a categoria do nadador, dado a sua idade.
#infantil A	de 5 a 8 anos
#infantil B	de 8 a 10 anos
#juvenil A	de 11 a 13 anos
#juvenil B	de 14 a 17 anos
#senior	maiores de 17 anos





idade = int(input("Entre com a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print(f'A categoria indicada para esse nadador é: Infantil A')

if idade >= 8 and idade <= 10:
    print(f'A categoria indicada para esse nadador é: Infantil B')

if idade >= 11  and idade <= 13:
    print(f'A categoria indicada para esse nadador é: Juvenil A')

if idade >= 14 and idade <= 17:
    print(f'A categoria indicada para esse nadador é: Juvenil B')

if idade > 17:
    print(f'A categoria indicada para esse nadador é: senior')
