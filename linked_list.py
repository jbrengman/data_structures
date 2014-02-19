class LinkedList:

	def __init__(self):
		self.head = None

	def insert(self, val):
		'''Insert val at head of the linked list'''
		node = Linked_node(val)
		node.next = self.head
		self.head = node

	def pop(self):
		'''Removes and returns the first node of the linked list.'''
		if (self.head):
			temp = self.head
			self.head = self.head.next
			return temp
		raise ValueError('List is empty.')

	def size(self):
		'''Returns the number of items in the linked list.'''
		n = 0
		if self.head:
			node = self.head
			n = 1
			while (node.next):
				node = node.next
				n += 1
		return n

	def search(self, val):
		'''Returns the node containing val.'''
		if self.head:
			node = self.head
			if (node.value == val):
				return node
			while (node.next):
				node = node.next
				if (node.value == val):
					return node
		raise ValueError('Item not found')

	def remove(self, rem_node):
		'''Removes the node rem_node if rem_node is a node in the linked list.'''
		if self.head:
			node = self.head
			if (node == rem_node): 
			# If first node of list is the node to be removed
				self.head = self.head.next
				return
			while (node.next):
				if (node.next == rem_node):
					if (node.next.next):
					# If the node being removed is not the last item in the list 
						node.next = node.next.next
					else: node.next = None 
					return
				node = node.next
		raise ValueError('Item not found')

	def remove_by_value(self, val):
		'''Removes the first node in the linked list whose value is val.'''
		if self.head:
			node = self.head
			if (node.value == val):
			# If first node of list is the node to be removed
				self.head = self.head.next
				return
			while (node.next):
				if (node.next.value == val):
					if (node.next.next):
					# If the node being removed is not the last item in the list 
						node.next = node.next.next
					else: node.next = None 
					return
				node = node.next
		raise ValueError('Item not found')

	def contains(self, val):
		if (self.head):
			node = self.head
			if (node.value == val):
				return True
			while (node.next):
				node = node.next
				if (node.value == val):
					return True
		return False

	def __str__(self):
		tup = ()
		if self.head:
			node = self.head
			tup = (node.value,)
			while (node.next):
				node = node.next
				tup += (node.value,)
		return str(tup)




class Linked_node:

	def __init__(self, val):
		self.value = val
		self.next = None

