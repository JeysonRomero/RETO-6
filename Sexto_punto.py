def calcular_contagiados(C, D):
    contagiados_totales = C * (2 ** D)
    return contagiados_totales


C = int(input("Ingrese el número actual de contagiados: "))
D = int(input("Ingrese el número de días a partir de hoy: "))

contagiados_totales = calcular_contagiados(C, D)

print("El número total de contagiados después de", D, "días será de:", contagiados_totales)
