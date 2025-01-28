# Programa para calcular o preço de venda de um automóvel com base no tipo do automóvel e no preço de fábrica.
# Condições:
# O preço de venda é a soma do preço de fábrica mais uma taxa de lucro, calculada a partir do tipo do automóvel:
# ID Tipo                     Taxa
# 1 Passeio                  20%
# 2 Esportivo                25%
# 3 Transporte coletivo      15%
# 4 Carga                    30%
# 5 Outros                   40%
#
# Entrada: Um número inteiro (tipo do automóvel) e um número real (preço de fábrica).
# Saída: O preço de venda do automóvel com duas casas decimais.

# Leitura do tipo do automóvel e do preço de fábrica
tipo_automovel = int(input("Digite o tipo do automóvel (1 a 5): "))
preco_fabrica = float(input("Digite o preço de fábrica: "))

