class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.items = 0

    def enqueue(self, val):
        '''Insert val at head of the queue (end of the line)'''
        self.head, self.head.next = Queue_node(val), self.head
        if self.items == 0:  # If queue was empty
            self.tail = self.head
        else:
            self.head.next.prev = self.head  # Set prev of (now) second node
        self.items += 1

    def dequeue(self):
        '''Removes and returns the last item in the queue.'''
        if self.items == 0:
            raise IndexError('Queue is empty.')
        node, self.tail = self.tail, self.tail.prev
        if self.items > 1:
            self.tail.next = None
        self.items -= 1
        return node.value

    def size(self):
        '''Returns the number of items in the queue.'''
        return self.items

    def __str__(self):
        s = ''
        node = self.head
        while node:
            s = s + str(node.value) + ', '
            node = node.next
        s = s[:-2]
        return s


class Queue_node:

    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
