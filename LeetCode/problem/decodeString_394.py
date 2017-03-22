# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

# Example
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# s = "2[2[b]]"


class Solution(object):
    @staticmethod
    def decodeString(s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(['', 1])
        nums = ''
        for ch in s:
            if ch.isdigit():
                nums += ch
            elif ch == '[':
                stack.append(['', int(nums)])
                nums = ''
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch

        return stack[0][0]