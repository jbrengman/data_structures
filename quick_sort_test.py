import unittest
import quick_sort
from random import randrange


class InsertionSortTest(unittest.TestCase):

    def test_sort(self):
        ''' Compare results of sorting a random list with insertion sort
        against sorting that same list using Python's built sorting. '''
        test_list = []
        for x in range(10000):
            test_list.append(randrange(0, 10000))
        expected = sorted(test_list)
        result = quick_sort.sort(test_list)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
