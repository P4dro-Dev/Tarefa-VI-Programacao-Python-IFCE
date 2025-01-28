# Programa para calcular o valor final da passagem de transporte público com base no tipo de usuário.
# Condições:
# • Estudante: paga 50% do valor total da passagem.
# • Idoso: isento de pagamento.
# • Trabalhador: paga o valor integral.
# • Turista: paga o valor integral acrescido de uma taxa de serviço de 10%.
#
# Entrada: Valor base da passagem (float) e o tipo de usuário (string).
# Saída: Valor final da passagem com duas casas decimais.

# Leitura do valor base da passagem e do tipo de usuário
valor_base = float(input("Digite o valor base da passagem: "))
tipo_usuario = input("Digite o tipo de usuário (Estudante, Idoso, Trabalhador, Turista): ").strip().capitalize()

# Cálculo do valor final da passagem usando match-case
match tipo_usuario:
    case "Estudante":
        valor_final = valor_base * 0.5
    case "Idoso":
        valor_final = 0.0
    case "Trabalhador":
        valor_final = valor_base
    case "Turista":
        valor_final = valor_base * 1.1
    case _:
        valor_final = None
        print("Tipo de usuário inválido.")

# Exibição do valor final da passagem
if valor_final is not None:
    print(f"Valor da passagem: R$ {valor_final:.2f}")
