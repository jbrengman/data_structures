class Stack:

    def __init__(self):
        self.head = None
        self.items = 0

    def push(self, val):
        '''Insert val at head of the stack'''
        self.head, self.head.next = Stack_node(val), self.head
        self.items += 1

    def pop(self):
        '''Removes and returns the first node of the stack.'''
        if self.head:
            node, self.head = self.head, self.head.next
            self.items -= 1
            return node.value
        raise IndexError('Stack is empty.')

    def size(self):  # Does a stack need a size method?
        '''Returns the number of items in the stack.'''
        return self.items

    def __str__(self):
        s = ''
        node = self.head
        while node:
            s = s + str(node.value) + ', '
            node = node.next
        s = s[:-2]
        return s


class Stack_node:

    def __init__(self, val):
        self.value = val
        self.next = None
