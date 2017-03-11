# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

'''
This is and code temp of how to print progress in a line
There are three method in this file
using \r
using \b
and using the lib -> progressBar

Sources:
blog.ihipop.info/2010/10/1736.html

Example of Lib:
http://code.google.com/p/python-progressbar/source/browse/progressbar/examples.py
'''


from __future__ import division
from time import sleep
from progressbar import *
import sys


if __name__ == '__main__':
    # using \r
    # j = '#'
    # for i in range(1, 61):
    #     j += '#'
    #     sys.stdout.write(str(int((i / 60) * 100)) + '%  ||'+j+'->' + '\r')
    #     sys.stdout.flush()
    #     sleep(0.5)

    # using \b
    # for i in range(1, 61):
    #     sys.stdout.write('#'+'->'+'\b\b')
    #     sys.stdout.flush()
    #     sleep(0.5)

    # using lib -> progressBar
    # total = 1000
    # progress = ProgressBar()
    # for i in progress(range(total)):
    #     sleep(0.01)
    #
    # pbar = ProgressBar().start()
    # for i in range(1, 1000):
    #     pbar.update(int(i/(total-1))*100)
    #     sleep(0.01)
    # pbar.finish()

    # progressBar advances
    widgets = ['Progress:', Percentage(), '', Bar(marker=RotatingMarker('>=')),
               '', ETA(), '', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(10000000):
        # do something
        pbar.update(10*i+1)
        sleep(0.0001)
    pbar.finish()