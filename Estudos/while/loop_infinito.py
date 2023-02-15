vendas = [100,90,80,50,40]
vendedores = ["Maria","Jão","José","Paula","Marta"] 

meta = 50 
i = 0

while vendas[i] > meta:
    print(f"{vendedores[i]} bateu a meta. Vendas {vendas[i]}")
    i += 1