import unittest
import stack


class StackTests(unittest.TestCase):

    def setUp(self):
        self.stacked = stack.Stack()
        for x in range(10, 0, -1):
            self.stacked.push(x)

    def test_push(self):
        size = self.stacked.size()
        self.stacked.push(100)
        self.assertEqual(size + 1, self.stacked.size())
        self.assertEqual(100, self.stacked.pop())

    def test_pop(self):
        for x in range(1, 11):
            size = self.stacked.size()
            popped = self.stacked.pop()
            self.assertEqual(x, popped)
            self.assertEqual(size - 1, self.stacked.size())
        self.assertRaises(IndexError, self.stacked.pop)  # Empty list

    def test_size(self):
        self.assertEqual(10, self.stacked.size())
        self.assertEqual(0, stack.Stack().size())

    def test_str(self):
        expected = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
        self.assertEqual(expected, str(self.stacked))

if __name__ == '__main__':
    unittest.main()
