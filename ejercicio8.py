def v_c(texto):
    vocales = 'aeiouáéíóúüAEIOUÁÉÍÓÚÜ'
    consonantes = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
    contar = {'vocales': 0, 'consonantes': 0}
    
    for caracter in texto:
        if caracter in vocales:
            contar['vocales'] += 1
        elif caracter in consonantes:
            contar['consonantes'] += 1
    
    return contar

texto = 'hola mundo'
resultado = v_c(texto)
print(resultado)