# Função para verificar semelhança usando o critério LAL (Lado-Ângulo-Lado)
# Recebe dois triângulos com dois lados e o ângulo entre eles
def verificar_lal(triangulo1, triangulo2):
    # Extrai os lados e o ângulo do primeiro e segundo triângulo
    lado1_t1, lado2_t1, angulo_t1 = triangulo1
    lado1_t2, lado2_t2, angulo_t2 = triangulo2
    
    # Verifica se os lados correspondentes são proporcionais e se os ângulos são congruentes
    proporcao_lados = (lado1_t1 / lado1_t2 == lado2_t1 / lado2_t2)
    angulos_congruentes = (angulo_t1 == angulo_t2)
    
    # Retorna True se os lados forem proporcionais e os ângulos congruentes, caso contrário False
    return proporcao_lados and angulos_congruentes

# Função para verificar semelhança usando o critério AA (Ângulo-Ângulo)
# Recebe dois triângulos com dois ângulos
def verificar_aa(triangulo1, triangulo2):
    # Extrai os dois ângulos do primeiro e segundo triângulo
    angulo1_t1, angulo2_t1 = triangulo1
    angulo1_t2, angulo2_t2 = triangulo2
    
    # Verifica se os ângulos correspondentes são congruentes
    return (angulo1_t1 == angulo1_t2) and (angulo2_t1 == angulo2_t2)

# Função para verificar semelhança usando o critério LLL (Lado-Lado-Lado)
# Recebe dois triângulos com três lados
def verificar_lll(triangulo1, triangulo2):
    # Extrai os três lados do primeiro e segundo triângulo
    lado1_t1, lado2_t1, lado3_t1 = triangulo1
    lado1_t2, lado2_t2, lado3_t2 = triangulo2
    
    # Verifica se os três lados correspondentes são proporcionais
    proporcao_lados = (lado1_t1 / lado1_t2 == lado2_t1 / lado2_t2 == lado3_t1 / lado3_t2)
    
    # Retorna True se os lados forem proporcionais, caso contrário False
    return proporcao_lados

# Função principal que coleta os dados dos dois triângulos e verifica a semelhança automaticamente
def verificar_semelhanca():
    # Solicita os dados do primeiro triângulo (3 lados e 2 ângulos)
    print("Insira os três lados e os dois ângulos do primeiro triângulo:")
    lado1_t1 = float(input("Lado 1 do triângulo 1: "))
    lado2_t1 = float(input("Lado 2 do triângulo 1: "))
    lado3_t1 = float(input("Lado 3 do triângulo 1: "))
    angulo1_t1 = float(input("Ângulo 1 do triângulo 1 (em graus): "))
    angulo2_t1 = float(input("Ângulo 2 do triângulo 1 (em graus): "))
    
    # Solicita os dados do segundo triângulo (3 lados e 2 ângulos)
    print("Insira os três lados e os dois ângulos do segundo triângulo:")
    lado1_t2 = float(input("Lado 1 do triângulo 2: "))
    lado2_t2 = float(input("Lado 2 do triângulo 2: "))
    lado3_t2 = float(input("Lado 3 do triângulo 2: "))
    angulo1_t2 = float(input("Ângulo 1 do triângulo 2 (em graus): "))
    angulo2_t2 = float(input("Ângulo 2 do triângulo 2 (em graus): "))
    
    # Agrupa os lados e ângulos dos dois triângulos
    triangulo1_lados = (lado1_t1, lado2_t1, lado3_t1)
    triangulo2_lados = (lado1_t2, lado2_t2, lado3_t2)
    
    triangulo1_angulos = (angulo1_t1, angulo2_t1)
    triangulo2_angulos = (angulo1_t2, angulo2_t2)

    # Verifica se os triângulos são semelhantes pelo critério LLL (Lado-Lado-Lado)
    if verificar_lll(triangulo1_lados, triangulo2_lados):
        print("Os triângulos são semelhantes pelo critério LLL (Lado-Lado-Lado).")
        return

    # Verifica se os triângulos são semelhantes pelo critério LAL (Lado-Ângulo-Lado)
    triangulo1_lal = (lado1_t1, lado2_t1, angulo1_t1)
    triangulo2_lal = (lado1_t2, lado2_t2, angulo1_t2)
    if verificar_lal(triangulo1_lal, triangulo2_lal):
        print("Os triângulos são semelhantes pelo critério LAL (Lado-Ângulo-Lado).")
        return

    # Verifica se os triângulos são semelhantes pelo critério AA (Ângulo-Ângulo)
    if verificar_aa(triangulo1_angulos, triangulo2_angulos):
        print("Os triângulos são semelhantes pelo critério AA (Ângulo-Ângulo).")
        return

    # Se nenhum critério for atendido, informa que os triângulos não são semelhantes
    print("Os triângulos não são semelhantes por nenhum dos critérios LAL, AA ou LLL.")

# Chama a função principal para iniciar a verificação
verificar_semelhanca()
