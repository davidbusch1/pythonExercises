#Faça um programa que calcule o IMC de uma pessoa 
#(IMC = massa em kg / altura em metros elevado ao quadrado) 
#e informe a sua classificação segundo a tabela a seguir:
#Menor que 17.0	Muito abaixo do peso
#De 17.0 a 18.50	Abaixo do peso
#De 18.50 a 25.0	Peso normal
#De 25.0 a 30.0	Acima do peso
#De 30.0 a 35.0	Obesidade I
#De 35.0 a 40.0	Obesidade II
#Acima de 40.0	Obesidade III (mórbida)




massa, alt = float(input("Entre com sua massa em quilos: ")), float(input("Entre com sua altura em metros: "))

imc = massa/(alt ** 2)

if imc < 17.0:
    print(f'Você está muito abaixo do peso.')

elif imc > 17.0 and imc < 18.5:
    print(f'Você está abaixo do peso.')

elif imc >= 18.5 and imc < 25.0:
    print(f'Você está com peso normal.')

elif imc >= 25.0 and imc < 30.0:
    print(f'Você está acima do peso.')

elif imc >= 30.0 and imc < 35.0:
    print(f'Você está com obesidade I.')

elif imc >= 35.0 and imc < 40.0:
    print(f'Você está com obesidade II.')

elif imc > 40.0:
    print(f'Você está com obesidade III (mórbida).')