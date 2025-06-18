### O Bubble Sort é um algoritmo de ordenação simples que repetidamente percorre a lista, compara pares de elementos adjacentes e os troca se estiverem na ordem errada.

```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Exemplo
desordenados = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(desordenados)) # [11, 12, 22, 25, 34, 64, 90] 

```

## Seu desafio: Caso de Uso - Classificação de Pontuações de Jogos

Você está desenvolvendo um jogo e precisa classificar as **pontuações dos jogadores** do menor para o maior. Implemente uma função `classificar_pontuacoes(pontuacoes)` que recebe uma lista de pontuações e as ordena usando o algoritmo Bubble Sort.


### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein!  ```(Ou será que é? Rs)```


## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.