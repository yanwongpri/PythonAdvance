# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


class Solution(object):

    @staticmethod
    def bubble_sort(lists):
        count = len(lists)
        for i in range(0, count):
            for j in range(i + 1, count):
                if lists[i] > lists[j]:
                    lists[i], lists[j] = lists[j], lists[i]
        return lists

    @staticmethod
    def perimeter_max_base(sides_list):
        n = len(sides_list)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    length = sides_list[i] + sides_list[j] + sides_list[k]
                    ma = max(sides_list[i], max(sides_list[j], sides_list[k]))
                    rest = length - ma
                    if ma < rest:
                        ans = max(ans, length)
        return ans

    @staticmethod
    def perimeter_max_upgrade(sides_list):
        n = len(sides_list)
        ans = 0
        sorted_sides_list = Solution.bubble_sort(sides_list)
        for i in range(n-1, 2, -1):
            length = sorted_sides_list[i] + sorted_sides_list[i-1] + sorted_sides_list[i-2]
            rest = length - sorted_sides_list[i]
            if sorted_sides_list[i] < rest:
                ans = length
        return ans
