numero_1 = input("Digite um numero: ")
numero_2 = input("Digite outro numero: ")
operador = input("Digite o operador matemático: ")



    
if operador == "-" :
    subtracao = numero_1 - numero_2
    print(f'O resultado é {subtracao}')
elif operador == "*" :
    multiplicacao = numero_1 * numero_2
    print(f'O resultado é {multiplicacao}')
elif operador == "/" :
    divisao = numero_1 // numero_2
    print(f'O resultado é {divisao}')
else :        
    soma = numero_1 + numero_2
    print(f'O resultado é {soma}')
        
