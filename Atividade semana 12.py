def verificar_lal(triangulo1, triangulo2):
    lado1_t1, lado2_t1, angulo_t1 = triangulo1
    lado1_t2, lado2_t2, angulo_t2 = triangulo2
    
    proporcao_lados = (lado1_t1 / lado1_t2 == lado2_t1 / lado2_t2)
    angulos_congruentes = (angulo_t1 == angulo_t2)
    
    return proporcao_lados and angulos_congruentes

def verificar_aa(triangulo1, triangulo2):
    angulo1_t1, angulo2_t1 = triangulo1
    angulo1_t2, angulo2_t2 = triangulo2
    
    return (angulo1_t1 == angulo1_t2) and (angulo2_t1 == angulo2_t2)

def verificar_lll(triangulo1, triangulo2):
    lado1_t1, lado2_t1, lado3_t1 = triangulo1
    lado1_t2, lado2_t2, lado3_t2 = triangulo2
    
    proporcao_lados = (lado1_t1 / lado1_t2 == lado2_t1 / lado2_t2 == lado3_t1 / lado3_t2)
    
    return proporcao_lados

def verificar_semelhanca():
    print("Insira os três lados e os dois ângulos do primeiro triângulo:")
    lado1_t1 = float(input("Lado 1 do triângulo 1: "))
    lado2_t1 = float(input("Lado 2 do triângulo 1: "))
    lado3_t1 = float(input("Lado 3 do triângulo 1: "))
    angulo1_t1 = float(input("Ângulo 1 do triângulo 1 (em graus): "))
    angulo2_t1 = float(input("Ângulo 2 do triângulo 1 (em graus): "))
    
    print("Insira os três lados e os dois ângulos do segundo triângulo:")
    lado1_t2 = float(input("Lado 1 do triângulo 2: "))
    lado2_t2 = float(input("Lado 2 do triângulo 2: "))
    lado3_t2 = float(input("Lado 3 do triângulo 2: "))
    angulo1_t2 = float(input("Ângulo 1 do triângulo 2 (em graus): "))
    angulo2_t2 = float(input("Ângulo 2 do triângulo 2 (em graus): "))
    
    triangulo1_lados = (lado1_t1, lado2_t1, lado3_t1)
    triangulo2_lados = (lado1_t2, lado2_t2, lado3_t2)
    
    triangulo1_angulos = (angulo1_t1, angulo2_t1)
    triangulo2_angulos = (angulo1_t2, angulo2_t2)

    if verificar_lll(triangulo1_lados, triangulo2_lados):
        print("Os triângulos são semelhantes pelo critério LLL (Lado-Lado-Lado).")
        return

    triangulo1_lal = (lado1_t1, lado2_t1, angulo1_t1)
    triangulo2_lal = (lado1_t2, lado2_t2, angulo1_t2)
    if verificar_lal(triangulo1_lal, triangulo2_lal):
        print("Os triângulos são semelhantes pelo critério LAL (Lado-Ângulo-Lado).")
        return

    if verificar_aa(triangulo1_angulos, triangulo2_angulos):
        print("Os triângulos são semelhantes pelo critério AA (Ângulo-Ângulo).")
        return

    print("Os triângulos não são semelhantes por nenhum dos critérios LAL, AA ou LLL.")

verificar_semelhanca()
