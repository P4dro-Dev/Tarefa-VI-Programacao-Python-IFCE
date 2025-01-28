# Nome: Pedro Henrique Sousa
# Curso: Técnioo em Informática | IFCE
# Disciplina: Programação
# Professora: Raquel 

# Programa para calcular o peso de uma pessoa em outro planeta com base no peso na Terra e no ID do planeta.
# Fórmula: Peso_planeta_escolhido = peso_terra / 10.0 * gravidade_planeta_escolhido
# ID Planeta      Gravidade
# 1  Mercúrio     0,37
# 2  Vênus        0,88
# 3  Marte        0,38
# 4  Júpiter      2,64
# 5  Saturno      1,15

# Entrada: Um número inteiro para o ID do planeta e um número fracionário para o peso na Terra.
# Saída: O peso equivalente no planeta escolhido com duas casas decimais.

# Leitura da entrada
id_planeta = int(input("Digite o ID do planeta (1 a 5): "))
peso_terra = float(input("Digite o peso na Terra (kg): "))

# Calculando o peso no planeta escolhido
match id_planeta:
    case 1:
        gravidade = 0.37  # Mercúrio
    case 2:
        gravidade = 0.88  # Vênus
    case 3:
        gravidade = 0.38  # Marte
    case 4:
        gravidade = 2.64  # Júpiter
    case 5:
        gravidade = 1.15  # Saturno
    case _:
        gravidade = None
        print("ID do planeta inválido!")

# Exibindo o resultado
if gravidade is not None:
    peso_planeta = peso_terra / 10.0 * gravidade
    print(f"Peso no planeta escolhido: {peso_planeta:.2f} kg")

