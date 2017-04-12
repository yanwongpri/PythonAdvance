# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


class M3U8Paser:
    def __init__(self, filepath):
        self.media_list = []
        try:
            with open(filepath) as f:
                lines = f.readlines()
                for line in lines:
                    if line[0] != '#':
                        self.media_list.append(line[:-1])
        except IOError as ie:
            print(ie)

    def get_media_list(self):
        return self.media_list
