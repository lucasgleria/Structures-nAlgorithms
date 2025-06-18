### Uma lista encadeada é uma coleção de elementos (nós) onde cada nó contém um dado e uma referência (link) para o próximo nó na sequência.

```python
class Nó:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, dado):
        novo_nó = Nó(dado)
        if not self.cabeca:
            self.cabeca = novo_nó
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_nó

    def imprimir(self):
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(elementos))

# Exemplo
minha_lista_encadeada = ListaEncadeada()
minha_lista_encadeada.adicionar(1) # 1
minha_lista_encadeada.adicionar(2) # 1 -> 2
minha_lista_encadeada.adicionar(3) # 1 -> 2 -> 3

minha_lista_encadeada.imprimir() # Terminal: 1 -> 2 -> 3
```

## Seu desafio: Caso de Uso - Playlist de Músicas

Crie uma **playlist de músicas** usando uma lista encadeada. Implemente as funções `adicionar_musica(titulo)`, que adiciona uma música ao final da playlist, e `remover_musica(titulo)`, que remove uma música específica da playlist. A função de remoção deve lidar com o caso da música não existir.

### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein! 

Para fazer seu algoritmo, responda as perguntas:
- Como você adicionaria uma nova música (nó) se a playlist estiver vazia? E se já houver músicas, como você encontraria o final da playlist para adicionar a nova música?
- Ao remover uma música, qual é o caso mais simples (e talvez o mais perigoso) que você precisa tratar primeiro? Em outras palavras, o que acontece se a música a ser removida for a primeira da playlist?
- Para remover uma música que não é a primeira, como você faria para "pular" o nó que contém a música que você quer remover, fazendo com que o nó anterior aponte para o nó seguinte ao removido? E o que fazer se a música que você procura não for encontrada na playlist?


## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.