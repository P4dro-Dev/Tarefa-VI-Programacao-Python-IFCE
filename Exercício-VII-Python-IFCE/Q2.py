# Desenvolva um programa que leia o código de um determinado produto e mostre sua classificação.
# Utilize a seguinte tabela como referência:
# Código               Classificação
# 1                    Alimento não-perecível
# 2, 3 ou 4            Alimento perecível
# 5 ou 6               Vestuário
# 7                    Higiene pessoal
# 8, 9 ou 10           Limpeza e utensílios domésticos
# Qualquer outro código Código inválido

# Entrada: Um número inteiro correspondendo ao código de um produto.
# Saída: A classificação do produto, conforme a tabela apresentada.

# Leitura do código do produto
codigo = int(input("Digite o código do produto: "))

# Verificação da classificação usando match-case
match codigo:
    case 1:
        classificacao = "Alimento não-perecível"
    case 2 | 3 | 4:
        classificacao = "Alimento perecível"
    case 5 | 6:
        classificacao = "Vestuário"
    case 7:
        classificacao = "Higiene pessoal"
    case 8 | 9 | 10:
        classificacao = "Limpeza e utensílios domésticos"
    case _:
        classificacao = "Código inválido"

# Exibindo a classificação
print(classificacao)

