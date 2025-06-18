class Fila_da_impressora:
    def __init__(self):
        self.itens = []
    
    def adicionar_documento(self, documento):
        self.itens.append(documento)
    
    def imprimir_documento(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def tamanho(self):
        return len(self.itens)
    
    def gerenciar_impressora(self):
        documento = self.imprimir_documento(); 
        if documento is None: 
            print("Não há documentos para imprimir") 
        else: 
            print(f"Imprimindo documento: {documento}")

fila_de_impressao = Fila_da_impressora()
fila_de_impressao.adicionar_documento("Documento 1")
fila_de_impressao.adicionar_documento("Documento 2")
fila_de_impressao.gerenciar_impressora() 
fila_de_impressao.gerenciar_impressora() 
fila_de_impressao.gerenciar_impressora() 