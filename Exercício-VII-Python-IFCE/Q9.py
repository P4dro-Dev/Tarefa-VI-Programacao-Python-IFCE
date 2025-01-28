# Programa para calcular a mensalidade de uma academia com base na categoria do cliente e no plano escolhido.
# Condições:
# • Categoria Estudante ou Idoso:
#   - Plano Básico: R$ 50
#   - Plano Premium: R$ 70
# • Categoria Convencional:
#   - Plano Básico: R$ 80
#   - Plano Premium: R$ 120
# Caso a categoria ou plano sejam inválidos, o programa exibe uma mensagem de erro.
#
# Entrada: Categoria do cliente (string) e plano escolhido (string).
# Saída: Mensalidade ou mensagem de erro.

# Leitura da categoria e plano
categoria = input("Digite a categoria (Estudante, Idoso ou Convencional): ").strip().capitalize()
plano = input("Digite o plano (Básico ou Premium): ").strip().capitalize()

# Cálculo da mensalidade usando match-case
match categoria:
    case "Estudante" | "Idoso":
        match plano:
            case "Básico":
                mensalidade = 50
            case "Premium":
                mensalidade = 70
            case _:
                mensalidade = None
                print("Plano inválido!")
    case "Convencional":
        match plano:
            case "Básico":
                mensalidade = 80
            case "Premium":
                mensalidade = 120
            case _:
                mensalidade = None
                print("Plano inválido!")
    case _:
        mensalidade = None
        print("Categoria inválida!")

# Exibição da mensalidade, caso seja válida
if mensalidade is not None:
    print(f"Mensalidade: R$ {mensalidade:.2f}")
