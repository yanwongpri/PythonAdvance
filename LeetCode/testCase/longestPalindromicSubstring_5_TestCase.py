import unittest
from LeetCode.problem.longestPalindromicSubstring_5 import Solution


class MyTestCase(unittest.TestCase):

    TEST_CASE_1 = 'babad'
    TARGET_1 = 'bab'
    TEST_CASE_2 = 'cbbd'
    TARGET_2 = 'bb'

    def test_longestPalindrome(self):
        ans_1 = Solution.longestPalindrome(self.TEST_CASE_1)
        self.assertEqual(ans_1, self.TARGET_1)
        ans_2 = Solution.longestPalindrome(self.TEST_CASE_2)
        self.assertEqual(ans_2, self.TARGET_2)

    def test_longestPalindrome_v1(self):
        ans_1 = Solution.longestPalindrome_v1(self.TEST_CASE_1)
        self.assertEqual(ans_1, self.TARGET_1)
        ans_2 = Solution.longestPalindrome_v1(self.TEST_CASE_2)
        self.assertEqual(ans_2, self.TARGET_2)

    def test_is_pal(self):
        ans = Solution.is_pal('abba')
        self.assertEqual(ans, True)


if __name__ == '__main__':
    unittest.main()
