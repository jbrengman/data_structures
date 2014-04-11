import unittest
import radix_sort
from random import randrange


class RadixSortTest(unittest.TestCase):

    def test_sort(self):
        ''' Compare results of sorting a random list with insertion sort
        against sorting that same list using Python's built sorting. '''
        test_list = []
        for x in range(10000):
            test_list.append(randrange(0, 100000))
        expected = sorted(test_list)
        result = radix_sort.sort_int(test_list)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
