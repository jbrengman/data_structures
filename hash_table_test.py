import unittest
import hash_table


class HashTableTests(unittest.TestCase):

    def setUp(self):
        with open('words', 'r') as infile:
            self.wordlist = [line.strip() for line in infile]
        self.h = hash_table.HashTable()
        for word in self.wordlist:
            self.h.set(word, word)

    def test_set_and_get(self):
        for key in self.wordlist:
            expected = key
            result = self.h.get(key)
            self.assertEqual(expected, result)

    def test_invalid_key(self):
        self.assertRaises(ValueError, self.h.set, 1, 'keyisnotastring')

    def test_overwrite_value(self):
        before = self.h.get('before')
        self.h.set('before', 'not before')
        after = self.h.get('before')
        self.assertNotEqual(before, after)
        self.assertEqual(self.h.get('before'), 'not before')

if __name__ == '__main__':
    unittest.main()
