import math

def calcular_area_perimetro_rectangulo_y_circulos(r, a, b):
    area_rectangulo = a * b
    area_circulos = 2 * math.pi * r**2 
    perimetro_rectangulo = 2 * (a + b)
    perimetro_circulos = 2 * math.pi * r + 2 * a  
    area_total = area_rectangulo + area_circulos
    perimetro_total = perimetro_rectangulo + perimetro_circulos
    return area_total, perimetro_total



r = float(input("Ingrese el radio de los círculos (r): "))
a = float(input("Ingrese la longitud del rectángulo (a): "))
b = float(input("Ingrese la altura del rectángulo (b): "))

area_total, perimetro_total = calcular_area_perimetro_rectangulo_y_circulos(r, a, b)

print("El área total de la figura es:", area_total)
print("El perímetro total de la figura es:", perimetro_total)
