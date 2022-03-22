import io
class ReadData:
    
    def __init__(self):
        self.archivo=("Nodos_prueba.txt")
        #self.show_file_content_v2()
        #self.write_in_file()
        #self.replace_file()
    #readline un elemento por linea
    def show_file_content(self):
        with io.open('Nodos_prueba.txt','r+', encoding='utf-8') as data_file:
            file_line = data_file.readline()
            while(file_line != ''):
                #for line in self.file:
                print(file_line, end='')
                #Crear el incremento en la linea antes de salir while
                file_line = data_file.readline()
        data_file.close()
        
    def show_file_content_v3(self):
        datos = []
        with io.open(self.archivo,'r+', encoding='utf-8') as data_file:
            file_lines = data_file.readlines()
            for line in file_lines:
                datos.append(line.strip("\n"))          
        data_file.close()
        #print(datos)
        return datos
                
    def count_Lines(self):
        counter=0;
        with io.open(self.archivo,'r+', encoding='utf-8') as data_file:
            file_line = data_file.readline()
            
            while(file_line != ''):
                #for line in self.file:
                counter+=1
                #Crear el incremento en la linea antes de salir while
                file_line = data_file.readline()
                #print(counter)
               
        data_file.close()
        return counter
    #readlines nos devuelve una lista
    
    def show_file_content_v2(self):
        with io.open(self.archivo,'r+', encoding='utf-8') as data_file:
            for line in data_file.readlines():
                print(line, end='')
        data_file.close()

    def write_in_file(self,value):
        #line_write = input('\n que deseas ingresar:\n   >>> ')
        with io.open(self.archivo,'a', encoding='utf-8') as data_file:
            data_file.write('\n' + value)
        data_file.close()
        #self.show_file_content()
    
    def replace_file(self):
        line_write = input('\nNuevo contenido:\n   >>> ')
        with io.open(self.archivo,'w', encoding='utf-8') as data_file:
            data_file.write(line_write)
        data_file.close()
        #self.show_file_content()
    def update_file_list(self,node_list):
        
        with io.open(self.archivo,"w",encoding="utf-8") as data_file:
            for item in range (len(node_list)):
                data_file.write(node_list[item]+"\n")
        data_file.close()
        
        #hacer salto de linea e ingresar la linea nueva
    def update_file_by_index(self,index,value):
        counter=0
        datos= self.show_file_content_v3()
        ''' with io.open(self.archivo,'w', encoding='utf-8') as data_file:
            file_lines = data_file.readlines() '''
            

        datos.insert(index,value) 
        self.update_file_list(datos)
             
        #data_file.close()
        #print(datos)
        
            
            
        
    def replace_file_v2(self,archivo):
        current_node=self.list_nodes.head
        with io.open(archivo,'w',encoding='utf-8') as data_file:
            while current_node!=None:
                data_file.write(current_node.value.strip()+'\n')
                current_node=current_node.next_node
        data_file.close() 