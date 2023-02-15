# Tupla é uma lista imutável

# Estrutura:
    # tupla = (valor1,valor2,...)

# Vantages:
    # Mais eficiente em termos de performance
    # Protege a base de dados (por ser imutável)
    # Muito usado para dados heterogêneos

vendas = ("Lucas", "25/10/2010", "30/10/2010", 2000, "Estag")

nome = vendas[0]
data_nascimento = vendas[1]
data_contratado = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(nome,data_nascimento,data_contratado,salario,cargo)