class Linked_list:

	def __init__(self):
		self.head = None

	def insert(self, val):
		node = Linked_node(val)
		node.next = self.head
		self.head = node

	def pop(self):
		temp = self.head
		self.head = self.head.next
		return temp

	def size(self):
		n = 0
		if self.head:
			node = self.head
			while (not node == None):
				n += 1
				node = node.next
		return n

	def search(self, val):
		if self.head:
			node = self.head
			while (node.next != None):
				if (node.value == val):
					return node
				node = node.next
			if (node.value == val):
				return node
		return None

	def remove(self, rem_node):
		if self.head:
			node = self.head
			while (node.next != None): # node.next.value == rem_node.value ??
				if (node.next == rem_node):
					node.next = node.next.next
					return
				node = node.next
		return None

	def print_list(self):
		tup = 'error'
		if self.head:
			node = self.head
			tup = (node.value,)
			while (node.next.next):
				node = node.next
				tup += (node.value,)
			tup += (node.next.value,)
		print tup

	# def print_list(self):
	# 	node = self.head
	# 	tup = (node.value,)
	# 	while (node.next.value):
	# 		node = node.next
	# 		tup += (node.value,)
	# 	print tup


class Linked_node:

	def __init__(self, val):
		self.value = val
		self.next = None

