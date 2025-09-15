class No:
    def __init__(self, data):
        self.data = data
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.__tamanho = 0

    def vazia(self):
        return self.inicio is None

    def add_fim(self, data):
        novoNo = Node(data)
        if self.inicio is None:
          self.inicio = novoNo
        else:
          self.fim = novoNo

    def inserir(self, i, data):
        novoNo = Node(data)
        if i == 0:
          if self.inicio is None:
            self.inicio = self.fim = novoNo
          else:
            novoNo.proximo = self.inicio
            self.inicio.anterior = novoNo
            self.inicio = novoNo
        else:
          atual = self.inicio
          index = 0
          while atual is not None and index < i:
            atual = atual.proximo
            index += 1
          if atual is None:
            self.add_fim(data)
          else:
            anterior = atual.anterior
            anterior.proximo = novoNo
            novoNo.anterior = anterior
            novoNo.proximo = atual
            atual.anterior = novoNo

minha_lista = Lista()
minha_lista.add_inicio(10)
minha_lista.add_fim(20)
