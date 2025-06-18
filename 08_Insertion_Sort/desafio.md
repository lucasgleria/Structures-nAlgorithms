### O Insertion Sort constrói a lista final ordenada um item por vez. Ele é um algoritmo de ordenação "in-place" e estável.

```python
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# Exemplo
valores_aleatorios = [12, 11, 13, 5, 6]
print(insertion_sort(valores_aleatorios)) # [5, 6, 11, 12, 13]
```

## Seu desafio: Caso de Uso - Cartas de Baralho

Imagine que você está organizando um baralho de cartas na sua mão. Implemente uma função `organizar_cartas(cartas)` que recebe uma lista de números inteiros representando as cartas (por exemplo, 1 para Ás, 11 para Valete, etc.) e as ordena usando o Insertion Sort, como se você estivesse inserindo cada nova carta na posição correta da sua mão.

### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein! ```(Ou será que é? Rs)```


## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.