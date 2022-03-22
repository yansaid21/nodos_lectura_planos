from singleLinkedList import SingleLinkedList
from read_data2 import ReadData

inst_sll = SingleLinkedList()
inst_read_data = ReadData()

#inst_sll.prepend_data_lines()
#inst_sll.show_nodes_list()
inst_sll.menu_options()
print(inst_read_data.count_Lines())

''' A, B, C, D'''
''' inst_sll.prepend_node('B')
inst_sll.prepend_node('A')
inst_sll.append_node('C')
inst_sll.append_node('D')
inst_sll.append_node('E')

inst_sll.show_nodes_list()

inst_sll.insert(1, "Head")
inst_sll.insert(7, "Tail")
inst_sll.insert(2, "Neigthbord Head") '''
''' ['Head', 'Neigthbord Head', 'A', 'B', 'C', 'D', 'E', 'Tail'] '''
''' inst_sll.show_nodes_list()
inst_sll.remove(2) '''
''' ['Head', 'A', 'B', 'C', 'D', 'E', 'Tail'] '''
''' inst_sll.remove(1) '''
''' ['A', 'B', 'C', 'D', 'E', 'Tail'] '''
''' inst_sll.remove(6) '''
''' ['A', 'B', 'C', 'D', 'E'] '''
''' inst_sll.show_nodes_list()
inst_sll.reverse()
inst_sll.show_nodes_list() '''
