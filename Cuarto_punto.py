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
