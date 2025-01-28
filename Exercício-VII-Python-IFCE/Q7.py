# Programa para calcular o valor do frete de um pedido com base no valor total da compra e na região de entrega.
# Condições:
# • Se o valor do pedido for maior ou igual a R$ 200, o frete é gratuito para qualquer região.
# • Caso contrário:
#   o Para a região Sudeste, o frete é R$ 20.
#   o Para a região Nordeste, o frete é R$ 30.
#   o Para outras regiões (Sul, Norte ou Centro-Oeste), o frete é R$ 50.
#   o Se a região não for válida, o programa exibe uma mensagem de erro.
#
# Entrada: Valor total da compra (float) e região de entrega (string).
# Saída: Valor do frete ou mensagem de erro.

# Leitura do valor total da compra e da região de entrega
valor_pedido = float(input("Digite o valor total da compra: "))
regiao = input("Digite a região de entrega (Sudeste, Nordeste, Sul, Norte ou Centro-Oeste): ").strip().capitalize()

# Cálculo do valor do frete usando match-case
if valor_pedido >= 200:
    frete = 0.0
else:
    match regiao:
        case "Sudeste":
            frete = 20.0
        case
