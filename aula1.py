# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """

numero_inteiro = input("Digite um numero inteiro: ")

if numero_inteiro.isdigit() :
    par_impar = int(numero_inteiro) % 2
    
    if par_impar == 0:
        print("Numero par")
    else:
        print("Numero impar")    
else:   
    print("Esse não é um numero inteiro")


# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.410
# """

entrada = input("Que horas são: ")

if entrada.isdigit():
    if entrada >= 0 and entrada <=11:
        print("Bom dia!")
    elif entrada >= 12 and entrada <=17:
        print("Boa tarde!")
    elif entrada >= 18 and entrada <= 23 :
        print("Boa noite!")       
    else:
        print("Hora invalida!")
else:
    print("Digite uma hora por favor!")   
    


# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 


nome = input("Digite seu nome: ") 

if nome:
    if len(nome) <= 4:
        print("Seu nome é curto")
    elif  (len(nome) == 5) or (len(nome) == 6): 
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Favor digite um nome!")  
          