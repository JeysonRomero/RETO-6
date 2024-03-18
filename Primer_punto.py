import math

def calcular_volumen(r1, r2, h):
    volumen = math.pi * h * ((r1**2 + r2**2 + r1 * r2) / 3)
    return volumen

def calcular_area_superficial(r1, r2, h):
    area_superficial = 2 * math.pi * ((r1 + r2) / 2) * (math.sqrt((r2 - r1)**2 + h**2)) + 2 * math.pi * r1**2 + 2 * math.pi * r2**2
    return area_superficial

r1 = float(input("Ingrese el radio de la base (r1): "))
r2 = float(input("Ingrese el radio del tope (r2): "))
h = float(input("Ingrese la altura (h): "))

volumen = calcular_volumen(r1, r2, h)
area_superficial = calcular_area_superficial(r1, r2, h)

print("El volumen del sólido de la imagen es:", volumen)
print("El área superficial del sólido de revolución es:", area_superficial)
