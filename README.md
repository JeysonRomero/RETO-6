# RETO-6

<br>

### 1. Dada la figura de la imagen,desarrolle

<br>

![image](https://github.com/JeysonRomero/RETO-6/assets/159095091/707ee1ba-6199-4656-8f4e-29cb92903c75)

<br>

-Una función matemática para calcular el volumen y el área superficial.

-Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

-Revise como utilizar el valor de pi usando import math y math.pi

<br>

```
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
```

<br>
el valor  de π se utiliza mediante la importación del módulo math de Python y accediendo a la constante math.pi.use este codigo ya que  los cálculos del volumen y el área superficial implican el uso de π  que están relacionados con formas geométricas circulares, como círculos y cilindros. Al utilizar math.pi,obteniendo  un valor confiable y preciso para π, lo que garantiza que los cálculos sean precisos y correctos.
