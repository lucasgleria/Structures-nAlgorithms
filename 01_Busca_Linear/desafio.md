### A busca linear é o algoritmo de busca mais simples. Ele verifica sequencialmente cada elemento da lista até encontrar o item desejado ou chegar ao final da lista.

```python
def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

# Exemplo
minha_lista = [4, 2, 7, 1, 9, 5]
alvo_desejado = 7

print(busca_linear(minha_lista, alvo_desejado)) # Imprime 2 
```

## Seu desafio: Caso de Uso - Inventário de Produtos

Imagine que você tem um **inventário de produtos** em um e-commerce, representado por uma lista de dicionários, onde cada dicionário contém o 'nome' e o 'id' de um produto. Implemente a função `encontrar_produto_por_id(inventario, id_produto)` que utilize a busca linear para retornar o dicionário completo do produto correspondente ao `id_produto` fornecido. Se o produto não for encontrado, retorne `None`.

### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein! 

Para fazer seu algoritmo, responda as perguntas:
- O que é uma lista de dicionários e como utilizar na linguagem que estou usando?
- Como vou acessar o valor dentro da lista de dicionários?
- Qual tipagem de output devo retornar exatamente?


## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.