def combinar_clientes(lista1, lista2):
    i = j = 0
    resultado = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            if not resultado or lista1[i] != resultado[-1]:
                resultado.append(lista1[i])
            i += 1
        elif lista2[j] < lista1[i]:
            if not resultado or lista2[j] != resultado[-1]:
                resultado.append(lista2[j])
            j += 1
        else:
            if not resultado or lista1[i] != resultado[-1]:
                resultado.append(lista1[i])
            i += 1
            j += 1

    while i < len(lista1):
        if not resultado or lista1[i] != resultado[-1]:
            resultado.append(lista1[i])
        i += 1

    while j < len(lista2):
        if not resultado or lista2[j] != resultado[-1]:
            resultado.append(lista2[j])
        j += 1
    return resultado

lista_clientes1 = ["Nome A", "Nome B", "Nome D", "Nome E"]
lista_clientes2 = ["Nome A", "Nome C", "Nome D", "Nome F"]
print("Lista combinada sem duplicatas:", combinar_clientes(lista_clientes1, lista_clientes2))