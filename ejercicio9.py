def promedio_y_mejor(estudiantes):
    
    suma_calificaciones = sum(estudiantes.values())
    numero_estudiantes = len(estudiantes)
    promedio = suma_calificaciones / numero_estudiantes
    
    mejor_estudiante = max(estudiantes, key=estudiantes.get)
    calificacion_maxima = estudiantes[mejor_estudiante]
    
    return f"Promedio: {promedio:.2f}, Mejor estudiante: {mejor_estudiante} con {calificacion_maxima}"

estudiantes = {'Juan': 7, 'Ana': 9, 'Pedro': 6}
resultado = promedio_y_mejor(estudiantes)
print(resultado)