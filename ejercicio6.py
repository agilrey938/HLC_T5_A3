def lp(lista_palabras):
    diccionario = {}
    for palabra in lista_palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

lista = ['gato', 'perro', 'elefante']
resultado = lp(lista)
print(resultado)  