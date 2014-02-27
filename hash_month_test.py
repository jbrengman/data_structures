import unittest
import hash_month
import datetime


class HashMonthTests(unittest.TestCase):

    def setUp(self):
        self.test_month = hash_month.HashMonth.make_month(2014, 2)

    def test_day(self):
        d = datetime.date(2014, 2, 1)
        while (d.month == 2):
            expected = d.strftime('%A')[:2]
            result = self.test_month.day(d.day)
            self.assertEqual(expected, result)
            d += datetime.timedelta(days=1)

    def test_invalid_day(self):
        self.assertRaises(IndexError, self.test_month.day, 32)


if __name__ == '__main__':
    unittest.main()
