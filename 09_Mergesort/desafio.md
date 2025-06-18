### O Mergesort é um algoritmo de ordenação eficiente, geral e baseado em comparação. A maioria das implementações utiliza o conceito de "dividir e conquistar".

```python
def mergesort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = mergesort(esquerda)
    direita = mergesort(direita)

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# Exemplo
dados_para_ordenar = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(dados_para_ordenar)) # [3, 9, 10, 27, 38, 43, 82]
```

## Seu desafio: Caso de Uso - Combinar Listas de Clientes

Duas agências de marketing diferentes possuem listas de **clientes potenciais** (representadas por listas de strings com os nomes). Cada lista já está ordenada alfabeticamente. Implemente uma função `combinar_clientes(lista1, lista2)` que utiliza a lógica de *merge* do Mergesort para combinar e ordenar as duas listas em uma única lista sem duplicatas.

### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein! 

Para fazer seu algoritmo, responda as perguntas:
- Como você pode percorrer as duas listas de clientes ao mesmo tempo, comparando os nomes para decidir qual adicionar à nova lista combinada? Quais "ponteiros" você precisaria para isso? 
- As listas já estão ordenadas alfabeticamente. Se você encontrar o mesmo nome em ambas as listas (uma duplicata), como você pode garantir que ele seja adicionado à lista final apenas uma vez?
- Depois de comparar todos os elementos que se sobrepõem nas duas listas, o que acontece com os elementos restantes em uma das listas que ainda não foram adicionados à lista combinada? Como você garantiria que eles sejam incluídos no final?


## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.