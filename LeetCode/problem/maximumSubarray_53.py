# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


class Solution(object):
    @staticmethod
    def maxSubArray_On3(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for st in range(0, n):
            for ed in range(st+1, n):
                sum = 0
                for pos in range(st, ed):
                    sum += nums[pos]
                    if sum > ans:
                        ans = sum
        return ans

    @staticmethod
    def maxSubArray_On2(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for st in range(0, n):
            sum = 0
            for ed in range(st+1, n):
                sum += nums[ed]
                if sum > ans:
                    ans = sum
        return ans

    @staticmethod
    def maxSubArray_On(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        sj = 0
        si = 0
        minSi = 0
        for j in range(0, n):
            sj += nums[j]           # sum = si - minSi:
            if si < minSi:          # if sum < 0
                minSi = si          #   sum = 0
            if sj - minSi > ans:    # if sum + num[j] > ans
                ans = sj - minSi    #   ans = sum
            si += nums[j]           # sum += num[j]
        return ans

    # 贪心
    @staticmethod
    def maxSubArray_On_symble(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        sum = 0
        n = len(nums)
        for j in range(0, n):
            sum += nums[j]
            if sum < 0:
                sum = 0
            if sum + nums[j] > ans:
                ans = sum
            sum += nums[j]
        return ans



