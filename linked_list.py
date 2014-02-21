class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, val):
        '''Insert val at head of the linked list'''
        self.head, self.head.next = Linked_node(val), self.head

    def pop(self):
        '''Removes and returns the first node of the linked list.'''
        if (self.head):
            node = self.head
            self.head = self.head.next
            return node
        raise ValueError('List is empty.')

    def size(self):
        '''Returns the number of items in the linked list.'''
        n = 0
        node = self.head
        while (node):
            node = node.next
            n += 1
        return n

    def search(self, val):
        '''Returns the node containing val.'''
        node = self.head
        while (node):
            if (node.value == val):
                return node
            node = node.next
        raise ValueError('Item not found')

    def remove(self, rem_node):
        '''Removes rem_node if rem_node is a node in the linked list.'''
        node = self.head
        if (node == rem_node):
            self.head = node.next
            return
        while (node):
            if (node.next == rem_node):
                node.next = node.next.next
                return
            node = node.next
        raise ValueError('Item not found')

    def remove_by_value(self, val):
        '''Removes the first node in the linked list whose value is val.'''
        node = self.head
        if (node.value == val):
            self.head = node.next
            return
        while (node.next):
            if (node.next.value == val):
                node.next = node.next.next
                return
            node = node.next
        raise ValueError('Item not found')

    def contains(self, val):
        node = self.head
        while (node):
            if (node.value == val):
                return True
            node = node.next
        return False

    def __str__(self):
        tup = ()
        node = self.head
        while (node):
            tup += (node.value,)
            node = node.next
        return str(tup)


class Linked_node:

    def __init__(self, val):
        self.value = val
        self.next = None
