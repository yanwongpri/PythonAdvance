# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

# LeetCode No.7
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321


class Solution(object):
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        # overflows, assumed 32bit int
        int_max_32 = 0x7fffff       # 2^31 - 1
        int_min_32 = -0x80000000    # -2^31
        ans = 0
        minus = False
        if x < 0:
            minus = True
            x *= -1
        while x != 0:
            ans = ans * 10 + (x % 10)
            x /= 10
        if minus:
            ans *= -1
        if ans < int_min_32 or ans > int_max_32:
            ans = 0
        return ans
