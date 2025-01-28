# Programa que informa a disponibilidade de um serviço com base no dia da semana.
# Condições:
# • De Segunda a Sexta-feira: "Atendimento disponível das 9h às 18h."
# • Sábado: "Atendimento disponível das 9h às 12h."
# • Domingo: "Serviço indisponível."
# • Qualquer dia inválido: "Dia da semana inválido."

# Entrada: Um texto representando o dia da semana.
# Saída: Uma mensagem indicando a disponibilidade do serviço.

# Leitura do dia da semana
dia_semana = input("Digite o dia da semana: ").strip().capitalize()

# Verificação da disponibilidade usando match-case
match dia_semana:
    case "Segunda-feira" | "Terça-feira" | "Quarta-feira" | "Quinta-feira" | "Sexta-feira":
        mensagem = "Atendimento disponível das 9h às 18h."
    case "Sábado":
        mensagem = "Atendimento disponível das 9h às 12h."
    case "Domingo":
        mensagem = "Serviço indisponível."
    case _:
        mensagem = "Dia da semana inválido."

# Exibindo a mensagem
print(mensagem)
