class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Pilha:
    def __init__(self): 
        self.topo = None
        self.tamanho = 0

    def empilhar(self, data):
        novoNo = Node(data)
        novoNo.next = self.topo 
        self.topo = novoNo      
        self.tamanho += 1

    def desempilhar(self):
        if self.topo is None:
            print("Pilha está vazia. Não é possível desempilhar!")
            return None
        noRemovido = self.topo
        self.topo = self.topo.next 
        self.tamanho -= 1
        return noRemovido.data

    def peek(self):
        if self.topo is None:
            print("Pilha está vazia. Não é possível espiar!")
            return None
        return self.topo.data

    def printThis(self):
        currentNode = self.topo
        print("Elementos na pilha:")
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next
        print("Tamanho atual é " + str(self.tamanho))


pilha = Pilha()
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.printThis()

print("------------")
print("Elemento removido:", pilha.desempilhar())
pilha.printThis()

print("------------")
print("Elemento no topo:", pilha.peek())

