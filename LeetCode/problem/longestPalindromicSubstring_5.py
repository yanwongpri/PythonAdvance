# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


def is_palindrome(low, high, s, length):
    if length == 0 or length == 1:
        return 1
    if s[low] != s[high]:
        return 0
    return is_palindrome(low + 1, high - 1, s, length - 2)


class Solution(object):

    @staticmethod
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        length = len(s)
        for i in range(length):
            for j in range(i+1, length+1):
                sub_str = s[i:j]
                is_pal = True
                while len(sub_str) != 0:
                    if len(sub_str) == 1:
                        break
                    if sub_str[0] != sub_str[-1]:
                        is_pal = False
                        break
                    sub_str = sub_str[1:-1]
                if is_pal:
                    if len(s[i:j]) > len(ans):
                        ans = s[i:j]
        return ans


    @staticmethod
    def longestPalindrome_v1(s):
        ans = ''
        length = len(s)
        for i in range(length):
            sub_str = s[i]
            for j in range(i + 1, length):
                sub_str += s[j]
                if sub_str[0] == sub_str[-1]:
                    if (len(sub_str) == 2 or len(sub_str) == 3) and len(sub_str) > len(ans):
                        ans = sub_str
                    else:
                        tmp_str = sub_str[1:-1]
                        is_pal = True
                        while len(tmp_str) != 0:
                            if len(tmp_str) == 1:
                                break
                            if tmp_str[0] != tmp_str[-1]:
                                is_pal = False
                                break
                            tmp_str = tmp_str[1:-1]
                        if is_pal:
                            if len(sub_str) > len(ans):
                                ans = sub_str
        return ans


    @staticmethod
    def longestPalindrome_ce(s):
        length = len(s)
        maxlength = 0
        start = 0

        if length == 1:
            return s

        # odd
        for i in range(0, length):
            j = i - 1
            k = i + 1
            while j >= 0 and k < length and s[j] == s[k]:

                if k-j+1 > maxlength:
                    maxlength = k-j+1
                    start = j
                j -= 1
                k += 1

        # even
        for i in range(length):
            j = i
            k = i + 1
            while j >= 0 and k < length and s[j] == s[k]:
                if k-j+1 > maxlength:
                    maxlength = k-j+1
                    start = j
                j -= 1
                k += 1

        if maxlength > 0:
            return s[start:start+maxlength]
        elif maxlength == 0 and s[0] == s[-1]:
            return s[0]
        return None


    @staticmethod
    def is_pal(str):
        sub_str = str[:]
        is_p = True
        while len(sub_str) != 0:
            if len(sub_str) == 1:
                break
            if sub_str[0] != sub_str[-1]:
                is_p = False
                break
            sub_str = sub_str[1:-1]
        return is_p

