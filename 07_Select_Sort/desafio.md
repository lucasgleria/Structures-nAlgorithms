### O Selection Sort seleciona repetidamente o menor (ou maior) elemento da parte não ordenada da lista e o move para a parte ordenada.

```python
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Exemplo
dados_misturados = [29, 13, 22, 37, 52, 46, 71]
print(selection_sort(dados_misturados)) # [13, 22, 29, 37, 46, 52, 71]
```

## Seu desafio: Caso de Uso - Organização de Produtos por Preço

Uma loja online precisa organizar seus **produtos por preço** (do menor para o maior). Implemente uma função `organizar_produtos_por_preco(produtos)` que recebe uma lista de produtos (onde cada produto é um dicionário com chaves 'nome' e 'preco') e os ordena usando o algoritmo Selection Sort com base no preço.

### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein! 

Para fazer seu algoritmo, responda as perguntas:
- O que é uma lista de dicionários?
- Ao comparar dois produtos, qual parte deles você deve realmente comparar para determinar qual é o "menor" em termos de preço? 
- Quando você encontra o produto com o menor preço e precisa trocá-lo de lugar, você deve trocar apenas o preço ou o dicionário inteiro que representa o produto? Por que isso é importante para manter as informações do produto corretas?


## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.