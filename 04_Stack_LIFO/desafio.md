### Uma pilha é uma estrutura de dados **LIFO** (Last-In, First-Out), o que significa que o último elemento adicionado é o primeiro a ser removido.

```python
class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None

# Exemplo
minha_pilha = Pilha()
minha_pilha.empilhar(10)
minha_pilha.empilhar(20)
item_removido = minha_pilha.desempilhar()

print(item_removido) # Imprime 20
print(minha_pilha.topo()) # Imprime 10
print(minha_pilha.desempilhar()) # Imprime 10
print(minha_pilha.desempilhar()) # Imprime None 
print(minha_pilha.topo()) # Imprime None 
```

## Seu desafio: Caso de Uso - Histórico de Navegação

Simule o **histórico de navegação de um navegador web** usando uma pilha. Implemente as funções `visitar_pagina(url)`, que adiciona a URL atual à pilha, e `voltar_pagina()`, que retorna à URL anterior (removendo-a da pilha). Se não houver histórico para voltar, retorne "Não há páginas anteriores."


### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça de que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente hein! 

Para fazer seu algoritmo, responda as perguntas:
- Qual método da Pilha reflete "visitar uma nova página"?
- Como "voltar" no histórico se relaciona com as operações da Pilha?
- O que acontece se você tentar voltar quando não há mais histórico?

## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.