#=========== Classe Nó ============#
class No:
    def __init__(self, elemento, proximo = None, anterior = None):
        self.elemento = elemento 
        self.__proximo = proximo 
        self.__anterior = anterior 

    @property
    def __proximo(self):
        return self.__proximo
    
    @__proximo.setter
    def __proximo(self, proximo):
        self.__proximo = proximo

    @property
    def __anterior(self):
        return self.__anterior
    
    @__anterior.setter
    def __anterior(self, anterior):
        self.__anterior = anterior
    
#=========== Classe DoublyLinkedList ============#
class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__tamanho = 0
        self.__cursor = None
    
    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head):
        self.head = head

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, tail):
        self.tail = tail
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho
    
    @property
    def cursor(self):
        return self.__cursor
    
    @cursor.setter
    def cursor(self, cursor):
        self.__cursor = cursor

    def getTamanho(self):
        return self.__tamanho

    def inserirNaFrente(self, elemento):
        if self.Vazia() == True:
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
        if self.Vazia() == True:
            self.inserirNaFrente(elemento)
        
        else:
            novo_no = No(elemento, None, self.__tail)
            self.__tail = novo_no
        
        self.__tamanho += 1
       
    def __avancarKPosicoes(self, k):
        if self.Vazia() == True:
            raise Exception("Lista Vazia")

        else:
            for i in range(k):
                if self.__cursor.proximo == None:
                    raise Exception("Não há elementos para avançar")
                else:
                    self.__cursor = self.__cursor.proximo


    def __retrocederKPosicoes(self, k):
        if self.Vazia() == True:
            raise Exception("Lista Vazia")

        else:
            for i in range(k):
                if self.__cursor.anterior == None:
                    raise Exception("Não há elementos para retornar")
                else:
                    self.__cursor = self.__cursor.anterior

    def __irParaPrimeiro(self):
        primeiro = self.__head
        return primeiro

    def __irParaUltimo(self):
        ultimo = self.__tail
        return ultimo
    
    def acessarAtual(self):
        return self.__cursor.elemento 

    def inserirAntesDoAtual(self, elemento):
        if self.__cursor == None:
            raise Exception("Não existe elemento atual")
        else:
            atual = self.__cursor 
            anterior = self.__cursor.anterior 
            novo_no = No(elemento, atual, anterior)
            self.__tamanho += 1

    def inserirAposAtual(self):
        pass

    def inserirNaPosicao(self, k, novo_elemento = No):
        if k < (self.__tamanho//2):
            self.__cursor.__irParaPrimeiro
            self.__cursor.__avancarKPosicoes(k)
            self.__cursor = novo_elemento
            
        else:
            self.__cursor.__irParaUltimo
            self.__cursor.__retrocederKPosicoes(k)
            self.__cursor = novo_elemento
        
        self.__tamanho += 1

    def ExcluirAtual(self):
        pass

    def ExcluirPrim(self):
        if self.Vazia() == True:
            raise Exception("Não existem elementos")
        else:
            self.__cursor.__irParaPrimeiro
            self.__cursor.elemento = None
            self.__tamanho -= 1

    def ExcluirUlt(self):
        pass

    def ExcluirElem(chave):
        pass

    def ExlcuirDaPos(self, k):
        if k < (self.__tamanho//2):
            self.__cursor.__irParaPrimeiro
            self.__cursor.__avancarKPosicoes(k)
            self.__cursor = None
            
        else:
            self.__cursor.__irParaUltimo
            self.__cursor.__retrocederKPosicoes(k)
            self.__cursor = None
        
        self.__tamanho -= 1
        pass
    
    def Buscar(chave):
        pass

    def Vazia(self):
        return (self.__head == None and self.__tail == None)
    
    def Cheia(self):
        return (self.__head == None and self.__tail == None)