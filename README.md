# RETO-6

<br>

### 1. Dada la figura de la imagen,desarrolle

<br>

![image](https://github.com/JeysonRomero/RETO-6/assets/159095091/707ee1ba-6199-4656-8f4e-29cb92903c75)

<br>

### -Una función matemática para calcular el volumen y el área superficial.

### -Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

### -Revise como utilizar el valor de pi usando import math y math.pi

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


<br>


### 2.Dado la figura de la imagen, desarrolle:

<br>

![image](https://github.com/JeysonRomero/RETO-6/assets/159095091/1edf5a34-b6f2-4d93-8a8c-ad7a6bf25954)

<br>

### -Una función matemática para calcular el área y el perimetro.

### -Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.

### -Revise como utilizar el valor de pi usando import math y math.pi

<br>

```
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

```
math.pi se utilizo en este codigo para acceder al valor preciso de π proporcionado por el módulo math, asegurando así cálculos precisos para el área y el perímetro de la figura .

<br>


### 3.Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

<br>

```
def calcular_cantidad_carne_avicola(N, M, K):
  
    peso_gallina = 6  # kilogramos
    peso_gallo = 7    # kilogramos
    peso_pollito = 1  # kilogramos
    
    
    total_carne_avicola = (N * peso_gallina) + (M * peso_gallo) + (K * peso_pollito)
    
    return total_carne_avicola


N = int(input("Ingrese el número de gallinas: "))
M = int(input("Ingrese el número de gallos: "))
K = int(input("Ingrese el número de pollitos: "))

cantidad_carne_avicola = calcular_cantidad_carne_avicola(N, M, K)
print("La cantidad total de carne de aves es:", cantidad_carne_avicola, "kilogramos")


```

<br>

### 4.Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

<br>

```
def calcular_vueltas(P, M, H, B):
    
    precio_pan = 300
    precio_leche = 3300
    precio_huevo = 350
    
    costo_total = P * precio_pan + M * precio_leche + H * precio_huevo
    

    vueltas = B - costo_total
    
    return vueltas

P = int(input("Ingrese la cantidad de panes a comprar: "))
M = int(input("Ingrese la cantidad de bolsas de leche a comprar: "))
H = int(input("Ingrese la cantidad de huevos a comprar: "))
B = int(input("Ingrese el valor del billete entregado: "))


vueltas = calcular_vueltas(P, M, H, B)

if vueltas >= 0:
    print("Las vueltas son:", vueltas)
else:
    print("Queda debiendo:", abs(vueltas))


```

### 5.Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

<br>

```
def calcular_valor_prestamo(C, i, n):
    M = C * (1 + i / 100) ** n
    return M


C = float(input("Ingrese el monto del préstamo: "))
i = float(input("Ingrese la tasa de interés anual (%): "))
n = int(input("Ingrese el número de meses: "))


valor_prestamo = calcular_valor_prestamo(C, i, n)


print("El valor del préstamo después de", n, "meses es:", valor_prestamo)

```

<br>

### 6.El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C

<br>

```
def calcular_contagiados(C, D):
    contagiados_totales = C * (2 ** D)
    return contagiados_totales


C = int(input("Ingrese el número actual de contagiados: "))
D = int(input("Ingrese el número de días a partir de hoy: "))

contagiados_totales = calcular_contagiados(C, D)

print("El número total de contagiados después de", D, "días será de:", contagiados_totales)

```

<br>

### 7.Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

### -El promedio

### -La mediana

### -El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)

### -Ordenar los números de forma ascendente

### -Ordenar los números de forma descendente

### -La potencia del mayor número elevado al menor número

### -La raíz cúbica del menor número

<br>

```
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

```

<br>

### 8.Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso

<br>

### 9.Consultar qué es y cómo funciona pip en python.

<br>

### ¿Que es?

PIP es el administrador de paquetes de Python, que se utiliza para instalar, actualizar y administrar paquetes y módulos de Python. PIP es una sigla recursiva que significa "PIP Installs Packages" (PIP Instala Paquetes). Es una herramienta fundamental para el desarrollo de software en Python, ya que facilita la instalación de bibliotecas y paquetes de terceros que no vienen incluidos en la distribución estándar de Python.

### ¿Como funciona?

Instalación de PIP: En versiones recientes de Python (después de la 3.4), PIP suele venir preinstalado. Sin embargo, en caso de que no esté instalado, se puede instalar fácilmente. Para instalar PIP, normalmente se utiliza el instalador de paquetes del sistema operativo o se puede instalar manualmente utilizando scripts proporcionados por Python.

Instalación de paquetes: Una vez que PIP está instalado, se puede utilizar para instalar paquetes de Python desde el repositorio PyPI (Python Package Index) o desde otros repositorios. Para instalar un paquete, se utiliza el comando pip install nombre_del_paquete. Por ejemplo, para instalar el paquete requests, se ejecutaría pip install requests.

Actualización de paquetes: PIP también se utiliza para actualizar paquetes a versiones más recientes. Para actualizar un paquete, se utiliza el comando pip install --upgrade nombre_del_paquete.

Desinstalación de paquetes: Si ya no se necesita un paquete, se puede desinstalar utilizando el comando pip uninstall nombre_del_paquete.

Requisitos de instalación: PIP también puede leer archivos de requisitos (por lo general, archivos con extensión .txt) que especifican los paquetes y las versiones que se necesitan para un proyecto. Esto facilita la instalación de todos los paquetes necesarios con un solo comando.

Entornos virtuales: PIP se utiliza comúnmente en conjunción con entornos virtuales para aislar las dependencias de diferentes proyectos. Los entornos virtuales permiten tener diferentes conjuntos de paquetes instalados en cada proyecto, lo que evita conflictos de dependencias entre ellos.










