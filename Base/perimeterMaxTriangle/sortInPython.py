# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
