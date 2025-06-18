def produtos_por_preco(produtos):
    n = len(produtos)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if produtos[j] < produtos[indice_minimo]:
                indice_minimo = j
        produtos[i], produtos[indice_minimo] = produtos[indice_minimo], produtos[i]
    return produtos

def organizar_produtos_por_preco(produtos):
    return sorted(produtos, key=lambda produto: produto["preco"])

produtos = [
    {"nome": "produto1", "preco": 1500},
    {"nome": "produto2", "preco": 3500},
    {"nome": "produto3", "preco": 2500},
    {"nome": "produto4", "preco": 500},
    {"nome": "produto5", "preco": 100},
]
print(organizar_produtos_por_preco(produtos))