import random


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
