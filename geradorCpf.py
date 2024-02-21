# ALGORITIMO PARA VALIDAR CPF

import re

cpf = "746.824.890-70"
cpf_numbers = re.sub(r'[^0-9]', '', cpf)

if cpf_numbers[0]*len(cpf_numbers) == cpf_numbers:
    print("CPF invalido")
else:    
    nine_digits = cpf_numbers[:9]
    sum = 0
    multiplier = 10
    for number in nine_digits:
        multiplied_number = int(number) * multiplier
        sum += multiplied_number
        multiplier -= 1
    first_digit = (sum * 10) % 11
        
    # SEGUNDO DIGITO 
        
ten_digits = cpf_numbers[:10]
print(ten_digits)
sum = 0
multiplier = 11
for number in ten_digits:
    multiplied_number = int(number) * multiplier
    sum += multiplied_number
    multiplier -= 1
second_digit = (sum * 10) % 11
        
cpf_calculator_system = f'{nine_digits}{first_digit}{second_digit}'


if cpf_calculator_system == cpf_numbers:
    print(f'O CPF: {cpf_calculator_system}, é válido!')
else:
    print("CPF inválido")    