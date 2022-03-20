from read_data import ReadData
class SingleLinkedList:
    ''' Creamos una clase anidada en SingleLinkedList '''
    class Node:
        ''' Creamos el método inicializador de la clase '''
        def __init__(self, value):
            ''' Definimos la estructura de un nodo '''
            self.value = value
            self.linked_next_node = None
    ''' Metodo inicializador de la clase SingleLinkesList '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        #self.menu_options()
    
    ''' Método que imprime el contenido de la lista simplemente enlazada '''
    def show_nodes_list(self):
        node_list = []
        current_node = self.head
        ''' Recorremos la lista hasta que no existan nodos '''
        while(current_node != None):
            ''' A la lista node_list le agregamos al final el value del nodo visitado '''
            node_list.append(current_node.value)
            current_node = current_node.linked_next_node
        print(f'{node_list} Cantidad de nodos {self.length}')

    
    ''' Método que agrega un nodo nuevi al INICIO de la lista '''
    def prepend_node(self, value):
        new_node = self.Node(value)
        ''' Consultar si la lista NO tiene head y tail '''
        if self.head == None and self.tail == None:
            ''' En este caso la lista esta vacía, no contiene nodos '''
            self.head = new_node
            self.tail = new_node
        else:
            ''' En este caso, la lista contiene al menos un nodo '''
            ''' Para este caso habría que enlazar el nodo nuevo con la head de la lista '''
            new_node.linked_next_node = self.head
            ''' Actualizar la head de la lista '''
            self.head = new_node
        self.length += 1

    ''' Añadir nodo al final de la lista '''
    def append_node(self, value):
        ''' El nuevo nodo toma la estructura de Nodo '''
        new_node = self.Node(value)
        ''' Validar si la lista esta vacía '''
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            ''' Creamos el enlace de la tail actual de la lista con el nuevo nodo '''
            self.tail.linked_next_node = new_node
            self.tail = new_node
        self.length += 1

    ''' Eliminar primer nodo de la lista '''
    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            ''' Eliminamos la head de la lista '''
            remove_node = self.head
            ''' El nodo que le seguia al primero pasa a ser la head de la lista '''
            self.head = remove_node.linked_next_node
            ''' Eliminamos el enlace del nodo que se removera de la lista '''
            remove_node. linked_next_node = None
            self.length -= 1
            print(f'El value del nodo eliminado es {remove_node.value}') 

    ''' Eliminar ultimo nodo de la lista '''
    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            ''' Creamos una variable para iniciar al recorrido de la lista desde la head '''
            current_node = self.head
            ''' Creamos una variable que asignara el nuevo value de tail '''
            new_tail = current_node
            while(current_node.linked_next_node != None):
                new_tail = current_node
                current_node = current_node.linked_next_node
            self.tail = new_tail
            self.tail.linked_next_node = None
            self.length -= 1
            print(f'El value del nodo eliminado es {current_node.value}') 

    ''' Consultar el value de determinado nodo '''        
    def get(self, index):
        # Obtiene un nodo dado un index
        # Si el indice es el último nodo de la lista, nos referimos a la cola
        if index == self.length - 1:
            print(self.tail.value)
            return self.tail
        #Si el indice es el primer value de la lista, devolvemos el value de la cabeza
        elif index == 0:
            print(self.head.value)
            return self.head
        #De lo contrario, es porque el indice esta en una posición intermedia de la lista
        #Validar que el indice se encuentre entre los rangos permitidos de la lista
        elif not (index >= self.length or index < 0):
            current_node = self.head
            contador = 0
            #Recorremos la lista siempre y cuando el contador sea diferente al nodo a buscar
            while contador != index:
                #Incrementamos en uno el while pasando a visitar el siguiente nodo
                current_node = current_node.linked_next_node
                contador  += 1
            print(current_node.value)
            return current_node
        else:
            return None

    ''' Método que nos permite actualizar el valor del nodo '''
    def update(self,index, value):
        # Cambia el value de un nodo dado un index
        nodo_objetivo = self.get(index)
        if nodo_objetivo != None:
            #Reemplazamos el valor actual del nodo por el suministrado por el usuario
            nodo_objetivo.value = value
        else:
            return None


    # Agrega un elemento en donde sea en la linkedlist dado el index
    def insert(self, index, value):
        #Siempre que se desee crear un nuevo nodo es necesario solicitar el valor
        #Si el usuario quiere añadir el nodo al final de la lista, se llama la función append_node()
        if index == self.length + 1:
            return self.append_node(value)
        #Se valida si el nodo se quiere insertar en la cabeza de la lista
        elif index == 1:
            return self.prepend_node(value)
        #Se valida si el indice esta entre los rangos de la lista
        elif not (index >= self.length+1 or index <= 0):
            new_node = self.Node(value)
            previous_node = self.get(index-2)
            nodos_siguientes = previous_node.linked_next_node
            #Generamos los enlaces del nuevo nodo con el anterior y el siguiente
            previous_node.linked_next_node = new_node
            new_node.linked_next_node = nodos_siguientes
            self.length += 1
        else:
            return None

    
    # Saca un elemento de donde sea de la linkedlist dado el index
    def remove(self, index):
        #Si el usuario quiere eliminar el primer nodo de la lista
        if index == 1:
            return self.shift_node()
        #Si el usuario quiere eliminar el último nodo de la lista
        elif index == self.length:
            return self.pop_node()
        #Si el usuario quiere eliminar un nodo intermedio en la lista
        elif not (index > self.length or index <= 0):
            nodos_anteriores = self.get(index - 2)
            nodo_removido = nodos_anteriores.linked_next_node
            nodos_anteriores.linked_next_node = nodo_removido.linked_next_node
            nodo_removido.linked_next_node = None
            self.length -= 1
            return nodo_removido
        else:
            return None



    def reverse(self):
        # Revierte la linkedlist
        reverse_nodes = None
        #El nodo actual es la cabeza
        current_node = self.head
        #La cola pasa a ser la cabeza
        self.tail = current_node
        while current_node != None:
            linked_next_node = current_node.linked_next_node
            current_node.linked_next_node = reverse_nodes
            reverse_nodes = current_node
            current_node = linked_next_node
        self.head = reverse_nodes
        return self.head
    
    def prepend_data_lines (self):
        the_file= ReadData
        for i in range(the_file.count_Lines()):
            self.prepend_node(the_file.show_file_content())
            print("lo leyo")

    '''  def menu_options(self):
        print('*********SELECCIONA UNA OPCIÓN*********\n            1. Insertar nodo al final\n            2. Insertar nodo al inicio')
        while True:
            try:
                option_user = int(input('           >>>'))
                if(option_user != 1 and option_user != 2):
                    option_user = int(input('           >>>'))
                elif option_user == 1:
                    self.prepend_node()
                else:
                    self.append_node()
                #Validar si la lista tiene más de dos nodos para activar en el menu la opción de 
                #insertar el nodo
            except ValueError:
                print('*********Opción inválida*********') ''' 