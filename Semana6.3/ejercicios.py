# Ejercicio 1
numeros = [9, 12, 9]

def sumar_lista(numeros):
    suma_de_numeros = 0
    for numero in numeros:
        suma_de_numeros += numero
    return suma_de_numeros

print(sumar_lista(numeros))


# Ejercicio 2
calificaciones = [96, 81, 100]

def calcular_promedio(calificaciones):
    suma_de_notas = 0
    contador = 0
    for nota in calificaciones:
        suma_de_notas += nota
        contador += 1
    return (suma_de_notas/contador)

print(calcular_promedio(calificaciones))


# Ejercicio 3
numeros = [1, 2, 3, -4]

def filtrar_positivos(numeros):
    positivos = []
    for numero in numeros:
        if numero > 0:
            positivos.append(numero)
    return positivos

print(filtrar_positivos(numeros))


# Ejercicio 4
numeros = [2, 4, 7, 1, 90]

def obtener_mayor(numeros):
    mayor = 0
    for numero in numeros:
        if numero > 0:
            mayor = numero

    return mayor

print(obtener_mayor(numeros))


# Ejercicio 5
numeros = [2, 34, 5, 7, 8, 91]

def contar_pares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador += 1
    return contador

print(contar_pares(numeros))


# Ejercicio 6
numeros = [1, 1, 3, 7, 4, 6, 7, 9, 9]

prueba = [4, 7, 100, 4, 5.6, 230, 7]

def eliminar_duplicados(numeros):
    for numero in numeros:
        contador = 0
        for numero1 in numeros:
            if numero1 == numero:
                contador += 1
                if contador > 1:
                    numeros.remove(numero1)
    return numeros

print(eliminar_duplicados(numeros))
print(eliminar_duplicados(prueba))


# Ejercicio 7
# Ejercicio 8
# Ejercicio 9
# Ejercicio 10