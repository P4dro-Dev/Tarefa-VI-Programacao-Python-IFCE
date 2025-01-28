# Programa para calcular a multa de um motorista com base na velocidade registrada.
# Condições:
# - Solicite a velocidade máxima da avenida, a velocidade do carro e a área de trânsito.
# - Multas:
#   - Dentro do limite: "Sem multa."
#   - Até 20 km/h acima do limite:
#     * Área escolar: R$ 200.
#     * Caso contrário: R$ 100.
#   - Acima de 20 km/h do limite:
#     * Área escolar: R$ 500.
#     * Caso contrário: R$ 300.
#
# Entrada: Velocidade máxima (int), velocidade registrada (int) e área de trânsito (string).
# Saída: Mensagem indicando a multa ou ausência dela.

# Leitura dos dados
velocidade_maxima = int(input("Digite a velocidade máxima da avenida (km/h): "))
velocidade_registrada = int(input("Digite a velocidade registrada do carro (km/h): "))
area = input("Digite a área de trânsito (Escolar ou Normal): ").strip().capitalize()

# Cálculo da diferença de velocidade
excesso_velocidade = velocidade_registrada - velocidade_maxima

# Determinação da multa usando match-case
if excesso_velocidade <= 0:
    print("Sem multa.")
else:
    match excesso_velocidade:
        case excesso if 0 < excesso <= 20:
            if area == "Escolar":
                multa = 200
            else:
                multa = 100
        case excesso if excesso > 20:
            if area == "Escolar":
                multa = 500
            else:
                multa = 300
        case _:
            multa = 0  # Caso padrão, para segurança (não esperado).
    print(f"Multa: R$ {multa:.2f}")

