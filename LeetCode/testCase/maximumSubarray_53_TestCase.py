import unittest
from LeetCode.problem.maximumSubarray_53 import Solution


class SolutionTestCase(unittest.TestCase):

    TEST_CASE = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    TEST_RESULT = 6

    def test_maxSubArray_On3(self):
        ans = Solution.maxSubArray_On3(self.TEST_CASE)
        self.assertEqual(ans, self.TEST_RESULT)

    def test_maxSubArray_On2(self):
        ans = Solution.maxSubArray_On2(self.TEST_CASE)
        self.assertEqual(ans, self.TEST_RESULT)

    def test_maxSubArray_On(self):
        ans = Solution.maxSubArray_On(self.TEST_CASE)
        self.assertEqual(ans, self.TEST_RESULT)

    def test_maxSubArray_On_symble(self):
        ans = Solution.maxSubArray_On(self.TEST_CASE)
        self.assertEqual(ans, self.TEST_RESULT)


if __name__ == '__main__':
    unittest.main()
