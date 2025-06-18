### A busca binária é um algoritmo eficiente para encontrar um item em uma **lista já ordenada**. Ela divide repetidamente a parte da lista que pode conter o item em duas metades, eliminando a metade onde o item não pode estar.

```python
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
```

## Seu desafio: Caso de Uso - Dicionário Telefônico

Você possui um **dicionário telefônico** representado por uma lista de tuplas ordenadas alfabeticamente pelo nome, onde cada tupla é `(nome, telefone)`. Implemente a função `buscar_telefone(lista_contatos, nome_procurado)` que utilize a busca binária para encontrar o telefone de um contato. Se o contato não for encontrado, retorne "Contato não encontrado".

### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein! 

Para fazer seu algoritmo, responda as perguntas:
- O que é uma lista de tuplas e como utilizar na linguagem que estou usando?
- Como vou acessar o valor dentro da lista de tuplas?
- Qual tipagem de output devo retornar exatamente?

## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.