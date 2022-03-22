
import io
class ReadData:
    ''' r: read
    w: write
    a: añadir contenido a un fichero ya existente '''
    def __init__(self):
        self.archivo="Nodos_prueba.txt"
        ''' self.show_file_content() '''
        ''' self.show_file_content_v2() '''
        ''' self.write_in_file() '''
        ''' self.replace_file() '''
    #readline un elemento por linea
    def show_file_content():
        with io.open("Nodos_prueba.txt",'r+', encoding='utf-8') as data_file:
            file_line = data_file.readline()
            while(file_line != ''):
                #for line in self.file:
                print(file_line, end='')
                #Crear el incremento en la linea antes de salir while
                
                file_line = data_file.readline()
        data_file.close()
        
    def show_file_content_v3():
        datos = []
        with io.open("Nodos_prueba.txt",'r+', encoding='utf-8') as data_file:
            file_lines = data_file.readlines()
            for line in file_lines:
                datos.append(line.strip("\n"))          
        data_file.close()
        #print(datos)
        return datos
                
    def count_Lines(self):
        counter=0;
        with io.open("Nodos_prueba.txt",'r+', encoding='utf-8') as data_file:
            file_line = data_file.readline()
            
            while(file_line != ''):
                #for line in self.file:
                counter=counter+1
                #Crear el incremento en la linea antes de salir while
                file_line = data_file.readline()
                #print(counter)
               
        data_file.close()
        return counter
    #readlines nos devuelve una lista
    
    def show_file_content_v2():
        with io.open('Nodos_prueba.txt','r+', encoding='utf-8') as data_file:
            for line in data_file.readlines():
                print(line, end='')
        data_file.close()

    def write_in_file(value):
        #line_write = input('\n que deseas ingresar:\n   >>> ')
        with io.open('Nodos_prueba.txt','a', encoding='utf-8') as data_file:
            data_file.write('\n' + value)
        data_file.close()
        #self.show_file_content()
    
    def replace_file():
        line_write = input('\nNuevo contenido:\n   >>> ')
        with io.open('Nodos_prueba.txt','w', encoding='utf-8') as data_file:
            data_file.write(line_write)
        data_file.close()
        #self.show_file_content()
    def update_file_list(node_list):
        new_data= ''.join(node_list)
        with io.open('Nodos_prueba.txt',"w",encoding="utf-8") as data_file:
            for item in range (len(node_list)):
                data_file.write(node_list[item]+"\n")
        data_file.close()
        
        #hacer salto de linea e ingresar la linea nueva
    #def update_file():
        
        
        
        
    