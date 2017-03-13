# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com


# argpase demo
# Source:
# http://www.2cto.com/kf/201412/363654.html
# https://docs.python.org/2/library/argparse.html

import argparse
import sys

parser = argparse.ArgumentParser(description='test parsing arguments')

parser.add_argument('--filename', dest='filename', type=str)
parser.add_argument('--output', dest='output', type=str)

args = parser.parse_args()
print args
print args.filename
print args.output
