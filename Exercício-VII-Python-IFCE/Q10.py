# Programa para gerenciar uma conta bancária com operações de consulta, depósito e saque.
# Condições:
# • Solicitar o valor inicial do saldo da conta.
# • Oferecer três opções de operação:
#   1. Consultar saldo: Exibe o saldo atual.
#   2. Realizar depósito: Solicita o valor a ser depositado, adiciona ao saldo e exibe o saldo atualizado.
#   3. Realizar saque: Solicita o valor do saque, verifica se há saldo suficiente e, se houver, deduz o valor do saldo.
# • Caso não haja saldo suficiente para o saque, exibe uma mensagem de erro.

# Função para exibir o menu de opções
def exibir_menu():
    print("\nEscolha uma operação:")
    print("1. Consultar saldo")
    print("2. Realizar depósito")
    print("3. Realizar saque")
    print("4. Sair")

# Função para realizar a consulta do saldo
def consultar_saldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função para realizar o depósito
def realizar_deposito(saldo):
    valor = float(input("Digite o valor do depósito: R$ "))
    saldo += valor
    print(f"Depósito realizado com sucesso! Saldo atualizado: R$ {saldo:.2f}")
    return saldo

# Função para realizar o saque
def realizar_saque(saldo):
    valor = float(input("Digite o valor do saque: R$ "))
    if valor <= saldo:
        saldo -= valor
        print(f"Saque realizado com sucesso! Saldo atualizado: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente para o saque.")
    return saldo

# Solicitação do valor inicial do saldo
saldo_inicial = float(input("Digite o saldo inicial da conta: R$ "))
saldo = saldo_inicial

# Loop para o gerenciamento da conta
while True:
    exibir_menu()  # Exibe as opções para o usuário
    opcao = input("Escolha a opção desejada: ")

    # Verificação da opção escolhida
    match opcao:
        case "1":
            consultar_saldo(saldo)
        case "2":
            saldo = realizar_deposito(saldo)
        case "3":
            saldo = realizar_saque(saldo)
        case "4":
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida! Tente novamente.")
