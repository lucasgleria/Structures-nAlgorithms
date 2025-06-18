class Nó:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Playlist:
    def __init__(self):
        self.cabeca = None

    def adicionar_musica(self, dado):
        novo_nó = Nó(dado)
        if not self.cabeca:
            self.cabeca = novo_nó
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_nó

    def remover_musica(self, dado):
        if not self.cabeca:
            return
        if self.cabeca.dado == dado:
            self.cabeca = self.cabeca.proximo
            return
        atual = self.cabeca
        while atual.proximo and atual.proximo.dado != dado:
            atual = atual.proximo
        if atual.proximo:
            atual.proximo = atual.proximo.proximo

    def fila_de_reproduçao(self):
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(elementos))

minha_playlist = Playlist()
minha_playlist.adicionar_musica("Musica1")
minha_playlist.adicionar_musica("Musica2")
minha_playlist.adicionar_musica("Musica3")
minha_playlist.fila_de_reproduçao()

minha_playlist.remover_musica("Musica2")
minha_playlist.fila_de_reproduçao()