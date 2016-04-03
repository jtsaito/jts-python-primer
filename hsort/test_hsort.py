import random
import unittest
from hsort import HSort

class TestHeapfiy(unittest.TestCase):

    def setUp(self):
        self.hsort = HSort()

    @classmethod
    def _random_list(cls, size, seed):
        random.seed(seed)

        random_list = [ int(random.random()*size) for i in range(size) ]
        sorted_list = list(random_list)

        sorted_list.sort()

        return random_list, sorted_list

    def test_sort_empty(self):
        self.assertEqual(self.hsort.sort([]), [])

    def test_sort_one(self):
        self.assertEqual(self.hsort.sort([1]), [1])

    def test_sort_two_reversed(self):
        self.assertEqual(self.hsort.sort([2, 1]), [1, 2])

    def test_sort_two_ordered(self):
        self.assertEqual(self.hsort.sort([1, 2]), [1, 2])

    def test_sort_three_ordered(self):
        self.assertEqual(self.hsort.sort([1, 2, 3]), [1, 2, 3])

    def test_sort_three_reversed(self):
        self.assertEqual(self.hsort.sort([3, 2, 1]), [1, 2, 3])

    def test_sort_four_sorted(self):
        self.assertEqual(self.hsort.sort([1,2,3,4]), [1,2,3,4])

    def test_sort_four_reverse(self):
        self.assertEqual(self.hsort.sort([4,3,2,1]), [1,2,3,4])

    def test_sort_four_random(self):
        self.assertEqual(self.hsort.sort([4,3,2,1]), [1,2,3,4])

    def test_sort_n_random(self):
        for random_seed in range(16):
            rand_list, sorted_list = _random_list(33, random_seed)
            self.assertEqual(self.hsort.sort(list(rand_list)), sorted_list)

if __name__ == '__main__':
    unittest.main()
