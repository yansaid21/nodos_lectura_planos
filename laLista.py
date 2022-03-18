from multiprocessing.sharedctypes import Value


class SSingleLinkedList:
    #creamos una clase anidada en singleLinkedList
    class Node:
        def __init__(self,value):
            #definimos la estructura de un nodo
            self.value= Value
            self.next_node=None
    
    #moetodo inicializado de la clase single linkedList
    def __init__(self):
        self.head= None
        self.tail= None
        self.length = 0
        
    def show_Nodes_List(self):
        node_List=[]
        current_node = self.head
        #recorremos la lista hasta que no existan nodos
        while(current_node != None):
            #a la lista node_lista le agregamos al final el valor del nodo visitado
            node_List.append(current_node.value)
            current_node = current_node.next_node
        print(f"{node_List} cantidad de nodos {self.length}")
        #metodo que agrega un nodo a la lista
    def prepend_node(self,value):
        new_node=self.Node(value)
        if self.head == None and self.tail == None:
            #en este caso la lisa esta vacia, no contiene nodos 
            self.head = new_node
            self.tail = new_node
        else:
            #en este caso, la lista contiene al menos un nodo
            #para este caso habría que enlazar el nono
            new_node.next_node = self.head
            self.head =new_node
        self.length += 1
    def append_node(self,value):
        new_node=self.Node(value)
        if self.head == None and self.tail == None:
            #en este caso la lisa esta vacia, no contiene nodos 
            self.head = new_node
            self.tail = new_node
        else:
            #en este caso, la lista contiene al menos un nodo
            #para este caso habría que enlazar el nono
           self.tail.next_node =new_node
           self.tail =new_node
        self.length +=1
        
