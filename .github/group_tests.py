import unittest
from group import groups_of_3

class testing(unittest.TestCase):
    def test_groups_of_3(self):
        nums = [3, 4, 7, 21, 99, 100, 44]
        expected = [[3, 4, 7], [21, 99, 100], [44]]
        result = groups_of_3(nums)
        self.assertEqual(expected, result)

    def test_groups_of_32(self):
        nums = [1,2,3,4,5,6,7,8,9]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = groups_of_3(nums)
        self.assertEqual(expected, result)

    def test_groups_of_33(self):
        nums = []
        expected = []
        result = groups_of_3(nums)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()