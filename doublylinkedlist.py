#criando a classe nó
class No:
    def __init__(self, elemento, proximo = None, anterior = None):
        self.elemento = elemento 
        self.proximo = proximo 
        self.anterior = anterior 

    @property
    def elemento(self):
        return self.elemento

    @elemento.setter
    def elemento(self, elemento):
        self.elemento = elemento

    @property
    def proximo(self):
        return self.proximo
    
    @proximo.setter
    def proximo(self, proximo):
        self.proximo = proximo

    @property
    def anterior(self):
        return self.anterior
    
    @anterior.setter
    def anterior(self, anterior):
        self.anterior = anterior
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0

    def getTamanho(self):
        return self.tamanho

    def InserirNaFrente(self, elemento):
        if self.tamanho == 0:
            self.head = No(elemento)
            self.tail = self.head
        
        else:
            novo_no = No(elemento, self.head)
            self.head.anterior = novo_no
            self.head = novo_no
        
        self.tamanho += 1

    def InserirNoFim(self, elemento):
        if self.tamanho == 0:
            self.InserirNaFrente(elemento)
        
        else:
            novo_no = No(elemento, None, self.tail)
            self.tail = novo_no
        
        self.tamanho += 1

    def InserirAntesDoAtual(self):
        pass

    def InserirAposAtual(self):
        pass