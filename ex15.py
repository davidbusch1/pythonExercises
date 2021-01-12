#Faça um programa que leia três valores que representam os 
#lados de um triângulo. Primeiramente, verifique se os lados podem formar um 
#triângulo ( a soma de dois lados não pode ser menor que o terceiro lado ). 
#Caso possa formar um triângulo, indique se este é equilátero, isósceles ou escaleno.





l1,l2,l3 = float(input("Entre com o valor do lado 1: ")), float(input("Entre com o valor do lado 2: ")), float(input("Entre com o valor do lado 3: "))

while l1 + l2 < l3:
    print(f'Os valores indicados não podem formar um triângulo, tente novamente...\n')
    l1, l2, l3 = float(input("Entre com o valor do lado 1: ")), float(input("Entre com o valor do lado 2: ")), float(input("Entre com o valor do lado 3: "))

if l1 == l2 == l3:
    print(f'Este triângulo é equilátero.')

if l1 == l2:
    print(f'Este triângulo é isósceles.')

if l1 != l2 != l3:
    print(f'Este triângulo é escaleno.')