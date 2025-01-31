def eliminar(lista_numeros):
    sin_pares = [num for num in lista_numeros if num % 2 != 0]
    return sin_pares

numeros = [1, 2, 3, 4, 5, 6]
resultado = eliminar(numeros)
print(resultado)