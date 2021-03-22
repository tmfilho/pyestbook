# Objetos e Classes

2.1. Implemente a classe UniformDistribution como uma subclasse da classe DiscreteDistribution da Seção anterior. 

class DiscreteDistribution:
    
    def __init__(self, params):
        self.params = params
        
    def pmf(self, x):
        pass
    
    def cdf(self, x):
        total = 0
        for v in range(x + 1):
            total += self.pmf(v)
        return total
    
    def mean(self):
        pass
    
    def variance(self):
        pass

class UniformDistribution(DiscreteDistribution):
    
    def pmf(self, x):
        a, b = self.params['a'], self.params['b']
        if a <= x <= b:
            return 1 / len(range(a, b + 1))
        else:
            return 0
    
    def mean(self):
        a, b = self.params['a'], self.params['b']
        return (a + b) / 2
    
    def variance(self):
        a, b = self.params['a'], self.params['b']
        return ((b - a + 1) ** 2 - 1) / 12

2.2. (Estrutura de dados: Lista encadeada). Uma lista encadeada é uma coleção de elementos em que cada elemento é um nó que "aponta" para o próximo membro da lista. Dessa forma, os elementos da lista formam uma cadeia cuja posição na memória não precisa ser contígua. Essa estrutura permite a inserção e a remoção eficiente de elementos em qualquer posição da lista, sem ser necessário deslocar "fisicamente" todos os outros membros. Uma desvatagem das listas é que o acesso a cada elemento não pode ser feita de forma direta, como em um array. É necessário navegar pela lista para encontrar o elemento desejado. Na sua forma mais simples, cada nó da lista contém dados e uma referência para o próximo elemento. Dessa forma, o último elemento da lista sempre apontará para uma referência nula. Variedades mais complexas adicionam referências extras, como para os elementos anteriores (lista duplamente encadeada). Implemente uma lista encadeada simples em Python, usando classes para a lista e para os nós, além das seguintes operações:

   1. Inserir elemento no início
   2. Inserir elemento no fim
   3. Inserir elemento em uma dada posição
   4. Verificar se um elemento está na lista
   6. Remover elemento com dado valor
   7. Remover começo da lista (cabeça) e retornar o seu valor
   8. Remover último elemento e retornar o seu valor
   9. Imprimir os valores da lista

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_end(self, value):
        new_node = Node(value)
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
    
    def insert(self, value, position):
        new_node = Node(value)
        i = 0
        previous = None
        current = self.head
        while current and i < position:
            previous = current
            current = current.next
            i += 1
        if previous:
            previous.next = new_node
        new_node.next = current
        if i == 0:
            self.head = new_node
    
    def find(self, value):
        found = False
        node = self.head
        while node and not found:
            if node.value == value:
                found = True
            node = node.next
        return found
    
    def remove_head(self):
        if self.head: # Para evitar erro, caso a lista encadeada esteja vazia
            node = self.head
            self.head = node.next
            return node.value
    
    def remove_end(self):
        if self.head:
            if self.head.next:
                node = self.head
                while node.next.next:
                    node = node.next
                end = node.next
                node.next = None
                return end.value
            else:
                end = self.head
                self.head = None
                return end.value
    
    def remove_value(self, value):
        if self.head:
            previous = None
            current = self.head
            while current and current.value != value:
                previous = current
                current = current.next
            if current:
                node = current
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return node.value
    
    def __str__(self):
        s = ''
        node = self.head
        while node:
            s += '{} -> '.format(node.value)
            node = node.next
        if s:
            return s
        else:
            return 'empty list'

2.3. (Estruturas de dados: Fila e Pilha). Fila e pilha são dois tipos especiais de listas encadeadas que se diferenciam pelas suas formas de adicionar e remover elementos. Nas filas, o primeiro elemento que entra deve ser sempre o primeiro a ser removido, comportamento conhecido em inglês como *First In First Out* (FIFO). As operações de inserir e remover na fila são conhecidas como *enfileirar* (*enqueue*) e *desenfileirar* (*dequeue*). Por outro lado, nas pilhas, o último elemento que entra deve ser o primeiro a sair, ou seja *Last In First Out* (LIFO). As operações de inserir e remover na pilha são conhecidas como *empilhar* (*push*) e *desempilhar* (*pop*). Implemente fila e pilha como subclasses da lista encadeada implementada no exercício anterior.

class Queue(LinkedList):
        
    def enqueue(self, value):
        super().insert_head(value)     
    
    def dequeue(self):
        return super().remove_end()
    
class Stack(LinkedList):
        
    def push(self, value):
        super().insert_head(value)     
    
    def pop(self):
        return super().remove_head()

2.4. Pilhas e filas possuem bastantes usos em sistemas computacionais. Por exemplo: as operações de *desfazer* e *refazer* de editores de texto e de *voltar* e *avançar* em navegadores são comumente implementadas usando duas pilhas. Implemente um simulador de editor de texto usando a função **input** de Python. O script irá registrar a *string* digitada pelo usuário e imprimir as últimas *strings* fornecidas. O usuário poderá fornecer três "*strings* especiais" que funcionarão como comandos: 'ctrl+z' fará o script descartar a última *string* digitada, 'ctrl+y' fará o script recuperar a última *string* descartada e 'stop' irá parar o scripts. Veja abaixo um exemplo de execução do script:

   1. *String* digitada: 'a'
      * Saída no console: 'a -> '
   2. *String* digitada: 'b'
      * Saída no console: 'b -> a -> '
   3. *String* digitada: 'c'
      * Saída no console: 'c -> b -> a -> '
   4. *String* digitada: 'ctrl+z'
      * Saída no console: 'b -> a -> '
   5. *String* digitada: 'ctrl+z'
      * Saída no console: 'a -> '
   6. *String* digitada: 'ctrl+y'
      * Saída no console: 'b -> a -> '
   7. *String* digitada: 'ctrl+y'
      * Saída no console: 'c -> b -> a -> '
   8. *String* digitada: 'stop'


s = Stack()
s2 = Stack()

value = input()
while value != 'stop':
    if value == 'ctrl+z':
        v = s.pop()
        s2.push(v)
        print(s)
    elif value == 'ctrl+y':
        v = s2.pop()
        s.push(v)
        print(s)
    else:
        s.push(value)
        print(s)
    value = input()