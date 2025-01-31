def duplicados(lista_palabras):
    return list(dict.fromkeys(lista_palabras))

entrada = ['hola', 'mundo', 'hola', 'python', 'mundo']
salida = duplicados(entrada)
print(salida)