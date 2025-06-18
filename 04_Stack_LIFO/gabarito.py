class Histórico_de_navegação:
    def __init__(self):
        self.itens = []
    
    def visitar_pagina(self, url):
        self.itens.append(url)
    
    def voltar_pagina(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return "Não há páginas anteriores"
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return "Não há páginas anteriores"

histórico = Histórico_de_navegação()
histórico.visitar_pagina("https://Url1.com")
histórico.visitar_pagina("https://Url2.com")
histórico.visitar_pagina("https://Url3.com")

print(histórico.topo())
print(histórico.voltar_pagina())
print(histórico.voltar_pagina())
print(histórico.voltar_pagina())
print(histórico.topo())
