# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


class Solution(object):
    @staticmethod
    def find_median_sorted_arrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        median = 0
        if (m + n) % 2 != 0:
            ans_avg = False
        else:
            ans_avg = True
        ans = []

        while len(nums1) > 0 and len(nums2) > 0 and len(ans) < ((m + n) / 2 + 1):
            if nums1[-1] > nums2[-1]:
                ans.append(nums1.pop())
            elif nums1[-1] == nums2[-1]:
                ans.append(nums1.pop())
            else:
                ans.append(nums2.pop())

        if len(ans) < ((m + n) / 2 + 1):
            if len(nums1) == 0:
                nums = nums2
            else:
                nums = nums1
            while len(ans) < ((m + n) / 2 + 1):
                ans.append(nums.pop())

        if ans_avg:
            median = (ans[-1] + ans[-2]) / 2.0
        else:
            median = ans[-1] / 1.0
        return median
