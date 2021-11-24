from node import Node

class LinkedList:

	def __init__(self):
		self.head  = None


	def print_list(self):
		node = self.head
		while(node.next !=None):
			print(node.data)
			node=node.next
		print(node.data)

	def push(self, value):
		'''Function to insert a new node at the beginning'''
	#achei que precisaria testar se o head era vazio, mas caso fosse nao teria problema colocar None com o
	#next do new_node logo nao precisa testar pra saber se o head é None.
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node

	def insertAfter(self, prev_node, value):
		'''Given a prev_node, insert a new node after the given'''
		#precisa testar se o nó dado é None?
		#Pra mim não precisaria
		new_node = Node(value)
		new_node.next = prev_node.next
		prev_node.next = new_node 
		

	
# Falta implementar os métodos de adicao de nos
# 1 - no inicio da lista - ok
# 2 - depois de um no específico
# 3 - no final da lista


if __name__ == '__main__':

	#Startr with the empty list
	
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	llist.head.next = second
	second.next = third
	third.data = 5
	llist.push(21)
	llist.insertAfter(second, 10)
	llist.print_list()
	
