vendas = [100, 150, 1500, 2000, 120]

meta = 140

# SE TODAS AS VENDAS FOREM ACIMA DA META A LOJA GANHA BÔNUS
print("Primeiro caso: ")
for venda in vendas:
    if venda < meta:
        print("A loja não atingiu a meta")
        break
    print(venda)

# EXIBINDO QUEM BATEU A META
print("Segundo caso:")
for venda in vendas:
    if venda < meta:
        continue
    print(venda)