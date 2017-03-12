import unittest
from LeetCode.problem.reverseInteger_7 import Solution


class SolutionCase(unittest.TestCase):
    def test_reverse(self):
        test_num_1 = 123
        self.assertEqual(Solution.reverse(test_num_1), 321)
        test_num_2 = -123
        self.assertEqual(Solution.reverse(test_num_2), -321)
        test_num_3 = pow(2, 31) + 100
        self.assertEqual(Solution.reverse(test_num_3), 0)
        test_num_4 = -pow(2, 31) - 100
        self.assertEqual(Solution.reverse(test_num_4), 0)


if __name__ == '__main__':
    unittest.main()
