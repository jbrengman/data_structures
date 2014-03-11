import unittest
import bst
import random


class BinarySearchTreeTests(unittest.TestCase):

    def setUp(self):
        self.tree = bst.BinarySearchTree()
        self.tree_values_list = []
        for x in range(100):
            n = random.randrange(0, 1000)
            self.tree_values_list.append(n)
            self.tree.insert(n)

    def test_insert(self):
        # Add 100 numbers not already in tree
        count = 0
        inserted_values = []
        while count < 100:
            n = random.randrange(0, 1000)
            if n not in self.tree_values_list:
                # self.assertFalse(self.tree.contains(n))
                inserted_values.append(n)
                self.tree.insert(n)
                count += 1
        for x in inserted_values:
            self.assertTrue(self.tree.contains(x))

    def test_contains(self):
        for x in self.tree_values_list:
            self.assertTrue(self.tree.contains(x))
        # Find 100 values that should not be in the tree, make sure they're not
        count = 0
        while count < 100:
            n = random.randrange(0, 1000)
            if n not in self.tree_values_list:
                self.assertFalse(self.tree.contains(n))
                count += 1

    def test_size(self):
        expected = 100
        result = self.tree.size()
        self.assertEqual(expected, result)
        count = 0
        while count < 100:
            n = random.randrange(0, 1000)
            if n not in self.tree_values_list:
                self.tree.insert(n)
                count += 1
        expected = 200
        result = self.tree.size()
        self.assertEqual(expected, result)

    def test_depth(self):
        # Depth is dependent on order of insertion, so it does not make sense
        # to test a non self-balancing tree with random values.
        vals = [50, 40, 60, 35, 45, 55, 65]
        depth_tree = bst.BinarySearchTree()
        for x in vals:
            depth_tree.insert(x)
        expected = 3
        result = depth_tree.depth()
        self.assertEqual(expected, result)
        depth_tree.insert(47)
        expected = 4
        result = depth_tree.depth()
        self.assertEqual(expected, result)
        depth_tree.insert(51)
        expected = 4
        result = depth_tree.depth()
        self.assertEqual(expected, result)
        depth_tree.insert(48)
        expected = 5
        result = depth_tree.depth()
        self.assertEqual(expected, result)
        depth_tree.insert(49)
        expected = 6
        result = depth_tree.depth()
        self.assertEqual(expected, result)

    def test_balance(self):
        # Assuming depth() and _depth() functions work correctly.
        expected = (self.tree._depth(self.tree.root.left)
                    - self.tree._depth(self.tree.root.right))
        result = self.tree.balance()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
