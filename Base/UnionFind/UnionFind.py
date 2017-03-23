# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.id = []
        for i in range(n):
            self.id.append(i)

    def count(self):
        return self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        for i in range(0, len(self.id)):
            if self.id[i] == pId:
                self.id[i] = qId
        self.count -= 1


