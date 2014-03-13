import random
from queue import Queue


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            self._size += 1
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.value:
            if not node.left:
                node.left = TreeNode(val)
                self._size += 1
            else:
                return self._insert(val, node.left)
        elif val > node.value:
            if not node.right:
                node.right = TreeNode(val)
                self._size += 1
            else:
                return self._insert(val, node.right)

    def contains(self, val):
        return self._contains(val, self.root)

    def _contains(self, val, node):
        if node is None:
            return False
        if val < node.value:
            return self._contains(val, node.left)
        if val > node.value:
            return self._contains(val, node.right)
        return node.value == val

    def size(self):
        return self._size

    def depth(self):
        return self._depth(self.root)

    def _depth(self, node):
        if node is None:
            return 0
        return 1 + max(self._depth(node.left), self._depth(node.right))

    def balance(self):
        return self._depth(self.root.left) - self._depth(self.root.right)

    def save_dot(self):
        with open('bst.dot', 'w') as outfile:
            outfile.write(self.root.get_dot())

    def in_order_traversal(self):
        for x in self._in_order_traversal(self.root):
            yield x

    def _in_order_traversal(self, node):
        if node.left:
            for x in self._in_order_traversal(node.left):
                yield x
        yield node.value
        if node.right:
            for x in self._in_order_traversal(node.right):
                yield x

    def pre_order_traversal(self):
        for x in self._pre_order_traversal(self.root):
            yield x

    def _pre_order_traversal(self, node):
        yield node.value
        if node.left:
            for x in self._pre_order_traversal(node.left):
                yield x
        if node.right:
            for x in self._pre_order_traversal(node.right):
                yield x

    def post_order_traversal(self):
        for x in self._post_order_traversal(self.root):
            yield x

    def _post_order_traversal(self, node):
        if node.left:
            for x in self._post_order_traversal(node.left):
                yield x
        if node.right:
            for x in self._post_order_traversal(node.right):
                yield x
        yield node.value

    def breadth_first_traversal(self):
        q = Queue()
        q.enqueue(self.root)
        while q.size() > 0:
            current = q.dequeue()
            yield current.value
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)

    def remove(self, val):
        if self.root.value == val:
            self.root = self.replace_removed(self.root)
        else:
            self._remove(val, self.root)

    def _remove(self, val, current):
        if val < current.value:
            if not current.left:
                raise IndexError('Value not found.')
            elif current.left.value == val:
                current.left = self.replace_removed(current.left)
            else:
                self._remove(val, current.left)
        elif val > current.value:
            if not current.right:
                raise IndexError('Value not found.')
            elif current.right.value == val:
                current.right = self.replace_removed(current.right)
            else:
                self._remove(val, current.right)

    def replace_removed(self, current):
        if not current.left and not current.right:
            return None
        elif not current.right:
            return current.left
        elif not current.left:
            return current.right
        replacement = self._replace_removed(current.right)
        replacement.left, replacement.right = current.left, current.right
        return replacement

    def _replace_removed(self, current):
        if current.left.left is None:
            replacement = current.left
            current.left = self.replace_removed(current.left)
            return replacement
        else:
            return self._replace_removed(current.left)

    def __str__(self):
        gen = self.breadth_first_traversal()
        as_list = []
        s = ', '
        try:
            while True:
                as_list.append(str(gen.next()))
        except StopIteration:
            pass
        s = s.join(as_list)
        return s


class TreeNode(object):

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.value = val

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.value is None else (
            "\t%s;\n%s\n" % (
                self.value,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)


def _test():
    '''Create a tree for testing.'''
    b = BinarySearchTree()
    nums = [20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 27, 32, 37]
    for num in nums:
        b.insert(num)
    return b


if __name__ == '__main__':
    '''
    Add values 1 - 900 to two binary search trees, one in order, the other
    in random order, and then compare the average lookup times for all
    values 1 - 900.
    '''
    from time import time
    linear_tree = BinarySearchTree()
    random_tree = BinarySearchTree()
    val_list = []
    for x in range(1, 901):
        val_list.append(x)
    for val in val_list:
        linear_tree.insert(val)
    random.shuffle(val_list)
    for val in val_list:
        random_tree.insert(val)
    linear_time = 0
    random_time = 0
    for x in range(1, 901):
        start = time()
        linear_tree.contains(x)
        t = time() - start
        linear_time += t
        start = time()
        random_tree.contains(x)
        t = time() - start
        random_time += t
    linear_avg = linear_time / 900
    random_avg = random_time / 900
    print(
        'Linear BST average lookup time for values 1 - 900: %s' % linear_avg)
    print(
        'Random BST average lookup time for values 1 - 900: %s' % random_avg)
