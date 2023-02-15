estoque = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

fabrica = ["fab1","fab2","fab3"]

for i, lista in enumerate(estoque):
    for qtde in lista:
        if qtde < 10:
            print(fabrica[i])