#Faça um programa que leia as repostas de três questões de 
#múltipla escolha (a, b, c, d). Em seguida, leia o gabarito 
#dessas questões, ou seja, as respostas corretas. Depois, 
#compare as respostas dadas com as do gabarito e indique quantas respostas estão corretas




gabarito = ['a', 'b', 'c']
r1,r2,r3 = input("Digite a resposta da questão 1: "),input("Digite a resposta da questão 2: "),input("Digite a resposta da questão 3: ")
cont = 0
if r1 == gabarito[0]:
   cont += 1
if r2 == gabarito[1]:
    cont += 1
if r3 == gabarito[2]:
    cont+= 1

print(f'A quantidade de questões acertadas foi: {cont}!')