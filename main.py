# Recebe os valores dos lados do triângulo
lado1 = input("Digite o valor do primeiro lado: ")
lado2 = input("Digite o valor do segundo lado: ")
lado3 = input("Digite o valor do terceiro lado: ")

# Estrutura de decisão responsável por retorar ao usuário qual é o tipo de triângulo mediante aos valores recebidos nas variáveis
if lado1 == lado2 and lado1 == lado3:
    print("Devido aos 3 lados serem iguais, o triângulo é equilátero")
elif lado1 == lado2 or lado1 == lado3:
    print("Devido a apenas 2 lados serem iguais, o triângulo é isósceles")
elif lado2 == lado1 or lado2 == lado3:
    print("Devido a apenas 2 lados serem iguais, o triângulo é isósceles")
elif lado3 == lado1 or lado3 == lado2:
    print("Devido a apenas 2 lados serem iguais, o triângulo é isósceles")
elif lado1 != lado2 and lado1 != lado3:
    print("Devido aos 3 lados serem diferentes, o triângulo é escaleno")
