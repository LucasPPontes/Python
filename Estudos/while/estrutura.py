# while condicao:
    # repete o código enquanto a condição for True

venda = input("Registre um produto: ")

vendas = []

while venda != "":
    vendas.append(venda)
    venda = input("Registre um produto: ")

print(f"{vendas} registrados")