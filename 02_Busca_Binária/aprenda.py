# A busca binária é um algoritmo eficiente para encontrar um item em uma lista já ordenada. Ela divide repetidamente a parte da lista que pode conter o item em duas metades, eliminando a metade onde o item não pode estar.

def busca_binaria(lista, alvo):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

# Exemplo
numeros_ordenados = [10, 20, 30, 40, 50, 60, 70, 80, 90]
numero_procurado = 50

print(busca_binaria(numeros_ordenados, numero_procurado))