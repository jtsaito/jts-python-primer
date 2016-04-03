"""Unittests for HSort"""

import random
import unittest
from hsort import HSort


class TestHSort(unittest.TestCase):
    "Test HSort class"

    def setUp(self):
        self.hsort = HSort()

    @classmethod
    def _random_list(cls, size, seed):
        random.seed(seed)

        random_list = [int(random.random()*size) for i in range(size)]
        sorted_list = list(random_list)

        sorted_list.sort()

        return random_list, sorted_list

    def test_sort_empty(self):
        """Sort empty list"""
        self.assertEqual(self.hsort.sort([]), [])

    def test_sort_one(self):
        """Sort list with one element"""
        self.assertEqual(self.hsort.sort([1]), [1])

    def test_sort_two_reversed(self):
        """Sort reversed list with two elements"""
        self.assertEqual(self.hsort.sort([2, 1]), [1, 2])

    def test_sort_two_ordered(self):
        """Sort sorted list with two elements"""
        self.assertEqual(self.hsort.sort([1, 2]), [1, 2])

    def test_sort_three_sorted(self):
        """Sort sorted list with three elements"""
        self.assertEqual(self.hsort.sort([1, 2, 3]), [1, 2, 3])

    def test_sort_three_reversed(self):
        """Sort reversed list with three elements"""
        self.assertEqual(self.hsort.sort([3, 2, 1]), [1, 2, 3])

    def test_sort_four_sorted(self):
        """Sort sorted list with four elements"""
        self.assertEqual(self.hsort.sort([1,2,3,4]), [1,2,3,4])

    def test_sort_four_reverse(self):
        """Sort reversed list with four elements"""
        self.assertEqual(self.hsort.sort([4,3,2,1]), [1,2,3,4])

    def test_sort_n_random(self):
        """sorts 16 random lists of size 33"""
        for random_seed in range(16):
            rand_list, sorted_list = TestHSort._random_list(33, random_seed)
            self.assertEqual(self.hsort.sort(list(rand_list)), sorted_list)

if __name__ == '__main__':
    unittest.main()
