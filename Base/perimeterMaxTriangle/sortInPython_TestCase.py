import unittest
from Base.perimeterMaxTriangle.sortInPython import *


class MyTestCase(unittest.TestCase):

    TEST_LISTS = [3, 6, 1, 8, 2, 10]
    SORT_RESULT = [1, 2, 3, 6, 8, 10]

    def test_bubble_sort(self):
        sorted_list = bubble_sort(self.TEST_LISTS)
        self.assertEqual(sorted_list, self.SORT_RESULT)


if __name__ == '__main__':
    unittest.main()
