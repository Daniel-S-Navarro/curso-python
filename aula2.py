lista = ["Maria", "Helena", "Luiz"]
lista.append("Mario")

contador = 0
    
while contador < len(lista):
    
    for nome in lista:
        print(f'{nome}: {contador}')
    
        contador = contador + 1

print() 