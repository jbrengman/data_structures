import unittest
import queue


class QueueTests(unittest.TestCase):

    def setUp(self):
        self.queued = queue.Queue()
        for x in range(10, 0, -1):
            self.queued.enqueue(x)

    def test_enqueue(self):
        size = self.queued.size()
        self.queued.enqueue(100)
        self.assertEqual(size + 1, self.queued.size())
        self.assertEqual(10, self.queued.dequeue())

    def test_dequeue(self):
        for x in range(10, 0, -1):
            size = self.queued.size()
            dequeued = self.queued.dequeue()
            self.assertEqual(x, dequeued)
            self.assertEqual(size - 1, self.queued.size())
        self.assertRaises(IndexError, self.queued.dequeue)  # Empty queue

    def test_size(self):
        self.assertEqual(10, self.queued.size())
        self.assertEqual(0, queue.Queue().size())

    def test_str(self):
        expected = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
        self.assertEqual(expected, str(self.queued))
        self.queued.enqueue(11)
        expected = '11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
        self.assertEqual(expected, str(self.queued))
        self.queued.dequeue()
        expected = '11, 1, 2, 3, 4, 5, 6, 7, 8, 9'
        self.assertEqual(expected, str(self.queued))

if __name__ == '__main__':
    unittest.main()
