import unittest
from LeetCode.problem.medianOfTwoSortedArrays_4 import Solution


class MyTestCase(unittest.TestCase):

    TEST_CASE_1 = [[1, 3], [2]]
    TARGET_1 = 2
    TEST_CASE_2 = [[1, 2], [3, 4]]
    TARGET_2 = 2.5
    TEST_CASE_3 = [[1, 2], [1, 2]]
    TARGET_3 = 1.5

    def test_find_median_sorted_arrays(self):
        # ans_1 = Solution.find_median_sorted_arrays(self.TEST_CASE_1[0], self.TEST_CASE_1[1])
        # self.assertEqual(ans_1, self.TARGET_1)
        # ans_2 = Solution.find_median_sorted_arrays(self.TEST_CASE_2[0], self.TEST_CASE_2[1])
        # self.assertEqual(ans_2, self.TARGET_2)
        ans_3 = Solution.find_median_sorted_arrays(self.TEST_CASE_3[0], self.TEST_CASE_3[1])
        self.assertEqual(ans_3, self.TARGET_3)


if __name__ == '__main__':
    unittest.main()
