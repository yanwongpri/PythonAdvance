import unittest
from Base.perimeterMaxTriangle.perimeterMaxTriangle import Solution


class MyTestCase(unittest.TestCase):

    TEST_CASE_1 = [2,3,4,5,10]
    TARGET_1 = 12
    TEST_CASE_2 = [4,5,10,20]
    TARGET_2 = 0

    def test_perimeter_max_base(self):
        ans_1 = Solution.perimeter_max_base(self.TEST_CASE_1)
        self.assertEqual(ans_1, self.TARGET_1)
        ans_2 = Solution.perimeter_max_base(self.TEST_CASE_2)
        self.assertEqual(ans_2, self.TARGET_2)

    def test_permieter_max_upgrade(self):
        ans_1 = Solution.perimeter_max_upgrade(self.TEST_CASE_1)
        self.assertEqual(ans_1, self.TARGET_1)
        ans_2 = Solution.perimeter_max_upgrade(self.TEST_CASE_2)
        self.assertEqual(ans_2, self.TARGET_2)


if __name__ == '__main__':
    unittest.main()
