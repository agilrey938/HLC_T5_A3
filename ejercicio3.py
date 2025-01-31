def diccionario():
    diccionario = {numero: numero ** 2 for numero in range(1, 6)}
    return diccionario

resultado = diccionario()
print(resultado)