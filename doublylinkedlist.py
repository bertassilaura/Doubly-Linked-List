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
    

class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__tamanho = 0
        self.__cursor = None

    def getTamanho(self):
        return self.__tamanho

    def inserirNaFrente(self, elemento):
        if self.__tamanho == 0:
            self.__head = No(elemento)
            self.__tail = self.__head
            self.__cursor = self.__head
        
        else:
            novo_no = No(elemento, self.__head)
            self.__head.anterior = novo_no
            self.__head = novo_no
            self.__cursor.no = self.__head
        
        self.__tamanho += 1

    def inserirNoFim(self, elemento):
        if self.__tamanho == 0:
            self.inserirNaFrente(elemento)
        
        else:
            novo_no = No(elemento, None, self.__tail)
            self.__tail = novo_no
        
        self.__tamanho += 1
       
    def __avancarKPosicoes(self, k):
        pass

    def __retrocederKPosicoes(self, k):
        pass

    def __irParaPrimeiro(self):
        primeiro = self.__head
        return primeiro

    def __irParaUltimo(self):
        ultimo = self.__tail
        return ultimo

    def inserirAntesDoAtual(self):
        pass

    def inserirAposAtual(self):
        pass

    def inserirNaPosicao(self):
        pass

    def ExcluirAtual(self):
        pass

    def ExcluirPrim(self):
        pass

    def ExcluirUlt(self):
        pass

    def ExcluirElem(chave):
        pass

    def ExlcuirDaPos(k):
        pass
    
    def Buscar(chave):
        pass

    def Vazia(self):
        return (self.__head == None and self.__tail == None)
    
    def Cheia(self):
        return (self.__head == None and self.__tail == None)