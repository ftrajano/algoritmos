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

	def insert_begining
# Falta implementar os métodos de adicao de nos
# 1 - no inicio da lista
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

	llist.print_list()

	third.data = 5

	llist.print_list()

