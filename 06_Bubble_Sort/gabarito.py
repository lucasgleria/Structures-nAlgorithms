def classificar_pontuacoes(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
             if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

pontuacoes = [100, 90, 85, 70, 60, 50, 40, 30, 20, 10, 0]
pontuacoes_desordenadas = [0, 20, 100, 70, 40, 60, 50, 10, 90, 85, 30]
print(classificar_pontuacoes(pontuacoes))
print(classificar_pontuacoes(pontuacoes_desordenadas))