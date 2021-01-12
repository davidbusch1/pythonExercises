#Faça um programa que simule uma calculadora com as quatro operações básicas (+, -, *, / ). 
#O programa deve solicitar ao usuário a entrada de dois operandos e da operação a ser executada,
#na forma de menu. Dependendo da opção escolhida, deve ser executada a operação solicitada e 
#escrito seu resultado. Utilize uma variável do tipo inteiro para armazenar a operação e utilize
#o comando caso para escolher a operação a ser executada a partir do operador.





num1, num2 = float(input("Entre com o primeiro número: ")), float(input("Entre com o segundo número: "))
op = int(input("***Escolha as operações***\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n "))

if op == 1:
    result = num1 + num2
    print(f'O resultado é {result}')

elif op == 2:
    result = num1 - num2
    print(f'O resultado é {result}')

elif op == 3:
    result = num1 * num2
    print(f'O resultado é {result}')

elif op == 4:
    result = num1 / num2
    print(f'O resultado é {result}')