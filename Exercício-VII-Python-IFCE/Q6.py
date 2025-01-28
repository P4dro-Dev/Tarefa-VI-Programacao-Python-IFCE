# Programa para exibir um cardápio de cinco opções de pratos e calcular o valor total do pedido.
# Condições:
# O usuário escolhe o prato digitando o número correspondente e a quantidade.
# O programa exibe o nome do prato selecionado e o valor a pagar.
# Caso o usuário selecione uma opção inválida, exibe uma mensagem de erro.
#
# ID    Prato        Valor
# 1     Pizza        R$ 40,00
# 2     Hambúrguer   R$ 15,00
# 3     Salada       R$ 20,00
# 4     Lasanha      R$ 30,00
# 5     Sushi        R$ 50,00

# Exibindo o cardápio
print("----- Cardápio -----")
print("1 - Pizza (R$ 40,00)")
print("2 - Hambúrguer (R$ 15,00)")
print("3 - Salada (R$ 20,00)")
print("4 - Lasanha (R$ 30,00)")
print("5 - Sushi (R$ 50,00)")

# Leitura da escolha do usuário
id_prato = int(input("Escolha o prato (1 a 5): "))
quantidade = int(input("Digite a quantidade: "))

# Verificação do prato escolhido usando match-case
match id_prato:
    case 1:
        nome_prato = "Pizza"
        preco_unitario = 40.00
    case 2:
        nome_prato = "Hambúrguer"
        preco_unitario = 15.00
    case 3:
        nome_prato = "Salada"
        preco_unitario = 20.00
    case 4:
        nome_prato = "Lasanha"
        preco_unitario = 30.00
    case 5:
        nome_prato = "Sushi"
        preco_unitario = 50.00
    case _:
        nome_prato = None
        print("Opção inválida!")

# Cálculo e exibição do valor a pagar
if nome_prato is not None:
    valor_total = preco_unitario * quantidade
    print(f"Você selecionou: {nome_prato}")
    print(f"Valor a pagar: R$ {valor_total:.2f}")
