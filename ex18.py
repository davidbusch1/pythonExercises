#Efetuar a leitura de dois valores numéricos inteiros 
#representados pelas variáveis A e B e apresentar o resultado 
#da diferença do maior valor pelo menor.



A, B = float(input("Entre com um número: ")), float(input("Entre com outro número: "))

if A > B:
    x = A - B
    print(f'A diferença entre o maior número e o menor é {x}')
else:
    x = B - A
    print(f'A diferença entre o maior número e o menor é {x}')