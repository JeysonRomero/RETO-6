def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    sorted_numeros = sorted(numeros)
    n = len(sorted_numeros)
    if n % 2 == 0:
        return (sorted_numeros[n//2 - 1] + sorted_numeros[n//2]) / 2
    else:
        return sorted_numeros[n//2]

def calcular_promedio_multiplicativo(numeros):
    producto = 1
    for num in numeros:
        producto *= num
    return producto ** (1 / len(numeros))

def ordenar_ascendentemente(numeros):
    return sorted(numeros)

def ordenar_descendentemente(numeros):
    return sorted(numeros, reverse=True)

def potencia_mayor_menor(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor

def raiz_cubica_menor(numeros):
    menor = min(numeros)
    return menor ** (1/3)

numeros = []
for i in range(5):
    numero = float(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(numero)

print("El promedio de los números es:", calcular_promedio(numeros))
print("La mediana de los números es:", calcular_mediana(numeros))
print("El promedio multiplicativo de los números es:", calcular_promedio_multiplicativo(numeros))
print("Los números ordenados de forma ascendente son:", ordenar_ascendentemente(numeros))
print("Los números ordenados de forma descendente son:", ordenar_descendentemente(numeros))
print("El resultado de elevar el mayor número al menor número es:", potencia_mayor_menor(numeros))
print("La raíz cúbica del menor número es:", raiz_cubica_menor(numeros))
