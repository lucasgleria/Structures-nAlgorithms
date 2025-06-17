# A busca linear é o algoritmo de busca mais simples. Ele verifica sequencialmente cada elemento da lista até encontrar o item desejado ou chegar ao final da lista.

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

# Exemplo
minha_lista = [4, 2, 7, 1, 9, 5]
alvo_desejado = 7

print(busca_linear(minha_lista, alvo_desejado))