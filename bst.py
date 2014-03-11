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
