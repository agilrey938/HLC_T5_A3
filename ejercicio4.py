def calcular(lista_numeros):
    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros) if lista_numeros else 0
    return suma, promedio

numeros = [10, 20, 30]
suma, promedio = calcular(numeros)
print(f"Suma: {suma}, Promedio: {promedio}")