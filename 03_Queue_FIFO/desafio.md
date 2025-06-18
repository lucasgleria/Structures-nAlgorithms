### Uma fila é uma estrutura de dados **FIFO** (First-In, First-Out), o que significa que o primeiro elemento adicionado é o primeiro a ser removido.

```python
class Fila:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

# Exemplo
minha_fila = Fila()
minha_fila.adicionar("Tarefa A")
minha_fila.adicionar("Tarefa B")
primeira_tarefa = minha_fila.remover()

print(primeira_tarefa) # Imprime Tarefa A
print(minha_fila.remover()) # Imprime Tarefa B
print(minha_fila.remover()) # Imprime None
```

## Seu desafio: Caso de Uso - Fila de Impressão

Crie uma **fila de impressão** que simule o gerenciamento de documentos. Implemente uma função `gerenciar_impressora()` que permita adicionar documentos à fila (com seus nomes) e processá-los (removendo-os da fila e "imprimindo-os" - apenas uma mensagem na tela). Se a fila estiver vazia, indique que não há documentos para imprimir.

### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein! 

Para fazer seu algoritmo, responda as perguntas:
- Como a classe da Fila de impressão deve se comportar?
- O que acontece se a impressora não tiver documentos?
- Como "simular" a impressão?
## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.