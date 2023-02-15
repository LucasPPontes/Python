vendas = []

while True:

    produto = input("Produto: ")
    if not produto:
        break
    quantidade = int(input("Quantidade: "))

    vendas.append([produto,quantidade])

print(vendas)