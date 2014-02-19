import unittest
import linked_list

class LinkedListTests(unittest.TestCase):

	def setUp(self):
		self.link = linked_list.LinkedList()
		for x in range(10, 0, -1):
			self.link.insert(x)

	def test_insert(self):
		size = self.link.size()
		self.link.insert(100)
		self.assertTrue(self.link.contains(100))
		self.assertEqual(size + 1, self.link.size())
		self.assertEqual(100, self.link.pop().value)

	def test_pop(self):
		for x in range(1, 11):
			size = self.link.size()
			popped = self.link.pop().value
			self.assertEqual(x, popped)
			self.assertEqual(size - 1, self.link.size()) # Assert the node was removed
		self.assertRaises(ValueError, self.link.pop) # Empty list


	def test_size(self):
		self.assertEqual(10, self.link.size())
		self.assertEqual(0, linked_list.LinkedList().size())


	def test_search(self):
		for x in range(1, 11):
			node = self.link.search(x)
			self.assertEqual(x, node.value)
		self.assertRaises(ValueError, self.link.search, 20)

	def test_remove(self):
		self.assertRaises(ValueError, self.link.remove, linked_list.Linked_node(20))
		size = self.link.size()
		for x in range(1, 11):
			self.assertTrue(self.link.contains(x))
			self.link.remove(self.link.search(x))
			self.assertFalse(self.link.contains(x))
			self.assertEqual(size - 1, self.link.size())
			size += -1


	def test_remove_by_value(self):
		self.assertRaises(ValueError, self.link.remove_by_value, 20)
		size = self.link.size()
		for x in range(1, 11):
			self.assertTrue(self.link.contains(x))
			self.link.remove_by_value(x)
			self.assertFalse(self.link.contains(x))
			self.assertEqual(size - 1, self.link.size())
			size += -1

	def test_contains(self):
		for x in range(1, 11):
			self.assertTrue(self.link.contains(x))
		for x in range(11, 20):
			self.assertFalse(self.link.contains(x))

	def test_str(self):
		expected = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
		self.assertEqual(str(expected), self.link.__str__())

if __name__ == '__main__':
	unittest.main()