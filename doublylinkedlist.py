#criando a classe nó
from typing_extensions import ParamSpec


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
    
class Cursor:
    def __init__(self, no = None):
        self.no = no
        
    def __avancarKPosicoes(self, k):
        pass

    def __retrocederKPosicoes(self, k):
        pass

    def __irParaPrimeiro(self):
        pass

    def __irParaUltimo(self):
        pass

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0
        self.cursor = Cursor()

    def getTamanho(self):
        return self.tamanho

    def inserirNaFrente(self, elemento):
        if self.tamanho == 0:
            self.head = No(elemento)
            self.tail = self.head
            self.cursor = self.head
        
        else:
            novo_no = No(elemento, self.head)
            self.head.anterior = novo_no
            self.head = novo_no
            self.cursor.no = self.head
        
        self.tamanho += 1

    def inserirNoFim(self, elemento):
        if self.tamanho == 0:
            self.inserirNaFrente(elemento)
        
        else:
            novo_no = No(elemento, None, self.tail)
            self.tail = novo_no
        
        self.tamanho += 1

    def inserirAntesDoAtual(self):
        pass

    def inserirAposAtual(self):
        pass