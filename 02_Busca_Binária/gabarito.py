def buscar_telefone(lista_contatos, nome_procurado):
    baixo = 0
    alto = len(lista_contatos) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        contato_no_meio = lista_contatos[meio]
        nome_no_meio = contato_no_meio[0]

        if nome_no_meio == nome_procurado:
            return contato_no_meio[1] 
        elif nome_no_meio < nome_procurado:
            baixo = meio + 1
        else: 
            alto = meio - 1
            
    return "Contato não encontrado"

dicionario_telefonico = [
    ("Nome 1", 123456789),
    ("Nome 2", 123456788),
    ("Nome 3", 123456787),
    ("Nome 4", 123456786),
    ("Nome 5", 123456785)
]

print(buscar_telefone(dicionario_telefonico, "Nome 4"))
print(buscar_telefone(dicionario_telefonico, "Nome Inexistente"))