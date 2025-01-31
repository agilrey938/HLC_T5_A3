def divisores(num):
    lista_divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            lista_divisores.append(i)
    return lista_divisores

numero = 12
resultado = divisores(numero)
print(resultado)