import unittest
from Base.UnionFind.UnionFind import UnionFind


class UnionFindTestCase(unittest.TestCase):
    def test_unionFind(self):
        uf = UnionFind(10)
        self.assertEqual(uf.count, 10)
        uf.union(4, 3)
        self.assertEqual(uf.find(4), uf.find(4))
        self.assertEqual(uf.count, 9)
        uf.union(3, 8)
        uf.union(6, 5)
        uf.union(9, 4)
        uf.union(2, 1)
        self.assertEqual(uf.count, 5)

        # 8 3 4 9 is connected, So 8 9 can not union.
        self.assertEqual(uf.find(8) == uf.find(9), True)
        uf.union(8, 9)
        self.assertEqual(uf.count, 5)

        uf.union(5, 0)
        self.assertEqual(uf.count, 4)
        uf.union(7, 2)
        uf.union(6, 1)
        self.assertEqual(uf.count, 2)

        # 0 5 6 1 2 7 is connected, So 1 0 can not union
        self.assertEqual(uf.find(1) == uf.find(0), True)
        uf.union(1, 0)
        self.assertEqual(uf.count, 2)

        # same as 6 7
        self.assertEqual(uf.find(6) == uf.find(7), True)
        uf.union(6, 7)
        self.assertEqual(uf.count, 2)


if __name__ == '__main__':
    unittest.main()
