vendas = ("Lucas", "25/10/2010", "30/10/2010", 2000, "Estag")

# modo padrão
nome = vendas[0]
data_nascimento = vendas[1]
data_contratado = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(nome, data_nascimento, data_contratado, salario, cargo)

# unpacking

nome, nascimento, contratacao, salario, cargo = vendas

print(nome, nascimento, contratacao, salario, cargo)

vendas = [100, 200, 300]
funcionarios = ["João", "Ana", "Maria"]

for i, venda in enumerate(vendas):
    print(f"{funcionarios[i]} vendeu {venda}")
