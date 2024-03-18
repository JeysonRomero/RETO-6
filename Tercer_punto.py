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
