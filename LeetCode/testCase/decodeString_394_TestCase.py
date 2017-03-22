import unittest
from LeetCode.problem.decodeString_394 import Solution


class MyTestCase(unittest.TestCase):

    TEST_CASE_1 = "3[a]2[bc]"
    TARGET_1 = "aaabcbc"
    TEST_CASE_2 = "3[a2[c]]"
    TARGET_2 = "accaccacc"
    TEST_CASE_3 = "2[abc]3[cd]ef"
    TARGET_3 = "abcabccdcdcdef"
    TEST_CASE_4 = "100[leetcode]"
    TARGET_4 = "leetcode"*100

    def test_decodeString(self):
        # ans_1 = Solution.decodeString(self.TEST_CASE_1)
        # self.assertEqual(ans_1, self.TARGET_1)
        # ans_2 = Solution.decodeString(self.TEST_CASE_2)
        # self.assertEqual(ans_2, self.TARGET_2)
        # ans_3 = Solution.decodeString(self.TEST_CASE_3)
        # self.assertEqual(ans_3, self.TARGET_3)
        ans_4 = Solution.decodeString(self.TEST_CASE_4)
        self.assertEqual(ans_4, self.TARGET_4)

if __name__ == '__main__':
    unittest.main()
