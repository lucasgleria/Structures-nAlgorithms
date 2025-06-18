def organizar_cartas(cartas):
    for i in range(1, len(cartas)):
        chave = cartas[i]
        j = i - 1
        while j >= 0 and chave < cartas[j]:
            cartas[j + 1] = cartas[j]
            j -= 1
        cartas[j + 1] = chave
    return cartas

cartas = [10, 7, 15, 12, 9]
print(organizar_cartas(cartas)) 