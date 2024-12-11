class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.tamanho = 0

    def enfileirar(self, data):
        novoNo = Node(data)
        if self.start is None:
            self.start = novoNo
        
        if self.end:
            self.end.next = novoNo
        
        self.end = novoNo
        self.tamanho += 1
    
    def desenfileirar(self):
        currentNode = self.start

        if currentNode is None:
            print('Fila esta vazia. Não é possível desenfileirar!')
            return None
        
        self.start = self.start.next
        self.tamanho -= 1

        return currentNode.data
    
    def peek(self):
        if self.start is None:
            print('Fila está vazia. Não é possível olhar!')
            return None
        return self.start.data
    
    def printThis(self):
        currentNode = self.start
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

        print('tamanho atual é ' + str(self.tamanho))
    
fila = Queue()
fila.enfileirar(333)
fila.enfileirar(234)
fila.enfileirar('aaaaaaaa')
fila.printThis()
print('------------')
fila.desenfileirar()
fila.printThis()
