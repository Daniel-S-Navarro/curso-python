# ALGORITIMO PARA VALIDAR CPF

import re

cpf = "746.824.890-70"
cpf_so_numeros = re.sub(r'[^0-9]', '', cpf)

if cpf_so_numeros[0]*len(cpf_so_numeros) == cpf_so_numeros:
    print("CPF invalido")
else:    
    nove_digitos = cpf_so_numeros[:9]
    soma = 0
    multiplicador = 10
    for numero in nove_digitos:
        numero_multiplicado = int(numero) * multiplicador
        soma += numero_multiplicado
        multiplicador -= 1
    primeiro_digito = (soma * 10) % 11
        
    # SEGUNDO DIGITO 
        
dez_digitos = cpf_so_numeros[:10]
print(dez_digitos)
soma = 0
multiplicador = 11
for numero in dez_digitos:
    numero_multiplicado = int(numero) * multiplicador
    soma += numero_multiplicado
    multiplicador -= 1
segundo_digito = (soma * 10) % 11
        
cpf_calculado_sistema = f'{nove_digitos}{primeiro_digito}{segundo_digito}'


if cpf_calculado_sistema == cpf_so_numeros:
    print(f'O CPF: {cpf_calculado_sistema}, é válido!')
else:
    print("CPF inválido")    